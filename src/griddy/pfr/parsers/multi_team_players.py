"""Parser for the PFR 'Players Who Played for Multiple Teams' page.

Parses ``/friv/players-who-played-for-multiple-teams-franchises.fcgi``
results including the top-player summaries, passing/rushing/receiving
stat tables, and the all-players table.
"""

import re
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup, Tag

from griddy.pfr.errors import ParsingError

from ._helpers import safe_numeric


class MultiTeamPlayersParser:
    """Parses the PFR multi-franchise players results page."""

    # Table IDs follow the pattern multifranchise_stats_N
    # 0 = Passing, 1 = Rushing, 2 = Receiving, 3 = All Players
    _TABLE_ID_PREFIX = "multifranchise_stats_"

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract the page title (e.g. 'Players who played for ...')."""
        title_tag = soup.find("title")
        if title_tag:
            text = title_tag.get_text(strip=True)
            # Strip the "| Pro-Football-Reference.com" suffix
            return text.split("|")[0].strip()
        return ""

    @staticmethod
    def _extract_total_players(soup: BeautifulSoup) -> Optional[int]:
        """Extract the total player count from the intro paragraph."""
        content = soup.find("div", id="content")
        if not content:
            return None

        for p_tag in content.find_all("p", recursive=False):
            text = p_tag.get_text()
            match = re.search(r"There were (\d+) players", text)
            if match:
                return int(match.group(1))

        # Also check nested paragraphs
        for p_tag in content.find_all("p"):
            text = p_tag.get_text()
            match = re.search(r"There were (\d+) players", text)
            if match:
                return int(match.group(1))

        return None

    @staticmethod
    def _extract_teams(soup: BeautifulSoup) -> List[str]:
        """Extract team names from the over_header row of the first table."""
        teams: List[str] = []
        table = soup.find("table", id="multifranchise_stats_0")
        if table is None:
            table = soup.find("table", id="multifranchise_stats_3")
        if table is None:
            return teams

        over_header = table.find("tr", class_="over_header")
        if over_header:
            for th in over_header.find_all("th"):
                text = th.get_text(strip=True)
                if text:
                    teams.append(text)
        return teams

    @staticmethod
    def _extract_top_players(soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extract the top 5 player summaries from h3/p pairs."""
        top_players: List[Dict[str, Any]] = []
        content = soup.find("div", id="content")
        if not content:
            return top_players

        # Find h3 tags that represent top player names
        for h3 in content.find_all("h3"):
            name = h3.get_text(strip=True)
            # Skip non-player h3 tags
            if not name or "Immaculate Grid" in name:
                continue

            # The description is in the next <p> sibling
            p_tag = h3.find_next_sibling("p")
            if p_tag is None:
                continue

            description = p_tag.get_text(strip=True)
            player_href = None
            player_id = None

            link = p_tag.find("a")
            if link and link.get("href"):
                player_href = link["href"]
                # Extract player ID from href like /players/C/CampCa99.htm
                href_match = re.search(
                    r"/players/[A-Z]/([A-Za-z0-9]+)\.htm", player_href
                )
                if href_match:
                    player_id = href_match.group(1)

            top_players.append(
                {
                    "name": name,
                    "player_href": player_href,
                    "player_id": player_id,
                    "description": description,
                }
            )

        return top_players

    @staticmethod
    def _extract_table_category(soup: BeautifulSoup, table_id: str) -> str:
        """Extract the category label (e.g. 'Passing') for a table."""
        wrapper = soup.find("div", id=f"all_{table_id}")
        if wrapper:
            heading = wrapper.find("h2")
            if heading:
                return heading.get_text(strip=True)
        return ""

    @staticmethod
    def _parse_table(table: Tag) -> List[Dict[str, Any]]:
        """Parse a single stats table into a list of player dicts."""
        players: List[Dict[str, Any]] = []

        tbody = table.find("tbody")
        if tbody is None:
            return players

        for row in tbody.find_all("tr"):
            if "thead" in (row.get("class") or []):
                continue

            player_name = ""
            player_href = None
            player_id = None
            stats: Dict[str, Any] = {}

            for cell in row.find_all(["th", "td"]):
                stat = cell.get("data-stat")
                if not stat:
                    continue

                text = cell.get_text(strip=True)

                if stat == "player":
                    player_name = text
                    link = cell.find("a")
                    if link and link.get("href"):
                        player_href = link["href"]
                    csv_id = cell.get("data-append-csv")
                    if csv_id:
                        player_id = csv_id
                else:
                    stats[stat] = safe_numeric(text)

            if player_name:
                players.append(
                    {
                        "player": player_name,
                        "player_href": player_href,
                        "player_id": player_id,
                        "stats": stats,
                    }
                )

        return players

    def parse(self, html: str) -> Dict[str, Any]:
        """Parse the multi-team players results page.

        Args:
            html: Raw HTML of the PFR multi-franchise players results page.

        Returns:
            A dict ready for ``MultiTeamPlayers.model_validate()``.

        Raises:
            ParsingError: If no stats tables are found.
        """
        soup = BeautifulSoup(html, "html.parser")

        title = self._extract_title(soup)
        total_players = self._extract_total_players(soup)
        teams = self._extract_teams(soup)
        top_players = self._extract_top_players(soup)

        stats_tables: List[Dict[str, Any]] = []
        idx = 0
        while True:
            table_id = f"{self._TABLE_ID_PREFIX}{idx}"
            table = soup.find("table", id=table_id)
            if table is None:
                break

            category = self._extract_table_category(soup, table_id)
            players = self._parse_table(table)

            stats_tables.append(
                {
                    "category": category,
                    "teams": teams,
                    "players": players,
                }
            )
            idx += 1

        if not stats_tables:
            raise ParsingError(
                "Could not find any multifranchise_stats tables in the HTML.",
                selector="multi_team_stats",
                html_sample=html[:500],
            )

        return {
            "title": title,
            "total_players": total_players,
            "teams": teams,
            "top_players": top_players,
            "stats_tables": stats_tables,
        }
