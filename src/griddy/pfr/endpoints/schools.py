"""Schools endpoint for Pro Football Reference.

Provides ``list()`` and ``high_schools()`` to fetch and parse PFR school pages.
"""

from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers.schools import SchoolsParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import CollegeList, HighSchoolList

_parser = SchoolsParser()


@sdk_endpoints
class Schools(BaseSDK):
    """Sub-SDK for PFR Schools & Colleges pages."""

    def _list_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the All Player Colleges page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/schools/``
        and returns structured data for every college/university.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.CollegeList` instance containing
            all college entries.
        """
        return EndpointConfig(
            path_template="/schools/",
            operation_id="getCollegeList",
            wait_for_element="#college_stats_table",
            parser=lambda html: _parser.parse_colleges(html),
            response_type=CollegeList,
            path_params={},
            timeout_ms=timeout_ms,
        )

    def _high_schools_config(
        self,
        *,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse the High Schools page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/schools/high_schools.cgi``
        and returns structured data for the top high schools by NFL player count.

        Args:
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.HighSchoolList` instance containing
            all high school entries.
        """
        return EndpointConfig(
            path_template="/schools/high_schools.cgi",
            operation_id="getHighSchoolList",
            wait_for_element="#high_schools",
            parser=lambda html: _parser.parse_high_schools(html),
            response_type=HighSchoolList,
            path_params={},
            timeout_ms=timeout_ms,
        )
