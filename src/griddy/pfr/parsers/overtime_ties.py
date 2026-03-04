"""Parser for the PFR 'Overtime Ties' page.

Parses ``/friv/nfl-ties.htm`` which lists all tied games since
sudden-death overtime was instituted in 1974.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._helpers import safe_int

# Columns that should be parsed as integers.
_INT_COLS = frozenset(
    {
        "points",
        "points_opp",
    }
)

# Plain text columns (no link extraction needed).
_TEXT_COLS = frozenset(
    {
        "game_date_formatted",
    }
)


class OvertimeTiesParser:
    """Parses the PFR overtime ties page."""

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
        """Parse the overtime ties table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            # Year — row header (<th> with data-stat="year")
            year_cell = row.find("th", {"data-stat": "year"})
            if not year_cell:
                continue

            year_raw = year_cell.get_text(strip=True)
            year = safe_int(year_raw)
            if year is None:
                continue

            entry: Dict[str, Any] = {
                "year": year,
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

            # Map game_date_formatted → game_date for the model
            entry["game_date"] = entry.pop("game_date_formatted", None)

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the overtime ties page.

        Args:
            html: Raw HTML of the PFR overtime ties page.

        Returns:
            A dict ready for ``OvertimeTies.model_validate()``.

        Raises:
            ParsingError: If the overtime ties table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="ot_ties")
        if table is None:
            raise ParsingError(
                "Could not find ot_ties table in the HTML.",
                selector="ot_ties",
                html_sample=html[:500],
            )

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
