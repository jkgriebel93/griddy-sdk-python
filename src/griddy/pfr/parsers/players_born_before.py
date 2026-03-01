"""Parser for the PFR Active Players Born Before a Date page.

Page (``/friv/age.cgi?month=...&day=...&year=...``):
    Parses the player table with career stats for active players born on or
    before the specified date.
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_int


class PlayersBornBeforeParser:
    """Parses the PFR active players born before a date page."""

    # Integer stat columns to extract from each player row.
    _STAT_COLUMNS: List[str] = [
        "age",
        "year_min",
        "year_max",
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
    ]

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title from h1 inside #content."""
        content = soup.find("div", id="content")
        if content:
            h1 = content.find("h1")
            if h1:
                return h1.get_text(strip=True)
        return ""

    @staticmethod
    def _extract_month_day_year(title: str) -> tuple[int, int, int]:
        """Extract month, day, and year from a title like
        'Active Players Born on or before August 5, 1993'.

        Returns:
            A ``(month, day, year)`` tuple. Values are 0 when not found.
        """
        month_names = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
        }
        match = re.search(
            r"(?P<month>"
            + "|".join(month_names.keys())
            + r")\s+(?P<day>\d{1,2}),\s+(?P<year>\d{4})",
            title,
        )
        if match:
            return (
                month_names[match.group("month")],
                int(match.group("day")),
                int(match.group("year")),
            )
        return 0, 0, 0

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the players table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            if "thead" in classes or "over_header" in classes:
                continue

            # Rank
            rank_cell = row.find(["th", "td"], {"data-stat": "ranker"})
            if not rank_cell:
                continue
            rank = safe_int(rank_cell.get_text(strip=True))
            if rank is None:
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

            # Birth date (formatted string)
            birth_date_cell = row.find(
                ["th", "td"], {"data-stat": "birth_date_formatted"}
            )
            birth_date = (
                birth_date_cell.get_text(strip=True) if birth_date_cell else None
            )
            if not birth_date:
                birth_date = None

            # Position
            pos_cell = row.find(["th", "td"], {"data-stat": "pos"})
            pos = pos_cell.get_text(strip=True) if pos_cell else None
            if not pos:
                pos = None

            entry: Dict[str, Any] = {
                "rank": rank,
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "birth_date": birth_date,
                "pos": pos,
            }

            # Integer stat columns
            for col in self._STAT_COLUMNS:
                cell = row.find(["th", "td"], {"data-stat": col})
                entry[col] = safe_int(cell.get_text(strip=True)) if cell else None

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the active players born before a date page.

        Args:
            html: Raw HTML of the PFR active players born before page.

        Returns:
            A dict ready for ``PlayersBornBefore.model_validate()``.

        Raises:
            ValueError: If the players table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        month, day, year = self._extract_month_day_year(title)

        table = soup.find("table", id="players")
        if table is None:
            raise ValueError("Could not find players table in the HTML.")

        players = self._parse_table(table)

        return {
            "title": title,
            "month": month,
            "day": day,
            "year": year,
            "players": players,
        }
