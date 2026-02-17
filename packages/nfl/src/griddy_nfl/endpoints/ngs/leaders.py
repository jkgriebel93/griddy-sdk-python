"""NGS Leaders endpoints for top plays and leaderboards."""

from __future__ import annotations

from typing import Mapping, Optional

from griddy_nfl import models
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.ngs import NgsBaseSDK
from griddy_nfl.types import UNSET, OptionalNullable
from griddy_nfl.utils import RetryConfig

NGS_ERROR_CODES = ["400", "401", "403", "404", "4XX", "500", "5XX"]


class NgsLeaders(NgsBaseSDK):
    """NGS Leaders endpoints for top plays and leaderboards.

    Provides access to:
    - Fastest ball carriers (max speed)
    - Fastest sacks (time to sack)
    - Improbable completions (completion probability)
    - Incredible YAC (yards after catch over expectation)
    - Longest plays (in-play distance)
    - Longest tackles (distance covered to tackle)
    - Remarkable rushes (rush yards over expected)
    """

    def get_fastest_ball_carriers(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsSpeedLeadersResponse:
        """Get fastest ball carrier speeds.

        Returns leaderboard of fastest ball carrier speeds recorded.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            limit: Number of results (default: 20)
            week: Optional week filter
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/speed/ballCarrier",
            operation_id="getNgsFastestBallCarriers",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsSpeedLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_fastest_ball_carriers_async(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsSpeedLeadersResponse:
        """Get fastest ball carrier speeds (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/speed/ballCarrier",
            operation_id="getNgsFastestBallCarriers",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsSpeedLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_fastest_sacks(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsSackLeadersResponse:
        """Get fastest sack times.

        Returns leaderboard of quickest sacks by time to tackle.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            limit: Number of results (default: 20)
            week: Optional week filter
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/time/sack",
            operation_id="getNgsFastestSacks",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsSackLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_fastest_sacks_async(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsSackLeadersResponse:
        """Get fastest sack times (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/time/sack",
            operation_id="getNgsFastestSacks",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsSackLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_improbable_completions(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsCompletionLeadersResponse:
        """Get most improbable completions.

        Returns leaderboard of completions with lowest completion probability.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/completion/season",
            operation_id="getNgsImprobableCompletions",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsCompletionLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_improbable_completions_async(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsCompletionLeadersResponse:
        """Get most improbable completions (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/completion/season",
            operation_id="getNgsImprobableCompletions",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsCompletionLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_incredible_yac(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsYACLeadersResponse:
        """Get incredible YAC plays.

        Returns leaderboard of yards after catch over expectation.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/yac/season",
            operation_id="getNgsIncredibleYAC",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsYACLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_incredible_yac_async(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsYACLeadersResponse:
        """Get incredible YAC plays (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/yac/season",
            operation_id="getNgsIncredibleYAC",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsYACLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_longest_plays(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsDistanceLeadersResponse:
        """Get longest plays by in-play distance.

        Returns leaderboard of plays with most distance covered.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            limit: Number of results (default: 20)
            week: Optional week filter
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/distance/ballCarrier",
            operation_id="getNgsLongestPlays",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsDistanceLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_longest_plays_async(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsDistanceLeadersResponse:
        """Get longest plays by in-play distance (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/distance/ballCarrier",
            operation_id="getNgsLongestPlays",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsDistanceLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_longest_tackles(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsTackleLeadersResponse:
        """Get longest tackles by distance covered.

        Returns leaderboard of tackles with most distance covered to make the tackle.

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            limit: Number of results (default: 20)
            week: Optional week filter
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/distance/tackle",
            operation_id="getNgsLongestTackles",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsTackleLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_longest_tackles_async(
        self,
        *,
        season: int,
        season_type: str,
        limit: int = 20,
        week: Optional[int] = None,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsTackleLeadersResponse:
        """Get longest tackles by distance covered (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/distance/tackle",
            operation_id="getNgsLongestTackles",
            request=models.GetNgsLeadersRequest(
                season=season, season_type=season_type, limit=limit, week=week
            ),
            response_type=models.NgsTackleLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)

    def get_remarkable_rushes(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsERYLeadersResponse:
        """Get remarkable rushes.

        Returns leaderboard of rush yards over expected (ERY).

        Args:
            season: Season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
        """
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/ery/season",
            operation_id="getNgsRemarkableRushes",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsERYLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return self._execute_endpoint(config)

    async def get_remarkable_rushes_async(
        self,
        *,
        season: int,
        season_type: str,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsERYLeadersResponse:
        """Get remarkable rushes (async)."""
        config = EndpointConfig(
            method="GET",
            path="/api/leaders/expectation/ery/season",
            operation_id="getNgsRemarkableRushes",
            request=models.GetNgsSeasonLeadersRequest(
                season=season, season_type=season_type
            ),
            response_type=models.NgsERYLeadersResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
        return await self._execute_endpoint_async(config)
