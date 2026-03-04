"""Parser for the PFR 'Octopus Tracker' page.

Parses ``/friv/octopus-tracker.htm`` including the table listing
game-level instances of a player scoring both the TD and the two-point
conversion on a single possession (since 1994).
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._helpers import safe_int

# Columns that should be parsed as integers.
_INT_COLS = frozenset(
    {
        "week_num",
        "margin",
    }
)

# Plain text columns (no link extraction needed).
_TEXT_COLS = frozenset(
    {
        "game_day_of_week",
        "game_date",
        "game_outcome",
        "score_type",
        "xpa_type",
    }
)


class OctopusTrackerParser:
    """Parses the PFR octopus tracker page."""

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
        """Parse the octopus stats table."""
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

            # Team — text + link
            team_cell = row.find(["th", "td"], {"data-stat": "team"})
            if team_cell:
                entry["team"] = team_cell.get_text(strip=True)
                entry["team_href"] = self._extract_link(team_cell)
            else:
                entry["team"] = None
                entry["team_href"] = None

            # Opponent — text + link
            opp_cell = row.find(["th", "td"], {"data-stat": "opp"})
            if opp_cell:
                entry["opp"] = opp_cell.get_text(strip=True)
                entry["opp_href"] = self._extract_link(opp_cell)
            else:
                entry["opp"] = None
                entry["opp_href"] = None

            # Boxscore — link only
            box_cell = row.find(["th", "td"], {"data-stat": "boxscore_word"})
            if box_cell:
                entry["boxscore_href"] = self._extract_link(box_cell)
            else:
                entry["boxscore_href"] = None

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
        """Parse the octopus tracker page.

        Args:
            html: Raw HTML of the PFR octopus tracker page.

        Returns:
            A dict ready for ``OctopusTracker.model_validate()``.

        Raises:
            ParsingError: If the octopus table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="octopus")
        if table is None:
            raise ParsingError(
                "Could not find octopus table in the HTML.",
                selector="octopus",
                html_sample=html[:500],
            )

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
