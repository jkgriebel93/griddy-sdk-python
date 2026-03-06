"""Super Bowl endpoint for Pro Football Reference.

Provides ``history()``, ``leaders()``, and ``standings()`` to fetch and parse
PFR Super Bowl pages.
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers.superbowl import SuperBowlParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import SuperBowlHistory, SuperBowlLeaders, SuperBowlStandings


@sdk_endpoints
class SuperBowl(BaseSDK):
    """Sub-SDK for PFR Super Bowl pages."""

    @cached_property
    def _parser(self) -> SuperBowlParser:
        """Lazily instantiate and cache the Super Bowl HTML parser."""
        return SuperBowlParser()

    def _history_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the Super Bowl history page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/super-bowl/``
        and returns structured data for every Super Bowl game.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.SuperBowlHistory` instance containing
            all Super Bowl game entries.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/super-bowl/",
            operation_id="getSuperBowlHistory",
            wait_for_element="#super_bowls",
            parser=lambda html: parser.parse_history(html),
            response_type=SuperBowlHistory,
            path_params={},
            timeout_ms=timeout_ms,
        )

    def _leaders_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the Super Bowl leaders page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/super-bowl/leaders.htm``
        and returns career and single-game statistical leaderboards.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.SuperBowlLeaders` instance containing
            all leaderboard tables.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/super-bowl/leaders.htm",
            operation_id="getSuperBowlLeaders",
            wait_for_element="table",
            parser=lambda html: parser.parse_leaders(html),
            response_type=SuperBowlLeaders,
            path_params={},
            timeout_ms=timeout_ms,
        )

    def _standings_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the Super Bowl standings page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/super-bowl/standings.htm``
        and returns franchise Super Bowl standings with win/loss records.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.SuperBowlStandings` instance
            containing all franchise standings entries.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/super-bowl/standings.htm",
            operation_id="getSuperBowlStandings",
            wait_for_element="#standings",
            parser=lambda html: parser.parse_standings(html),
            response_type=SuperBowlStandings,
            path_params={},
            timeout_ms=timeout_ms,
        )
