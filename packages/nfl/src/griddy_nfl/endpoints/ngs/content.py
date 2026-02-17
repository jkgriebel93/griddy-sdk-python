"""NGS Content endpoints for charts and highlights."""

from __future__ import annotations

from typing import Mapping, Optional

from griddy_nfl import models
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.ngs import NgsBaseSDK
from griddy_nfl.types import UNSET, OptionalNullable
from griddy_nfl.utils import RetryConfig

NGS_ERROR_CODES = ["400", "401", "403", "404", "4XX", "500", "5XX"]


class NgsContent(NgsBaseSDK):
    """NGS Content endpoints for charts and highlights.

    Provides access to:
    - Player charts (route, pass, carry)
    - Chart players list
    - Play highlights
    """

    def get_charts(
        self,
        *,
        season: int,
        count: int = 12,
        week: str = "all",
        chart_type: str = "all",
        team_id: str = "all",
        esb_id: str = "all",
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsChartsResponse:
        """Get player charts (route, pass, carry).

        Args:
            season: Season year (e.g., 2025)
            count: Number of charts to return (default: 12)
            week: Week filter or "all" (default: "all")
            chart_type: Chart type filter: "all", "route", "pass", "carry"
            team_id: Team ID filter or "all"
            esb_id: Player ESB ID filter or "all"
        """
        config = EndpointConfig(
            method="GET",
            path="/api/content/microsite/chart",
            operation_id="getNgsCharts",
            request=models.GetNgsChartsRequest(
                season=season,
                count=count,
                week=week,
                chart_type=chart_type,
                team_id=team_id,
                esb_id=esb_id,
            ),
            response_type=models.NgsChartsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_charts_async(
        self,
        *,
        season: int,
        count: int = 12,
        week: str = "all",
        chart_type: str = "all",
        team_id: str = "all",
        esb_id: str = "all",
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsChartsResponse:
        """Get player charts (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/content/microsite/chart",
            operation_id="getNgsCharts",
            request=models.GetNgsChartsRequest(
                season=season,
                count=count,
                week=week,
                chart_type=chart_type,
                team_id=team_id,
                esb_id=esb_id,
            ),
            response_type=models.NgsChartsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_players(
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsChartPlayersResponse:
        """Get players available in the chart system."""
        config = EndpointConfig(
            method="GET",
            path="/api/content/microsite/chart/players",
            operation_id="getNgsChartPlayers",
            request=models.GetNgsCurrentScheduleRequest(),  # No params needed
            response_type=models.NgsChartPlayersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_players_async(
        self,
        *,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsChartPlayersResponse:
        """Get players available in the chart system (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/content/microsite/players",
            operation_id="getNgsChartPlayers",
            request=models.GetNgsCurrentScheduleRequest(),
            response_type=models.NgsChartPlayersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_highlights(
        self,
        *,
        season: int,
        limit: int = 16,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsHighlightsResponse:
        """Get play highlights.

        Args:
            season: Season year (e.g., 2025)
            limit: Number of highlights to return (default: 16)
        """
        config = EndpointConfig(
            method="GET",
            path="/api/plays/highlights",
            operation_id="getNgsHighlights",
            request=models.GetNgsHighlightsRequest(season=season, limit=limit),
            response_type=models.NgsHighlightsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_highlights_async(
        self,
        *,
        season: int,
        limit: int = 16,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsHighlightsResponse:
        """Get play highlights (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/plays/highlights",
            operation_id="getNgsHighlights",
            request=models.GetNgsHighlightsRequest(season=season, limit=limit),
            response_type=models.NgsHighlightsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)
