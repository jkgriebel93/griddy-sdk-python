"""Leaders endpoints for Pro Football Reference.

Provides ``get()`` to fetch and parse PFR career, single-season, and
single-game statistical leaderboard pages.
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import LeadersParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import Leaderboard


@sdk_endpoints
class Leaders(BaseSDK):
    """Sub-SDK for PFR statistical leaders pages."""

    @cached_property
    def _parser(self) -> LeadersParser:
        return LeadersParser()

    def _get_config(
        self,
        *,
        stat: str,
        scope: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a leaders page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/leaders/{stat}_{scope}.htm``
        and returns a structured leaderboard with player entries.

        Args:
            stat: Stat category slug (e.g. ``"pass_yds"``, ``"rush_td"``,
                ``"sacks"``, ``"def_int"``).
            scope: Leaderboard scope (e.g. ``"career"``,
                ``"single_season"``).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.Leaderboard` instance.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/leaders/{stat}_{scope}.htm",
            operation_id="getLeaders",
            wait_for_element="table.stats_table",
            parser=lambda html: parser.parse(html, stat=stat, scope=scope),
            response_type=Leaderboard,
            path_params={"stat": stat, "scope": scope},
            timeout_ms=timeout_ms,
        )
