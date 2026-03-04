"""Parser for the PFR 'Quarterback Wins vs. Each Franchise' page.

Parses ``/friv/qb-wins.htm`` including the table listing quarterbacks
who have beaten every (or nearly every) NFL franchise.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._helpers import safe_int


class QBWinsParser:
    """Parses the PFR quarterback wins page."""

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title.

        The page uses an ``<h2>`` rather than an ``<h1>`` for the main
        heading, so we fall back to the ``<title>`` tag.
        """
        content = soup.find("div", id="content")
        if content:
            h2 = content.find("h2")
            if h2:
                return h2.get_text(strip=True)
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.get_text(strip=True)
        return ""

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the qb_wins stats table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            # Player name, href, and id
            player_cell = row.find(["th", "td"], {"data-stat": "player"})
            if not player_cell:
                continue

            player_name = player_cell.get_text(strip=True)
            player_href: Optional[str] = None
            player_id: Optional[str] = player_cell.get("data-append-csv") or None

            link = player_cell.find("a")
            if link and link.get("href"):
                player_href = link["href"]

            # Teams beat (integer)
            teams_beat_cell = row.find(["th", "td"], {"data-stat": "teams_beat"})
            teams_beat = (
                safe_int(teams_beat_cell.get_text(strip=True)) if teams_beat_cell else 0
            ) or 0

            # Teams not beat (comma-separated string → list)
            teams_not_beat_cell = row.find(
                ["th", "td"], {"data-stat": "teams_not_beat"}
            )
            teams_not_beat: List[str] = []
            if teams_not_beat_cell:
                raw = teams_not_beat_cell.get_text(strip=True)
                if raw:
                    teams_not_beat = [t.strip() for t in raw.split(",")]

            entry: Dict[str, Any] = {
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "teams_beat": teams_beat,
                "teams_not_beat": teams_not_beat,
            }

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the quarterback wins page.

        Args:
            html: Raw HTML of the PFR quarterback wins page.

        Returns:
            A dict ready for ``QBWins.model_validate()``.

        Raises:
            ParsingError: If the qb_wins table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="qb_wins")
        if table is None:
            raise ParsingError(
                "Could not find qb_wins table in the HTML.",
                selector="qb_wins",
                html_sample=html[:500],
            )

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
