"""Awards endpoint for Pro Football Reference.

Provides ``get()`` to fetch and parse PFR award history pages.
"""

from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import AwardsParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import AwardHistory

_parser = AwardsParser()


@sdk_endpoints
class Awards(BaseSDK):
    """Sub-SDK for PFR award history pages."""

    def _get_config(
        self,
        *,
        award: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse an award history page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/awards/{award}.htm``
        and returns structured award winner data.

        Args:
            award: The PFR award slug (e.g. ``"ap-nfl-mvp-award"``).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.AwardHistory` instance containing
            all winners for the given award.
        """
        return EndpointConfig(
            path_template="/awards/{award}.htm",
            operation_id="getAward",
            wait_for_element="#awards",
            parser=lambda html: _parser.parse_award(html, award=award),
            response_type=AwardHistory,
            path_params={"award": award},
            timeout_ms=timeout_ms,
            validate_model=True,
        )
