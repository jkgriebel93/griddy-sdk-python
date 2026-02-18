from typing import List, Mapping, Optional

from griddy.core._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class Games(BaseSDK):

    def _get_games_config(
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
    ) -> EndpointConfig:
        request = models.GetFootballGamesRequest(
            season=season,
            season_type=season_type,
            week=week,
            with_external_ids=with_external_ids,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/games/season/{season}/seasonType/{seasonType}/week/{week}",
            operation_id="getFootballGames",
            request=request,
            response_type=models.FootballGamesResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

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
        config = self._get_games_config(
            season=season,
            season_type=season_type,
            week=week,
            with_external_ids=with_external_ids,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_games_config(
            season=season,
            season_type=season_type,
            week=week,
            with_external_ids=with_external_ids,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_box_score_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetFootballBoxScoreRequest(game_id=game_id)

        return EndpointConfig(
            method="GET",
            path="/football/v2/games/{gameId}/boxscore",
            operation_id="getFootballBoxScore",
            request=request,
            response_type=models.BoxScoreResponse2,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
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
        config = self._get_box_score_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_box_score_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_play_by_play_config(
        self,
        *,
        game_id: str,
        include_penalties: Optional[bool] = True,
        include_formations: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetPlayByPlayRequest(
            game_id=game_id,
            include_penalties=include_penalties,
            include_formations=include_formations,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/games/{gameId}/playbyplay",
            operation_id="getPlayByPlay",
            request=request,
            response_type=models.PlayByPlayResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
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
        config = self._get_play_by_play_config(
            game_id=game_id,
            include_penalties=include_penalties,
            include_formations=include_formations,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_play_by_play_config(
            game_id=game_id,
            include_penalties=include_penalties,
            include_formations=include_formations,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_live_game_stats_config(
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
        request = models.GetLiveGameStatsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/stats/live/game-summaries",
            operation_id="getLiveGameStats",
            request=request,
            response_type=models.GameStatsResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
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
        config = self._get_live_game_stats_config(
            season=season,
            season_type=season_type,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    def _get_weekly_game_details_config(
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
    ) -> EndpointConfig:
        request = models.GetWeeklyGameDetailsRequest(
            season=season,
            type=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/experience/weekly-game-details",
            operation_id="getWeeklyGameDetails",
            request=request,
            response_type=List[models.WeeklyGameDetail],
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_weekly_game_details_config(
            season=season,
            type_=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_weekly_game_details_config(
            season=season,
            type_=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
