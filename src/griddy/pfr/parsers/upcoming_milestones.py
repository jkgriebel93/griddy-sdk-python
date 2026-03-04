"""Parser for the PFR 'Upcoming Milestones' page.

Parses ``/friv/upcoming-milestones.htm`` including the milestones table
(players who may hit a round-number milestone in their next game) and the
leaderboards table (players who may move up the career leaderboard).
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError


class UpcomingMilestonesParser:
    """Parses the PFR upcoming milestones page."""

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
    def _extract_description(soup: BeautifulSoup) -> str:
        """Extract the description paragraph from the page."""
        content = soup.find("div", id="content")
        if content:
            p = content.find("p")
            if p:
                return p.get_text(strip=True)
        return ""

    @staticmethod
    def _extract_player_id(href: str) -> Optional[str]:
        """Extract player ID from a PFR player href like /players/M/McCaCh01.htm."""
        match = re.search(r"/players/[A-Z]/([A-Za-z0-9]+)\.htm", href)
        return match.group(1) if match else None

    @staticmethod
    def _parse_value(text: str) -> Optional[int]:
        """Parse an integer value, stripping commas."""
        cleaned = text.replace(",", "").strip()
        try:
            return int(cleaned)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _parse_table(
        table: Tag, *, extract_leader_href: bool = False
    ) -> List[Dict[str, Any]]:
        """Parse a milestones/leaderboards table with interleaved category headers.

        Args:
            table: The BeautifulSoup Tag for the table.
            extract_leader_href: If True, extract the href from the
                ``val_to_milestone`` cell (used for the leaderboards table).
        """
        entries: List[Dict[str, Any]] = []
        current_category = ""

        tbody = table.find("tbody")
        if tbody is None:
            return entries

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []

            # Category header row
            if "thead" in classes:
                cell = row.find(["th", "td"], {"data-stat": "name_display"})
                if cell and cell.get("colspan"):
                    current_category = cell.get_text(strip=True)
                continue

            # Player data row
            name_cell = row.find(["th", "td"], {"data-stat": "name_display"})
            if not name_cell:
                continue

            player_name = name_cell.get_text(strip=True)
            player_href = None
            player_id = None

            link = name_cell.find("a")
            if link and link.get("href"):
                player_href = link["href"]
                player_id = UpcomingMilestonesParser._extract_player_id(player_href)

            value_cell = row.find(["th", "td"], {"data-stat": "value"})
            value = (
                UpcomingMilestonesParser._parse_value(value_cell.get_text(strip=True))
                if value_cell
                else None
            )

            needed_cell = row.find(["th", "td"], {"data-stat": "val_to_milestone"})
            needed = needed_cell.get_text(strip=True) if needed_cell else None
            if not needed:
                needed = None

            entry: Dict[str, Any] = {
                "category": current_category,
                "player": player_name,
                "player_href": player_href,
                "player_id": player_id,
                "value": value,
                "needed": needed,
            }

            if extract_leader_href:
                leader_link = needed_cell.find("a") if needed_cell else None
                entry["leader_href"] = (
                    leader_link["href"]
                    if leader_link and leader_link.get("href")
                    else None
                )

            entries.append(entry)

        return entries

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the upcoming milestones page.

        Args:
            html: Raw HTML of the PFR upcoming milestones page.

        Returns:
            A dict ready for ``UpcomingMilestones.model_validate()``.

        Raises:
            ParsingError: If the milestones table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        description = self._extract_description(soup)

        milestones_table = soup.find("table", id="upcoming_milestones")
        if milestones_table is None:
            raise ParsingError(
                "Could not find upcoming milestones table in the HTML.",
                selector="upcoming_milestones",
                html_sample=html[:500],
            )

        milestones = self._parse_table(milestones_table)

        leaderboards_table = soup.find("table", id="upcoming_leaderboards")
        leaderboards = (
            self._parse_table(leaderboards_table, extract_leader_href=True)
            if leaderboards_table
            else []
        )

        return {
            "title": title,
            "description": description,
            "milestones": milestones,
            "leaderboards": leaderboards,
        }
