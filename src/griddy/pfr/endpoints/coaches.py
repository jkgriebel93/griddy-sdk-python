"""Coach profile endpoint for Pro Football Reference.

Provides ``get_coach_profile()`` to fetch and parse a PFR coach profile page
(``/coaches/{coach_id}.htm``) and return structured coaching data.
"""

from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import CoachProfileParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import CoachProfile


@sdk_endpoints
class Coaches(BaseSDK):
    """Sub-SDK for PFR coach profile data."""

    def _get_coach_profile_config(
        self,
        *,
        coach_id: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a coach profile page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/coaches/{coach_id}.htm``
        using the Browserless ``/chromium/unblock`` API with a residential
        proxy, then connects via Playwright CDP to extract the fully-rendered
        HTML and parse it into structured coaching data.

        Args:
            coach_id: The PFR coach identifier (e.g. ``"BeliBi0"``
                for Bill Belichick).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.CoachProfile` instance containing
            the coach's bio, coaching results, ranks, history, coaching tree,
            and challenge results.
        """
        return EndpointConfig(
            path_template="/coaches/{coach_id}.htm",
            operation_id="getCoachProfile",
            wait_for_element="#coaching_results",
            parser=CoachProfileParser().parse,
            response_type=CoachProfile,
            path_params={"coach_id": coach_id},
            timeout_ms=timeout_ms,
        )
