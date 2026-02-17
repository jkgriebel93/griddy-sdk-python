from typing import Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import RESOURCE_ERROR_CODES
from griddy_nfl.basesdk import BaseSDK, EndpointConfig
from griddy_nfl.types import UNSET, OptionalNullable


class LiveStats(BaseSDK):

    def _get_team_statistics_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetLiveTeamStatisticsRequest(
            game_id=game_id,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/stats/live/team-statistics/{gameId}",
            operation_id="getLiveTeamStatistics",
            request=request,
            response_type=models.LiveTeamStatisticsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_team_statistics(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LiveTeamStatisticsResponse:
        r"""Get Live Team Statistics

        Retrieves live team statistics for a specific game.
        Returns awayTeam and homeTeam objects each containing 100+ stat fields.


        :param game_id: Game identifier (UUID)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_statistics_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_team_statistics_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LiveTeamStatisticsResponse:
        r"""Get Live Team Statistics"""
        config = self._get_team_statistics_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_player_statistics_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetLivePlayerStatisticsRequest(
            game_id=game_id,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/stats/live/player-statistics/{gameId}",
            operation_id="getLivePlayerStatistics",
            request=request,
            response_type=models.LivePlayerStatisticsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_player_statistics(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LivePlayerStatisticsResponse:
        r"""Get Live Player Statistics

        Retrieves live player statistics for a specific game.
        Returns awayTeam and homeTeam objects, each containing a players
        array with per-player identification and 100+ stat fields.


        :param game_id: Game identifier (UUID)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_player_statistics_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_player_statistics_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LivePlayerStatisticsResponse:
        r"""Get Live Player Statistics"""
        config = self._get_player_statistics_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
