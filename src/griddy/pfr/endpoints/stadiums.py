"""Stadium endpoint for Pro Football Reference.

Provides ``get_stadium()`` to fetch and parse a PFR stadium page
(``/stadiums/{stadium_id}.htm``) and return structured stadium data.
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import StadiumParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import StadiumProfile


@sdk_endpoints
class Stadiums(BaseSDK):
    """Sub-SDK for PFR stadium data."""

    @cached_property
    def _parser(self) -> StadiumParser:
        """Lazily instantiate and cache the stadium HTML parser."""
        return StadiumParser()

    def _get_stadium_config(
        self,
        *,
        stadium_id: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a stadium page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/stadiums/{stadium_id}.htm``
        using the Browserless ``/chromium/unblock`` API with a residential
        proxy, then connects via Playwright CDP to extract the fully-rendered
        HTML and parse it into structured stadium data.

        Args:
            stadium_id: The PFR stadium identifier (e.g. ``"BOS00"``
                for Gillette Stadium).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.StadiumProfile` instance containing
            the stadium's bio, career leaders, best games, and notable game
            summaries.
        """
        return EndpointConfig(
            path_template="/stadiums/{stadium_id}.htm",
            operation_id="getStadium",
            wait_for_element="#leaders",
            parser=self._parser.parse,
            response_type=StadiumProfile,
            path_params={"stadium_id": stadium_id},
            timeout_ms=timeout_ms,
        )
