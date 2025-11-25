from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.types import UNSET, OptionalNullable


class Games(BaseSDK):
    _COLLECTION_ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]
    _RESOURCE_ERROR_CODES = ["400", "401", "404", "4XX", "500", "5XX"]

    def get_games(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        with_external_ids: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballGamesResponse:
        r"""Get Games by Season, Type, and Week

        Retrieves game information for a specific season, season type, and week from the Football API.
        This endpoint provides core game data with external IDs.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param with_external_ids: Include external IDs in response
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballGamesRequest(
            season=season,
            season_type=season_type,
            week=week,
            with_external_ids=with_external_ids,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/games/season/{season}/seasonType/{seasonType}/week/{week}",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getFootballGames", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.FootballGamesResponse, self._COLLECTION_ERROR_CODES
        )

    async def get_games_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        with_external_ids: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballGamesResponse:
        r"""Get Games by Season, Type, and Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballGamesRequest(
            season=season,
            season_type=season_type,
            week=week,
            with_external_ids=with_external_ids,
        )

        req = self._build_request_async(
            method="GET",
            path="/football/v2/games/season/{season}/seasonType/{seasonType}/week/{week}",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context("getFootballGames", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.FootballGamesResponse, self._COLLECTION_ERROR_CODES
        )

    def get_box_score(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.BoxScoreResponse2:
        r"""Get Game Box Score (Football API)

        Retrieves comprehensive box score data for a specific game including
        team statistics, individual player statistics, and scoring summary.


        :param game_id: Game identifier (UUID)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballBoxScoreRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/football/v2/games/{gameId}/boxscore",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getFootballBoxScore", base_url),
            request=req,
            error_status_codes=self._RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.BoxScoreResponse2, self._RESOURCE_ERROR_CODES
        )

    async def get_box_score_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.BoxScoreResponse2:
        r"""Get Game Box Score (Football API)"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballBoxScoreRequest(game_id=game_id)

        req = self._build_request_async(
            method="GET",
            path="/football/v2/games/{gameId}/boxscore",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context("getFootballBoxScore", base_url),
            request=req,
            error_status_codes=self._RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.BoxScoreResponse2, self._RESOURCE_ERROR_CODES
        )

    def get_play_by_play(
        self,
        *,
        game_id: str,
        include_penalties: Optional[bool] = True,
        include_formations: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayByPlayResponse:
        r"""Get Play-by-Play Data

        Retrieves detailed play-by-play data for a specific game including
        all plays, drives, scoring events, and key statistics.


        :param game_id: Game identifier (UUID)
        :param include_penalties: Include penalty details
        :param include_formations: Include offensive/defensive formations
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayByPlayRequest(
            game_id=game_id,
            include_penalties=include_penalties,
            include_formations=include_formations,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/games/{gameId}/playbyplay",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = self.do_request(
            hook_ctx=self._create_hook_context("getPlayByPlay", base_url),
            request=req,
            error_status_codes=self._RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.PlayByPlayResponse, self._RESOURCE_ERROR_CODES
        )

    async def get_play_by_play_async(
        self,
        *,
        game_id: str,
        include_penalties: Optional[bool] = True,
        include_formations: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayByPlayResponse:
        r"""Get Play-by-Play Data"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayByPlayRequest(
            game_id=game_id,
            include_penalties=include_penalties,
            include_formations=include_formations,
        )

        req = self._build_request_async(
            method="GET",
            path="/football/v2/games/{gameId}/playbyplay",
            base_url=base_url,
            url_variables=None,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        retry_config = self._resolve_retry_config(retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context("getPlayByPlay", base_url),
            request=req,
            error_status_codes=self._RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.PlayByPlayResponse, self._RESOURCE_ERROR_CODES
        )

    def get_live_game_stats(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.GameStatsResponseData]:
        r"""Get Live Game Statistics

        Retrieves live game statistics and summaries for games in progress or completed games.
        Provides real-time statistical data for specified season, type, and week.


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

        request = models.GetLiveGameStatsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/stats/live/game-summaries",
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
            hook_ctx=self._create_hook_context("getLiveGameStats", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.GameStatsResponse, self._COLLECTION_ERROR_CODES
        )

    def get_weekly_game_details(
        self,
        *,
        season: int,
        type_: models.SeasonTypeEnum,
        week: int,
        include_drive_chart: Optional[bool] = False,
        include_replays: Optional[bool] = False,
        include_standings: Optional[bool] = False,
        include_tagged_videos: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.WeeklyGameDetail]:
        r"""Get Weekly Game Details

        Retrieves detailed game information for a specific week including team standings,
        drive charts, replays, and tagged videos.


        :param season: Season year
        :param type_: Season type
        :param week: Week number
        :param include_drive_chart: Include drive chart data
        :param include_replays: Include replay videos
        :param include_standings: Include team standings
        :param include_tagged_videos: Include tagged video content
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetWeeklyGameDetailsRequest(
            season=season,
            type=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/experience/weekly-game-details",
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
            hook_ctx=self._create_hook_context("getWeeklyGameDetails", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic models
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, List[models.WeeklyGameDetail], self._COLLECTION_ERROR_CODES
        )

    async def get_weekly_game_details_async(
        self,
        *,
        season: int,
        type_: models.SeasonTypeEnum,
        week: int,
        include_drive_chart: Optional[bool] = False,
        include_replays: Optional[bool] = False,
        include_standings: Optional[bool] = False,
        include_tagged_videos: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.WeeklyGameDetail]:
        r"""Get Weekly Game Details"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetWeeklyGameDetailsRequest(
            season=season,
            type=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
        )

        req = self._build_request_async(
            method="GET",
            path="/football/v2/experience/weekly-game-details",
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
            hook_ctx=self._create_hook_context("getWeeklyGameDetails", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, List[models.WeeklyGameDetail], self._COLLECTION_ERROR_CODES
        )
