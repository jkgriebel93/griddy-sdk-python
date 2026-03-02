"""Parser for the PFR 'Last Undefeated Team' page.

Parses ``/friv/last-undefeated.htm`` which lists the last undefeated
team(s) in every season along with their season outcomes.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_int

# Columns where we extract both text and an optional link.
_LINK_COLS = frozenset(
    {
        "first_loss",
        "playoff_result",
    }
)

# Plain text columns (no link extraction needed).
_TEXT_COLS = frozenset(
    {
        "league_id",
        "record",
        "final_record",
    }
)


class LastUndefeatedParser:
    """Parses the PFR last-undefeated-team page."""

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
        """Parse the undefeated teams table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            entry: Dict[str, Any] = {}

            # Year — row header (<th> with data-stat="year")
            # Can be empty for continuation rows (multiple teams same year).
            year_cell = row.find("th", {"data-stat": "year"})
            if year_cell:
                year_raw = year_cell.get_text(strip=True)
                entry["year"] = safe_int(year_raw) if year_raw else None
                entry["year_href"] = self._extract_link(year_cell)
            else:
                entry["year"] = None
                entry["year_href"] = None

            # Team — text + link (always present)
            team_cell = row.find(["th", "td"], {"data-stat": "team"})
            if team_cell:
                entry["team"] = team_cell.get_text(strip=True) or None
                entry["team_href"] = self._extract_link(team_cell)
            else:
                entry["team"] = None
                entry["team_href"] = None

            # Columns with text + optional link
            for col in _LINK_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                    entry[f"{col}_href"] = None
                else:
                    raw = cell.get_text(strip=True)
                    entry[col] = raw if raw else None
                    entry[f"{col}_href"] = self._extract_link(cell)

            # Plain text columns
            for col in _TEXT_COLS:
                cell = row.find(["th", "td"], {"data-stat": col})
                if cell is None:
                    entry[col] = None
                else:
                    raw = cell.get_text(strip=True)
                    entry[col] = raw if raw else None

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the last-undefeated-team page.

        Args:
            html: Raw HTML of the PFR last-undefeated-team page.

        Returns:
            A dict ready for ``LastUndefeated.model_validate()``.

        Raises:
            ValueError: If the undefeated_teams table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        table = soup.find("table", id="undefeated_teams")
        if table is None:
            raise ValueError("Could not find undefeated_teams table in the HTML.")

        entries = self._parse_table(table)

        return {
            "title": title,
            "entries": entries,
        }
