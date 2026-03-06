"""Draft endpoints for Pro Football Reference.

Provides ``get_year_draft()``, ``get_combine()``, and ``get_team_draft()``
to fetch and parse PFR draft-related pages.
"""

from functools import cached_property
from typing import Optional

from griddy.core.decorators import sdk_endpoints
from griddy.pfr.parsers import DraftParser

from ..basesdk import BaseSDK, EndpointConfig
from ..models import CombineResults, TeamDraft, YearDraft


@sdk_endpoints
class Draft(BaseSDK):
    """Sub-SDK for PFR NFL Draft pages."""

    @cached_property
    def _parser(self) -> DraftParser:
        """Lazily instantiate and cache the draft HTML parser."""
        return DraftParser()

    # ------------------------------------------------------------------
    # Year Draft — /years/{year}/draft.htm
    # ------------------------------------------------------------------

    def _get_year_draft_config(
        self,
        *,
        year: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a draft year page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/years/{year}/draft.htm``
        and returns structured draft pick data including career stats.

        Args:
            year: The draft year (e.g. ``2024``).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.YearDraft` instance containing
            all draft picks for the given year.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/years/{year}/draft.htm",
            operation_id="getYearDraft",
            wait_for_element="#drafts",
            parser=lambda html: parser.parse_year_draft(html, year=year),
            response_type=YearDraft,
            path_params={"year": year},
            timeout_ms=timeout_ms,
        )

    # ------------------------------------------------------------------
    # Combine — /draft/{year}-combine.htm
    # ------------------------------------------------------------------

    def _get_combine_config(
        self,
        *,
        year: int,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a combine page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/draft/{year}-combine.htm``
        and returns structured combine measurement data.

        Args:
            year: The combine year (e.g. ``2024``).
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.CombineResults` instance
            containing all combine entries for the given year.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/draft/{year}-combine.htm",
            operation_id="getCombine",
            wait_for_element="#combine",
            parser=lambda html: parser.parse_combine(html, year=year),
            response_type=CombineResults,
            path_params={"year": year},
            timeout_ms=timeout_ms,
        )

    # ------------------------------------------------------------------
    # Team Draft — /teams/{team}/draft.htm
    # ------------------------------------------------------------------

    def _get_team_draft_config(
        self,
        *,
        team: str,
        timeout_ms: Optional[int] = None,
    ) -> EndpointConfig:
        r"""Fetch and parse a team draft history page from Pro Football Reference.

        Scrapes
        ``https://www.pro-football-reference.com/teams/{team}/draft.htm``
        and returns structured draft history data for the given team.

        Args:
            team: The PFR team abbreviation (e.g. ``"phi"`` for
                Philadelphia Eagles). Case-insensitive; will be lowercased.
            timeout_ms: Optional timeout in milliseconds for the page
                selector.

        Returns:
            A :class:`~griddy.pfr.models.TeamDraft` instance containing
            all draft picks for the given team.
        """
        parser = self._parser
        return EndpointConfig(
            path_template="/teams/{team}/draft.htm",
            operation_id="getTeamDraft",
            wait_for_element="#draft",
            parser=lambda html: parser.parse_team_draft(html, team=team),
            response_type=TeamDraft,
            path_params={"team": team.lower()},
            timeout_ms=timeout_ms,
        )
