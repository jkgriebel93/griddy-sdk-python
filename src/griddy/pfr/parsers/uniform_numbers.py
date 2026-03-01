"""Parser for the PFR 'Players By Uniform Number' page.

Parses ``/players/uniform.cgi?number=N&team=TEAM`` including the player
table listing all players who wore the specified uniform number.
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_int


class UniformNumbersParser:
    """Parses the PFR uniform numbers page."""

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
    def _extract_number(title: str) -> int:
        """Extract the uniform number from the title.

        Example titles:
        - ``'All Players To Wear Number 6 For Pittsburgh Steelers'``
        - ``'All Players To Wear Number 12'``
        """
        match = re.search(r"Number\s+(\d+)", title)
        if match:
            return int(match.group(1))
        return 0

    @staticmethod
    def _extract_team(title: str) -> Optional[str]:
        """Extract the team name from the title, if present.

        Returns ``None`` when no team filter was applied.
        """
        match = re.search(r"For\s+(.+)$", title)
        if match:
            return match.group(1).strip()
        return None

    def _parse_table(self, table: Tag) -> List[Dict[str, Any]]:
        """Parse the uniform numbers stats table."""
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

            # Integer stat columns
            year_min_cell = row.find(["th", "td"], {"data-stat": "year_min"})
            year_max_cell = row.find(["th", "td"], {"data-stat": "year_max"})
            av_cell = row.find(["th", "td"], {"data-stat": "av"})

            entry: Dict[str, Any] = {
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "year_min": (
                    safe_int(year_min_cell.get_text(strip=True))
                    if year_min_cell
                    else None
                ),
                "year_max": (
                    safe_int(year_max_cell.get_text(strip=True))
                    if year_max_cell
                    else None
                ),
                "av": (safe_int(av_cell.get_text(strip=True)) if av_cell else None),
            }

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the uniform numbers page.

        Args:
            html: Raw HTML of the PFR uniform numbers page.

        Returns:
            A dict ready for ``UniformNumbers.model_validate()``.

        Raises:
            ValueError: If the uniform_number table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        number = self._extract_number(title)
        team = self._extract_team(title)

        table = soup.find("table", id="uniform_number")
        if table is None:
            raise ValueError("Could not find uniform_number table in the HTML.")

        players = self._parse_table(table)

        return {
            "title": title,
            "number": number,
            "team": team,
            "players": players,
        }
