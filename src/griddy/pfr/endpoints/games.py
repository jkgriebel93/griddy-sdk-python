"""Game details endpoint for Pro Football Reference.

Provides ``get_game_details()`` to fetch and parse a PFR boxscore page
(``/boxscores/{game_id}.htm``) and return all game-specific data as JSON.
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import GameDetailsParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import GameDetails


@sdk_endpoints
class Games(BaseSDK):
    """Sub-SDK for PFR boxscore / game detail data."""

    @cached_property
    def _parser(self) -> GameDetailsParser:
        return GameDetailsParser()

    def _get_game_details_config(
        self,
        *,
        game_id: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a boxscore page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/boxscores/{game_id}.htm``
        using Browserless + Playwright, then parses the HTML into a
        comprehensive dict of game data.

        Args:
            game_id: The PFR game identifier (e.g. ``"201509100nwe"``).
                This is the filename portion of the boxscore URL.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.GameDetails` instance containing
            all extracted game data (scorebox, linescore, scoring plays,
            team stats, player stats, drives, etc.).
        """
        return EndpointConfig(
            path_template="/boxscores/{game_id}.htm",
            operation_id="getGameDetails",
            wait_for_element="#scoring",
            parser=self._parser.parse,
            response_type=GameDetails,
            path_params={"game_id": game_id},
            timeout_ms=timeout_ms,
        )
