"""Hall of Fame endpoint for Pro Football Reference.

Provides ``list()`` to fetch and parse the PFR Hall of Fame page.
"""

from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import AwardsParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import HallOfFame

_parser = AwardsParser()


@sdk_endpoints
class Hof(BaseSDK):
    """Sub-SDK for the PFR Hall of Fame page."""

    def _list_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the Hall of Fame page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/hof/``
        and returns structured data for all Hall of Fame inductees.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.HallOfFame` instance containing
            all Hall of Fame player entries.
        """
        return EndpointConfig(
            path_template="/hof/",
            operation_id="getHof",
            wait_for_element="#hof_players",
            parser=lambda html: _parser.parse_hof(html),
            response_type=HallOfFame,
            path_params={},
            timeout_ms=timeout_ms,
            validate_model=True,
        )
