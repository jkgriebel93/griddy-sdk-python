from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
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
