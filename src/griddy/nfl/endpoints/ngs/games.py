"""NGS Games endpoints for live scores and game center data."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional

from griddy.nfl import models
from griddy.nfl.basesdk import EndpointConfig
from griddy.nfl.endpoints.ngs import NgsBaseSDK
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import RetryConfig

# Standard error codes for NGS endpoints
NGS_ERROR_CODES = ["400", "401", "403", "404", "4XX", "500", "5XX"]


class NgsGames(NgsBaseSDK):
    """NGS Games endpoints for live scores and game center data.

    Provides access to:
    - Live game scores
    - Game center overview with detailed NGS metrics
    """

    def get_live_scores(
        self,
        *,
        season: int,
        season_type: str,
        week: int,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsLiveScoresResponse:
        """Get live game scores for a specific week.

        Returns live scores for all games in the specified week, including
        quarter-by-quarter scoring, game status, and team information.

        Args:
            season: The season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            week: Week number
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            NgsLiveScoresResponse with game scores
        """
        config = EndpointConfig(
            method="GET",
            path="/api/live/games/scores",
            operation_id="getNgsLiveScores",
            request=models.GetNgsLiveScoresRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsLiveScoresResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
        return self._execute_endpoint(config)

    async def get_live_scores_async(
        self,
        *,
        season: int,
        season_type: str,
        week: int,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.NgsLiveScoresResponse:
        """Get live game scores for a specific week (async).

        Returns live scores for all games in the specified week, including
        quarter-by-quarter scoring, game status, and team information.

        Args:
            season: The season year (e.g., 2025)
            season_type: Season type (REG, PRE, POST)
            week: Week number
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            NgsLiveScoresResponse with game scores
        """
        config = EndpointConfig(
            method="GET",
            path="/api/live/games/scores",
            operation_id="getNgsLiveScores",
            request=models.GetNgsLiveScoresRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.NgsLiveScoresResponse,
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
        return await self._execute_endpoint_async(config)

    def get_overview(
        self,
        *,
        game_id: int,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get detailed game center overview with NGS metrics.

        Returns comprehensive game data including:
        - Passer statistics with zone breakdowns
        - Rusher statistics with location maps
        - Receiver statistics with separation metrics
        - Pass rusher statistics
        - Game leaders (speed, sacks, pass distance)

        Args:
            game_id: The unique game identifier (e.g., 2025112700)
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            Dict containing the full game overview response

        Note:
            This endpoint returns raw JSON due to the complexity of the
            nested response structure. Future versions may add typed models.
        """
        config = EndpointConfig(
            method="GET",
            path="/api/gamecenter/overview",
            operation_id="getNgsGameOverview",
            request=models.GetNgsGameOverviewRequest(game_id=game_id),
            response_type=Dict[str, Any],
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,
        )
        return self._execute_endpoint(config)

    async def get_overview_async(
        self,
        *,
        game_id: int,
        retries: OptionalNullable[RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get detailed game center overview with NGS metrics (async).

        Returns comprehensive game data including:
        - Passer statistics with zone breakdowns
        - Rusher statistics with location maps
        - Receiver statistics with separation metrics
        - Pass rusher statistics
        - Game leaders (speed, sacks, pass distance)

        Args:
            game_id: The unique game identifier (e.g., 2025112700)
            retries: Override the default retry configuration
            server_url: Override the default server URL
            timeout_ms: Override the default timeout
            http_headers: Additional headers to send

        Returns:
            Dict containing the full game overview response

        Note:
            This endpoint returns raw JSON due to the complexity of the
            nested response structure. Future versions may add typed models.
        """
        config = EndpointConfig(
            method="GET",
            path="/api/gamecenter/overview",
            operation_id="getNgsGameOverview",
            request=models.GetNgsGameOverviewRequest(game_id=game_id),
            response_type=Dict[str, Any],
            error_status_codes=NGS_ERROR_CODES,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,
        )
        return await self._execute_endpoint_async(config)
