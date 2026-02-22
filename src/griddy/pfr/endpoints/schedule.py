"""Schedule endpoint for Pro Football Reference.

Provides ``get_season_schedule()`` to fetch and parse the PFR season
schedule page (``/years/{season}/games.htm``).
"""

from typing import Any, Dict, List

from ..basesdk import BaseSDK
from ..utils.browserless import fetch_page_html
from ..utils.parsers import parse_schedule_table


class Schedule(BaseSDK):
    """Sub-SDK for PFR season schedule data."""

    def get_season_schedule(self, *, season: int) -> List[Dict[str, Any]]:
        """Fetch and parse the season schedule from Pro Football Reference.

        Scrapes ``https://www.pro-football-reference.com/years/{season}/games.htm``
        using Browserless + Playwright, then parses the HTML table into
        structured game data.

        Args:
            season: The NFL season year (e.g. 2015, 2024).

        Returns:
            A list of dicts, one per game. Each dict contains fields like
            ``week_num``, ``game_date``, ``winner``, ``loser``, ``pts_win``,
            ``pts_lose``, etc.
        """
        base_url, _ = self.sdk_configuration.get_server_details()
        url = f"{base_url}/years/{season}/games.htm"
        html = fetch_page_html(url, wait_for_selector="table#games")
        return parse_schedule_table(html)
