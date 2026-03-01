"""Parser for the PFR 'Non-Skill Position TD Scorers' page.

Parses ``/friv/odd_td.htm`` including the table listing game-level
instances of non-skill position players scoring an offensive touchdown.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_float, safe_int

# Columns that should be parsed as integers.
_INT_COLS = frozenset(
    {
        "week_num",
        "pts_off",
        "pts_def",
        "rush_att",
        "rush_yds",
        "rush_long",
        "rush_td",
        "rec",
        "rec_yds",
        "rec_long",
        "rec_td",
    }
)

# Columns that should be parsed as floats.
_FLOAT_COLS = frozenset(
    {
        "rush_yds_per_att",
        "rec_yds_per_rec",
    }
)

# Plain text columns (no link extraction needed).
_TEXT_COLS = frozenset(
    {
        "game_day_of_week",
        "game_date",
        "game_outcome",
        "game_location",
    }
)


class NonSkillPosTdParser:
    """Parses the PFR non-skill position TD scorers page."""

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
        """Parse the odd_scorers stats table."""
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

            # Position (plain text)
            pos_cell = row.find(["th", "td"], {"data-stat": "pos"})
            pos = pos_cell.get_text(strip=True) if pos_cell else ""

            entry: Dict[str, Any] = {
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "pos": pos,
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

            # Numeric columns
            for col in _INT_COLS | _FLOAT_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                    continue
                raw = cell.get_text(strip=True)
                if not raw:
                    entry[col] = None
                elif col in _INT_COLS:
                    entry[col] = safe_int(raw)
                else:
                    entry[col] = safe_float(raw)

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the non-skill position TD scorers page.

        Args:
            html: Raw HTML of the PFR odd TD scorers page.

        Returns:
            A dict ready for ``NonSkillPosTdScorers.model_validate()``.

        Raises:
            ValueError: If the odd_scorers table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="odd_scorers")
        if table is None:
            raise ValueError("Could not find odd_scorers table in the HTML.")

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
