"""Parser for the PFR 'Statistical Milestones' page.

Parses ``/friv/milestones.cgi`` results including the milestone watch
table (active players approaching milestone thresholds) and the top-25
career leaders table.
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from ._helpers import safe_int, uncomment_tables


class StatisticalMilestonesParser:
    """Parses the PFR statistical milestones page."""

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
    def _extract_stat(soup: BeautifulSoup) -> str:
        """Extract the stat parameter from the canonical URL or page title."""
        canonical = soup.find("link", rel="canonical")
        if canonical and canonical.get("href"):
            href = canonical["href"]
            match = re.search(r"stat=([^&]+)", href)
            if match:
                return match.group(1)
        return ""

    @staticmethod
    def _parse_milestones_table(table: Tag) -> List[Dict[str, Any]]:
        """Parse the milestones table with interleaved threshold/player rows."""
        entries: List[Dict[str, Any]] = []
        current_milestone = ""

        for row in table.find_all("tr"):
            classes = row.get("class") or []

            # Milestone threshold header row
            if "thead" in classes and "onecell" in classes:
                cell = row.find("td", {"data-stat": "onecell"})
                if cell:
                    current_milestone = cell.get_text(strip=True)
                continue

            # Player data row
            player_cell = row.find(["th", "td"], {"data-stat": "player"})
            if not player_cell:
                continue

            player_name = player_cell.get_text(strip=True)
            player_href = None
            player_id = None

            link = player_cell.find("a")
            if link and link.get("href"):
                player_href = link["href"]

            csv_id = player_cell.get("data-append-csv")
            if csv_id:
                player_id = csv_id

            value_cell = row.find(["th", "td"], {"data-stat": "value"})
            value = safe_int(value_cell.get_text(strip=True)) if value_cell else None

            needed_cell = row.find(["th", "td"], {"data-stat": "needed"})
            needed = needed_cell.get_text(strip=True) if needed_cell else None
            if needed and needed in ("", "\xa0"):
                needed = None

            entries.append(
                {
                    "milestone": current_milestone,
                    "player": player_name,
                    "player_href": player_href,
                    "player_id": player_id,
                    "value": value,
                    "needed": needed,
                }
            )

        return entries

    @staticmethod
    def _parse_leaders_table(table: Tag) -> List[Dict[str, Any]]:
        """Parse the career leaders table."""
        leaders: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return leaders

        for row in tbody.find_all("tr"):
            classes = row.get("class") or []
            # Skip the "See full leaderboard" row
            if "onecell" in classes:
                continue

            rank_cell = row.find(["th", "td"], {"data-stat": "ranker"})
            rank = safe_int(rank_cell.get_text(strip=True)) if rank_cell else None

            player_cell = row.find(["th", "td"], {"data-stat": "player"})
            if not player_cell:
                continue

            player_name = player_cell.get_text(strip=True)
            # Strip trailing * from HOF players
            player_name = player_name.rstrip("*")
            player_href = None
            player_id = None

            link = player_cell.find("a")
            if link and link.get("href"):
                player_href = link["href"]

            csv_id = player_cell.get("data-append-csv")
            if csv_id:
                player_id = csv_id

            # Active players are wrapped in <strong>
            is_active = player_cell.find("strong") is not None

            value_cell = row.find(["th", "td"], {"data-stat": "value"})
            value = safe_int(value_cell.get_text(strip=True)) if value_cell else None

            needed_cell = row.find(["th", "td"], {"data-stat": "needed"})
            needed_text = needed_cell.get_text(strip=True) if needed_cell else None
            if not needed_text or needed_text in ("\xa0",):
                needed_text = None

            leaders.append(
                {
                    "rank": rank,
                    "player": player_name,
                    "player_href": player_href,
                    "player_id": player_id,
                    "value": value,
                    "needed": needed_text,
                    "is_active": is_active,
                }
            )

        return leaders

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the statistical milestones page.

        Args:
            html: Raw HTML of the PFR milestones page.

        Returns:
            A dict ready for ``StatisticalMilestones.model_validate()``.

        Raises:
            ValueError: If the milestones table is not found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        stat = self._extract_stat(soup)

        # The milestones table is directly in the page
        milestones_table = soup.find("table", id="milestones")
        if milestones_table is None:
            raise ValueError("Could not find milestones table in the HTML.")

        milestones = self._parse_milestones_table(milestones_table)

        # The leaders table is wrapped in an HTML comment
        uncomment_tables(soup)
        leaders_table = soup.find("table", id="leaders")
        career_leaders = (
            self._parse_leaders_table(leaders_table) if leaders_table else []
        )

        return {
            "title": title,
            "stat": stat,
            "milestones": milestones,
            "career_leaders": career_leaders,
        }
