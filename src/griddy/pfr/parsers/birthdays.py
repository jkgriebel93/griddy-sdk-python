"""Parser for the PFR 'Players Born Today' (Birthdays) page.

Parses ``/friv/birthdays.cgi?month=M&day=D`` including the player table
with career stats (passing, rushing, receiving).
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_int


class BirthdaysParser:
    """Parses the PFR birthdays page."""

    # Stat columns to extract as integers from each player row.
    _STAT_COLUMNS: List[str] = [
        "birth_year",
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
    def _extract_month_day(title: str) -> tuple[int, int]:
        """Extract month and day from a title like
        'List of all NFL Players Born on March 2'.
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
            r"(?P<month>" + "|".join(month_names.keys()) + r")\s+(?P<day>\d{1,2})",
            title,
        )
        if match:
            return month_names[match.group("month")], int(match.group("day"))
        return 0, 0

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the birthdays stats table."""
        entries: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            # Skip spacer / over-header rows
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
                "pos": pos,
            }

            # Integer stat columns
            for col in self._STAT_COLUMNS:
                cell = row.find(["th", "td"], {"data-stat": col})
                entry[col] = safe_int(cell.get_text(strip=True)) if cell else None

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the birthdays page.

        Args:
            html: Raw HTML of the PFR birthdays page.

        Returns:
            A dict ready for ``Birthdays.model_validate()``.

        Raises:
            ValueError: If the birthdays table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        month, day = self._extract_month_day(title)

        table = soup.find("table", id="birthdays")
        if table is None:
            raise ValueError("Could not find birthdays table in the HTML.")

        players = self._parse_table(table)

        return {
            "title": title,
            "month": month,
            "day": day,
            "players": players,
        }
