from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.mixins import (
    GameContentMixin,
    GameResultsDataMixin,
    GameScheduleMixin,
)
from griddy.nfl.types import UNSET, OptionalNullable


class ProGames(ProSDK, GameScheduleMixin, GameContentMixin, GameResultsDataMixin):

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
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamecenterRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/stats/gamecenter",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getGamecenter", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model
        # Once fixed, use: return self._handle_json_response(http_res, models.GamecenterResponse, RESOURCE_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.GamecenterResponse, RESOURCE_ERROR_CODES
        )

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
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamecenterRequest(game_id=game_id)

        req = self._build_request_async(
            method="GET",
            path="/api/stats/gamecenter",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context("getGamecenter", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GamecenterResponse, RESOURCE_ERROR_CODES
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
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetLiveGameScoresRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/scores/live/games",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getLiveGameScores", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model
        # Once fixed, use: return self._handle_json_response(http_res, models.LiveScoresResponse, COLLECTION_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.LiveScoresResponse, COLLECTION_ERROR_CODES
        )

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
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetLiveGameScoresRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/scores/live/games",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context("getLiveGameScores", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.LiveScoresResponse, COLLECTION_ERROR_CODES
        )
