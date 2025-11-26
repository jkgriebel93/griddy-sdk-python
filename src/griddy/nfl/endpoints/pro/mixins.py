from typing import List, Mapping, Optional, Union

from griddy.nfl import models, utils
from griddy.nfl._constants import (
    COLLECTION_ERROR_CODES,
    RESOURCE_ERROR_CODES,
    SECURED_RESOURCE_ERROR_CODES,
)
from griddy.nfl.types import UNSET, OptionalNullable


class GameScheduleMixin:
    """Mixin for game schedule-related endpoints.

    These methods are designed to be mixed into classes that inherit from ProSDK/BaseSDK,
    which provides the helper methods (_resolve_base_url, _resolve_timeout, etc.).
    """

    def get_scheduled_game(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GameDetail:
        r"""Get Single Game Details

        Retrieves detailed information for a specific game by its ID.
        Returns comprehensive game data including teams, score, venue, broadcast information,
        and current game status.


        :param game_id: Game identifier (UUID format)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduledGameRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/schedules/game",
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
            hook_ctx=self._create_hook_context("getScheduledGame", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.GameDetail, RESOURCE_ERROR_CODES
        )

    async def get_scheduled_game_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GameDetail:
        r"""Get Single Game Details

        Retrieves detailed information for a specific game by its ID.
        Returns comprehensive game data including teams, score, venue, broadcast information,
        and current game status.


        :param game_id: Game identifier (UUID format)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduledGameRequest(game_id=game_id)

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/game",
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
            hook_ctx=self._create_hook_context("getScheduledGame", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GameDetail, RESOURCE_ERROR_CODES
        )

    def get_game_matchup_rankings(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.MatchupRankingsResponse:
        r"""Get Game Matchup Rankings

        Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
        Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
        for various statistical categories.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameMatchupRankingsRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/schedules/game/matchup/rankings",
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
            hook_ctx=self._create_hook_context("getGameMatchupRankings", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.MatchupRankingsResponse, RESOURCE_ERROR_CODES
        )

    async def get_game_matchup_rankings_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.MatchupRankingsResponse:
        r"""Get Game Matchup Rankings

        Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
        Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
        for various statistical categories.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameMatchupRankingsRequest(game_id=game_id)

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/game/matchup/rankings",
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
            hook_ctx=self._create_hook_context("getGameMatchupRankings", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.MatchupRankingsResponse, RESOURCE_ERROR_CODES
        )

    def get_game_team_rankings(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        away_team_id: str,
        home_team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRankingsResponse:
        r"""Get Team Rankings for Game

        Retrieves comprehensive statistical rankings for both teams in a specific game.
        Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


        :param season: Season year
        :param season_type: Type of season
        :param away_team_id: Away team UUID
        :param home_team_id: Home team UUID
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameTeamRankingsRequest(
            season=season,
            season_type=season_type,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/stats/game/team-rankings",
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
            hook_ctx=self._create_hook_context("getGameTeamRankings", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model
        # Once fixed, use: return self._handle_json_response(http_res, models.TeamRankingsResponse, COLLECTION_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamRankingsResponse, COLLECTION_ERROR_CODES
        )

    async def get_game_team_rankings_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        away_team_id: str,
        home_team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRankingsResponse:
        r"""Get Team Rankings for Game

        Retrieves comprehensive statistical rankings for both teams in a specific game.
        Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


        :param season: Season year
        :param season_type: Type of season
        :param away_team_id: Away team UUID
        :param home_team_id: Home team UUID
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameTeamRankingsRequest(
            season=season,
            season_type=season_type,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/stats/game/team-rankings",
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
            hook_ctx=self._create_hook_context("getGameTeamRankings", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.TeamRankingsResponse, COLLECTION_ERROR_CODES
        )

    def get_team_injuries(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        r"""Get Team Injuries for Game Week

        Retrieves injury report information for a specific team in a given week.
        Returns player injury status and details for the specified team and week.


        :param season: Season year
        :param season_type: Type of season
        :param team_id: Team identifier (UUID format)
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamInjuriesRequest(
            season=season,
            season_type=season_type,
            team_id=team_id,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/schedules/game/team/injuries",
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
            hook_ctx=self._create_hook_context("getTeamInjuries", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.InjuryReportResponse, RESOURCE_ERROR_CODES
        )

    async def get_team_injuries_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        r"""Get Team Injuries for Game Week

        Retrieves injury report information for a specific team in a given week.
        Returns player injury status and details for the specified team and week.


        :param season: Season year
        :param season_type: Type of season
        :param team_id: Team identifier (UUID format)
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamInjuriesRequest(
            season=season,
            season_type=season_type,
            team_id=team_id,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/game/team/injuries",
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
            hook_ctx=self._create_hook_context("getTeamInjuries", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.InjuryReportResponse, RESOURCE_ERROR_CODES
        )


class GameContentMixin:
    """Mixin for game content-related endpoints."""

    def get_game_preview(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        visitor_display_name: str,
        home_display_name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamePreviewResponse:
        r"""Get Game Preview Content

        Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param visitor_display_name: Visiting team display name
        :param home_display_name: Home team display name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamePreviewRequest(
            season=season,
            season_type=season_type,
            week=week,
            visitor_display_name=visitor_display_name,
            home_display_name=home_display_name,
        )

        req = self._build_request(
            method="GET",
            path="/api/content/game/preview",
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
            hook_ctx=self._create_hook_context("getGamePreview", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: The model is busted, so unmarshaling returns an empty dict
        return self._handle_json_response(
            http_res, models.GamePreviewResponse, COLLECTION_ERROR_CODES
        )

    async def get_game_preview_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        visitor_display_name: str,
        home_display_name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamePreviewResponse:
        r"""Get Game Preview Content

        Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param visitor_display_name: Visiting team display name
        :param home_display_name: Home team display name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamePreviewRequest(
            season=season,
            season_type=season_type,
            week=week,
            visitor_display_name=visitor_display_name,
            home_display_name=home_display_name,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/content/game/preview",
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
            hook_ctx=self._create_hook_context("getGamePreview", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GamePreviewResponse, COLLECTION_ERROR_CODES
        )

    def get_game_insights(
        self,
        *,
        season: int,
        fapi_game_id: str,
        away_team_id: str,
        home_team_id: str,
        limit: Optional[int] = 20,
        tags: Optional[str] = None,
        exclude_tags: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.GameInsight]:
        r"""Get Game-Specific Insights

        Retrieves analytical insights and advanced statistics for a specific game.
        Can filter by tags and exclude specific content types.


        :param season: Season year
        :param fapi_game_id: FAPI Game identifier (UUID)
        :param away_team_id: Away team identifier
        :param home_team_id: Home team identifier
        :param limit: Maximum number of insights to return
        :param tags: Comma-separated list of tags to filter by
        :param exclude_tags: Comma-separated list of tags to exclude
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            exclude_tags=exclude_tags,
            fapi_game_id=fapi_game_id,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
        )

        req = self._build_request(
            method="GET",
            path="/api/content/insights/game",
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
            hook_ctx=self._create_hook_context("getGameInsights", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, List[models.GameInsight], COLLECTION_ERROR_CODES
        )

    async def get_game_insights_async(
        self,
        *,
        season: int,
        fapi_game_id: str,
        away_team_id: str,
        home_team_id: str,
        limit: Optional[int] = 20,
        tags: Optional[str] = None,
        exclude_tags: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.GameInsight]:
        r"""Get Game-Specific Insights

        Retrieves analytical insights and advanced statistics for a specific game.
        Can filter by tags and exclude specific content types.


        :param season: Season year
        :param fapi_game_id: FAPI Game identifier (UUID)
        :param away_team_id: Away team identifier
        :param home_team_id: Home team identifier
        :param limit: Maximum number of insights to return
        :param tags: Comma-separated list of tags to filter by
        :param exclude_tags: Comma-separated list of tags to exclude
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            exclude_tags=exclude_tags,
            fapi_game_id=fapi_game_id,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/content/insights/game",
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
            hook_ctx=self._create_hook_context("getGameInsights", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, List[models.GameInsight], COLLECTION_ERROR_CODES
        )


class GameResultsDataMixin:
    """Mixin for game results and play data endpoints."""

    def get_stats_boxscore(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.BoxscoreResponse:
        r"""Get Game Boxscore (Stats API)

        Retrieves comprehensive boxscore data for a specific game including team statistics,
        individual player statistics, and scoring summary. Returns empty arrays for future games.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetStatsBoxscoreRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/stats/boxscore",
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
            hook_ctx=self._create_hook_context("getStatsBoxscore", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model
        # Once fixed, use: return self._handle_json_response(http_res, models.BoxscoreResponse, RESOURCE_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.BoxscoreResponse, RESOURCE_ERROR_CODES
        )

    def get_playlist(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""
        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayListRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/secured/plays/playlist/game",
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
            hook_ctx=self._create_hook_context("getPlaysWinProbability", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Implement the pydantic models for PlayList & related response
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(http_res, dict, RESOURCE_ERROR_CODES)

    def get_summary_play(
        self,
        *,
        game_id: str,
        play_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlaySummaryResponse:
        r"""Get Play Summary

        Retrieves detailed information about a specific play in a game including play description,
        statistics, involved players, win probability, and expected points.


        :param game_id: Game identifier (UUID format)
        :param play_id: Play identifier within the game
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetSummaryPlayRequest(
            game_id=game_id,
            play_id=play_id,
        )

        req = self._build_request(
            method="GET",
            path="/api/plays/summaryPlay",
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
            hook_ctx=self._create_hook_context("getSummaryPlay", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.PlaySummaryResponse, RESOURCE_ERROR_CODES
        )

    async def get_summary_play_async(
        self,
        *,
        game_id: str,
        play_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlaySummaryResponse:
        r"""Get Play Summary

        Retrieves detailed information about a specific play in a game including play description,
        statistics, involved players, win probability, and expected points.


        :param game_id: Game identifier (UUID format)
        :param play_id: Play identifier within the game
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetSummaryPlayRequest(
            game_id=game_id,
            play_id=play_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/plays/summaryPlay",
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
            hook_ctx=self._create_hook_context("getSummaryPlay", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.PlaySummaryResponse, RESOURCE_ERROR_CODES
        )

    def get_plays_win_probability(
        self,
        *,
        game_id: Union[models.GameID, models.GameIDTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetPlaysWinProbabilityResponse:
        r"""Get Game Win Probability by Plays

        Retrieves comprehensive win probability data for every play in specified games.
        Returns pre-game win probabilities and detailed play-by-play probability changes,
        including Win Probability Added (WPA) metrics for each play. This advanced analytics
        endpoint tracks how each play impacts the probability of each team winning the game.
        Supports querying multiple games simultaneously.


        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlaysWinProbabilityRequest(game_id=game_id)

        req = self._build_request(
            method="GET",
            path="/api/secured/plays/winProbability",
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
            hook_ctx=self._create_hook_context("getPlaysWinProbability", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model
        # Once fixed, use: return self._handle_json_response(http_res, models.GetPlaysWinProbabilityResponse, RESOURCE_ERROR_CODES)
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.GetPlaysWinProbabilityResponse, RESOURCE_ERROR_CODES
        )

    async def get_plays_win_probability_async(
        self,
        *,
        game_id: Union[models.GameID, models.GameIDTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetPlaysWinProbabilityResponse:
        r"""Get Game Win Probability by Plays

        Retrieves comprehensive win probability data for every play in specified games.
        Returns pre-game win probabilities and detailed play-by-play probability changes,
        including Win Probability Added (WPA) metrics for each play. This advanced analytics
        endpoint tracks how each play impacts the probability of each team winning the game.
        Supports querying multiple games simultaneously.


        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlaysWinProbabilityRequest(game_id=game_id)

        req = self._build_request_async(
            method="GET",
            path="/api/secured/plays/winProbability",
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
            hook_ctx=self._create_hook_context("getPlaysWinProbability", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GetPlaysWinProbabilityResponse, RESOURCE_ERROR_CODES
        )

    def get_win_probability_min(
        self,
        *,
        fapi_game_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WinProbabilityResponse:
        r"""Get Minimal Win Probability Data

        Retrieves minimal win probability data for specified games, including pregame
        win probabilities and play-by-play probability changes throughout the game.
        This endpoint provides essential win probability metrics with optimized data
        structure for performance. Supports multiple games in a single request.


        :param fapi_game_id: Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetWinProbabilityMinRequest(fapi_game_id=fapi_game_id)

        req = self._build_request(
            method="GET",
            path="/api/secured/plays/winProbabilityMin",
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
            hook_ctx=self._create_hook_context("getWinProbabilityMin", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.WinProbabilityResponse, RESOURCE_ERROR_CODES
        )

    async def get_win_probability_min_async(
        self,
        *,
        fapi_game_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WinProbabilityResponse:
        r"""Get Minimal Win Probability Data

        Retrieves minimal win probability data for specified games, including pregame
        win probabilities and play-by-play probability changes throughout the game.
        This endpoint provides essential win probability metrics with optimized data
        structure for performance. Supports multiple games in a single request.


        :param fapi_game_id: Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetWinProbabilityMinRequest(fapi_game_id=fapi_game_id)

        req = self._build_request_async(
            method="GET",
            path="/api/secured/plays/winProbabilityMin",
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
            hook_ctx=self._create_hook_context("getWinProbabilityMin", base_url),
            request=req,
            error_status_codes=RESOURCE_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.WinProbabilityResponse, RESOURCE_ERROR_CODES
        )
