"""Parser for the PFR 'Cups of Coffee' page.

Parses ``/friv/coffee.htm`` including the table listing all players
who played only a single game in the NFL, with their career statistics
from that one game.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._helpers import safe_int

# Columns that should be parsed as integers.
_INT_COLS = frozenset(
    {
        "all_pros_first_team",
        "pro_bowls",
        "years_as_primary_starter",
        "career_av",
        "g",
        "pass_cmp",
        "pass_att",
        "pass_yds",
        "pass_td",
        "pass_long",
        "pass_int",
        "pass_sacked",
        "pass_sacked_yds",
        "rush_att",
        "rush_yds",
        "rush_td",
        "rush_long",
        "rec",
        "rec_yds",
        "rec_td",
        "rec_long",
    }
)

# Plain text columns (no link extraction needed).
_TEXT_COLS = frozenset(
    {
        "pos",
        "year_id",
    }
)


class CupsOfCoffeeParser:
    """Parses the PFR 'Cups of Coffee' page."""

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title from ``<h2>`` inside ``#content``."""
        content = soup.find("div", id="content")
        if content:
            h2 = content.find("h2")
            if h2:
                return h2.get_text(strip=True)
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.get_text(strip=True)
        return ""

    @staticmethod
    def _extract_link(cell: Tag) -> Optional[str]:
        """Extract the href from the first ``<a>`` in a cell."""
        link = cell.find("a")
        if link and link.get("href"):
            return link["href"]
        return None

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the coffee stats table."""
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
            player_href: Optional[str] = self._extract_link(player_cell)
            player_id: Optional[str] = player_cell.get("data-append-csv") or None

            entry: Dict[str, Any] = {
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
            }

            # Plain text columns
            for col in _TEXT_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                else:
                    raw = cell.get_text(strip=True)
                    entry[col] = raw if raw else None

            # Integer columns
            for col in _INT_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                    continue
                raw = cell.get_text(strip=True)
                if not raw:
                    entry[col] = None
                else:
                    entry[col] = safe_int(raw)

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the cups of coffee page.

        Args:
            html: Raw HTML of the PFR cups of coffee page.

        Returns:
            A dict ready for ``CupsOfCoffee.model_validate()``.

        Raises:
            ParsingError: If the coffee table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="coffee")
        if table is None:
            raise ParsingError(
                "Could not find coffee table in the HTML.",
                selector="coffee",
                html_sample=html[:500],
            )

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
