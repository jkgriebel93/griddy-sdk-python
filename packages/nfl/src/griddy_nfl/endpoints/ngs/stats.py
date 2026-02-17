"""NGS Stats endpoints for player statistics."""

from __future__ import annotations

from typing import Mapping, Optional

from griddy_nfl import models
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.ngs import NgsBaseSDK
from griddy_nfl.types import UNSET, OptionalNullable
from griddy_nfl.utils import RetryConfig

# Standard error codes for NGS endpoints
NGS_ERROR_CODES = ["400", "401", "403", "404", "4XX", "500", "5XX"]


class NgsStats(NgsBaseSDK):
    """NGS Stats endpoints for player statistics.

    Provides access to:
    - Passing statistics (time to throw, air yards, completion probability, etc.)
    - Receiving statistics (separation, cushion, YAC, etc.)
    - Rushing statistics (time to LOS, rush yards over expected, etc.)
    """

    def get_passing_stats(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsPassingStatsResponse:
        """Get NGS passing statistics.

        Returns detailed passing statistics including time to throw,
        air yards, completion probability, and more.

        Args:
            season: The season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            week: Optional week filter
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            Dict containing passing statistics
        """
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/passing",
            operation_id="getNgsPassingStats",
            request=models.GetNgsPassingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsPassingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_passing_stats_async(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsPassingStatsResponse:
        """Get NGS passing statistics (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/passing",
            operation_id="getNgsPassingStats",
            request=models.GetNgsPassingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsPassingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_receiving_stats(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsReceivingStatsResponse:
        """Get NGS receiving statistics.

        Returns detailed receiving statistics including separation,
        cushion, YAC over expectation, and more.

        Args:
            season: The season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            week: Optional week filter
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            NgsReceivingStatsResponse containing receiving statistics
        """
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/receiving",
            operation_id="getNgsReceivingStats",
            request=models.GetNgsReceivingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsReceivingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_receiving_stats_async(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsReceivingStatsResponse:
        """Get NGS receiving statistics (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/receiving",
            operation_id="getNgsReceivingStats",
            request=models.GetNgsReceivingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsReceivingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_rushing_stats(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsRushingStatsResponse:
        """Get NGS rushing statistics.

        Returns detailed rushing statistics including time to LOS,
        rush yards over expected, efficiency, and more.

        Args:
            season: The season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            week: Optional week filter
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            NgsRushingStatsResponse containing rushing statistics
        """
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/rushing",
            operation_id="getNgsRushingStats",
            request=models.GetNgsRushingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsRushingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_rushing_stats_async(
        self,
        *,
        season: int,
        season_type: str,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsRushingStatsResponse:
        """Get NGS rushing statistics (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/statboard/rushing",
            operation_id="getNgsRushingStats",
            request=models.GetNgsRushingStatsRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsRushingStatsResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)
