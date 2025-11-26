from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy.nfl.basesdk import EndpointConfig
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.mixins import (
    GameContentMixin,
    GameResultsDataMixin,
    GameScheduleMixin,
)
from griddy.nfl.types import UNSET, OptionalNullable


class ProGames(ProSDK, GameScheduleMixin, GameContentMixin, GameResultsDataMixin):

    def _get_gamecenter_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_gamecenter."""
        return EndpointConfig(
            method="GET",
            path="/api/stats/gamecenter",
            operation_id="getGamecenter",
            request=models.GetGamecenterRequest(game_id=game_id),
            response_type=models.GamecenterResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    # NOTE: game_id corresponds to an int here.
    # You must use the UUID that is returned by all (or most?) other
    # API endpoints to query the /schedules/game endpoint (or possibly others?)
    # and use the gameId from _that_ response.
    def get_gamecenter(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamecenterResponse:
        r"""Get Gamecenter Statistics

        Retrieves advanced game statistics including passer zones, receiver separation,
        pass rush metrics, and performance leaders for a specific game.


        :param game_id: Game identifier
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_gamecenter_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_gamecenter_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamecenterResponse:
        r"""Get Gamecenter Statistics

        Retrieves advanced game statistics including passer zones, receiver separation,
        pass rush metrics, and performance leaders for a specific game.


        :param game_id: Game identifier
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_gamecenter_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_live_game_scores_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_live_game_scores."""
        return EndpointConfig(
            method="GET",
            path="/api/scores/live/games",
            operation_id="getLiveGameScores",
            request=models.GetLiveGameScoresRequest(
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.LiveScoresResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_live_game_scores(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LiveScoresResponse:
        r"""Get Live Game Scores

        Retrieves real-time scores and game status for all games in a specified week.
        This endpoint updates frequently (15-second cache) to provide live scoring updates
        during active games. Returns an empty array when no games are currently being played.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_live_game_scores_config(
            season=season,
            season_type=season_type,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_live_game_scores_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.LiveScoresResponse:
        r"""Get Live Game Scores

        Retrieves real-time scores and game status for all games in a specified week.
        This endpoint updates frequently (15-second cache) to provide live scoring updates
        during active games. Returns an empty array when no games are currently being played.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_live_game_scores_config(
            season=season,
            season_type=season_type,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
