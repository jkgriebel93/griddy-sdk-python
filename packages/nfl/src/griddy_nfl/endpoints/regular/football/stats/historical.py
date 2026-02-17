from typing import Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import RESOURCE_ERROR_CODES
from griddy_nfl.basesdk import BaseSDK, EndpointConfig
from griddy_nfl.types import UNSET, OptionalNullable


class HistoricalStats(BaseSDK):

    def _get_team_stats_config(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetHistoricalTeamStatsRequest(
            game_id=game_id,
            team_id=team_id,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/stats/historical/game/{gameId}/team/{teamId}",
            operation_id="getHistoricalTeamStats",
            request=request,
            response_type=models.HistoricalTeamStatsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_team_stats(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HistoricalTeamStatsResponse:
        r"""Get Historical Team Stats

        Retrieves historical team statistics for a specific game and team.
        Returns game info, team info, and deeply nested stat categories
        (defense, passing, rushing, receiving, kicking, etc.).


        :param game_id: Game identifier (UUID)
        :param team_id: Team identifier (UUID)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_stats_config(
            game_id=game_id,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_team_stats_async(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HistoricalTeamStatsResponse:
        r"""Get Historical Team Stats"""
        config = self._get_team_stats_config(
            game_id=game_id,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_player_stats_config(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetHistoricalPlayerStatsRequest(
            game_id=game_id,
            team_id=team_id,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/stats/historical/game/{gameId}/persons/team/{teamId}",
            operation_id="getHistoricalPlayerStats",
            request=request,
            response_type=models.HistoricalPlayerStatsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=False,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_player_stats(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HistoricalPlayerStatsResponse:
        r"""Get Historical Player Stats

        Retrieves historical player statistics for a specific game and team.
        Returns game and team identifiers and a list of per-player stat objects
        with nullable stat categories (defense, passing, rushing, etc.).


        :param game_id: Game identifier (UUID)
        :param team_id: Team identifier (UUID)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_player_stats_config(
            game_id=game_id,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_player_stats_async(
        self,
        *,
        game_id: str,
        team_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HistoricalPlayerStatsResponse:
        r"""Get Historical Player Stats"""
        config = self._get_player_stats_config(
            game_id=game_id,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
