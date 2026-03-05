"""Schedule endpoint for Pro Football Reference.

Provides ``get_season_schedule()`` to fetch and parse the PFR season
schedule page (``/years/{season}/games.htm``).
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import ScheduleParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models.entities.schedule_game import ScheduleGame


@sdk_endpoints
class Schedule(BaseSDK):
    """Sub-SDK for PFR season schedule data."""

    @cached_property
    def _parser(self) -> ScheduleParser:
        return ScheduleParser()

    def _get_season_schedule_config(
        self,
        *,
        season: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the season schedule from Pro Football Reference.

        Scrapes ``https://www.pro-football-reference.com/years/{season}/games.htm``
        using Browserless + Playwright, then parses the HTML table into
        structured game data.

        Args:
            season: The NFL season year (e.g. 2015, 2024).
            timeout_ms: Optional timeout in milliseconds for the page selector.

        Returns:
            A list of ``ScheduleGame`` models, one per game.
        """
        return EndpointConfig(
            path_template="/years/{season}/games.htm",
            operation_id="getSeasonSchedule",
            wait_for_element="#games",
            parser=self._parser.parse,
            response_type=ScheduleGame,
            path_params={"season": season},
            timeout_ms=timeout_ms,
        )
