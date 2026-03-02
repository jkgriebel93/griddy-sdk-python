"""Parser for the PFR 'Standings on Any Date' page.

Parses ``/boxscores/standings.cgi`` which lists NFL standings as of a
specified date or week, broken out by conference and division.
"""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_float, safe_int

# Table IDs corresponding to each conference.
_CONFERENCE_TABLES = ("AFC", "NFC")

# Columns parsed as integers.
_INT_COLS: List[tuple[str, str]] = [
    ("wins", "wins"),
    ("losses", "losses"),
    ("ties", "ties"),
    ("points", "points_for"),
    ("points_opp", "points_against"),
    ("points_diff", "points_diff"),
]

# Columns parsed as floats.
_FLOAT_COLS: List[tuple[str, str]] = [
    ("win_loss_perc", "win_loss_perc"),
    ("mov", "margin_of_victory"),
]


class StandingsOnDateParser:
    """Parses the PFR standings-on-date page."""

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title from ``<h1>`` inside ``#content``."""
        content = soup.find("div", id="content")
        if content:
            h1 = content.find("h1")
            if h1:
                return h1.get_text(strip=True)
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

    def _parse_table(self, table: Tag, conference: str) -> List[Dict[str, Any]]:
        """Parse a single conference standings table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        division: Optional[str] = None

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []

            # Division header rows (class "thead onecell").
            if "thead" in classes:
                onecell = row.find("td", {"data-stat": "onecell"})
                if onecell:
                    division = onecell.get_text(strip=True)
                continue

            entry: Dict[str, Any] = {}
            entry["conference"] = conference
            entry["division"] = division

            # Team cell — <th> with data-stat="team", contains <a> + optional marker.
            team_cell = row.find("th", {"data-stat": "team"})
            if team_cell:
                link = team_cell.find("a")
                if link:
                    entry["team"] = link.get_text(strip=True)
                    entry["team_href"] = link.get("href")
                    # Playoff marker is text after the </a> tag (* or +).
                    full_text = team_cell.get_text(strip=True)
                    team_name = link.get_text(strip=True)
                    marker = full_text[len(team_name) :]
                    entry["playoff_marker"] = marker if marker else None
                else:
                    entry["team"] = team_cell.get_text(strip=True) or None
                    entry["team_href"] = None
                    entry["playoff_marker"] = None
            else:
                entry["team"] = None
                entry["team_href"] = None
                entry["playoff_marker"] = None

            # Integer columns.
            for data_stat, key in _INT_COLS:
                cell = row.find("td", {"data-stat": data_stat})
                if cell is not None:
                    entry[key] = safe_int(cell.get_text(strip=True))
                else:
                    entry[key] = None

            # Float columns.
            for data_stat, key in _FLOAT_COLS:
                cell = row.find("td", {"data-stat": data_stat})
                if cell is not None:
                    raw = cell.get_text(strip=True)
                    entry[key] = safe_float(raw) if raw else None
                else:
                    entry[key] = None

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the standings-on-date page.

        Args:
            html: Raw HTML of the PFR standings page.

        Returns:
            A dict ready for ``StandingsOnDate.model_validate()``.

        Raises:
            ValueError: If no conference standings tables are found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)

        teams: List[Dict[str, Any]] = []
        for table_id in _CONFERENCE_TABLES:
            table = soup.find("table", id=table_id)
            if table:
                teams.extend(self._parse_table(table, table_id))

        if not teams:
            raise ValueError("Could not find AFC or NFC standings tables in the HTML.")

        return {
            "title": title,
            "teams": teams,
        }
