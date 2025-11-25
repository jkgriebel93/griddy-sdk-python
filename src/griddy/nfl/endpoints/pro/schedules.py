from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.mixins import GameScheduleMixin
from griddy.nfl.types import UNSET, OptionalNullable


class Schedules(ProSDK, GameScheduleMixin):
    r"""Game schedules, matchup rankings, and injury reports"""

    _COLLECTION_ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]

    def get_scheduled_games(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamesResponse:
        r"""Get Games by Week

        Retrieves all games for a specific season, season type, and week.
        Returns comprehensive game data including teams, venues, broadcast information,
        and ticket details for all games in the specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduledGamesRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/schedules/games",
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
            hook_ctx=self._create_hook_context("getScheduledGames", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.GamesResponse, self._COLLECTION_ERROR_CODES
        )

    async def get_scheduled_games_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamesResponse:
        r"""Get Games by Week

        Retrieves all games for a specific season, season type, and week.
        Returns comprehensive game data including teams, venues, broadcast information,
        and ticket details for all games in the specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduledGamesRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/games",
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
            hook_ctx=self._create_hook_context("getScheduledGames", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GamesResponse, self._COLLECTION_ERROR_CODES
        )

    def get_current_week_games(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CurrentGamesResponse:
        r"""Get Current Week Games

        Retrieves all games for the current week of the NFL season.
        Returns comprehensive game data including teams, venues, broadcast information,
        scores (for completed games), and ticket details. The endpoint automatically
        determines the current week based on the current date.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        req = self._build_request(
            method="GET",
            path="/api/schedules/current",
            base_url=base_url,
            url_variables=None,
            request=None,
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
            hook_ctx=self._create_hook_context("getCurrentWeekGames", base_url),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.CurrentGamesResponse, ["401", "4XX", "500", "5XX"]
        )

    async def get_current_week_games_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CurrentGamesResponse:
        r"""Get Current Week Games

        Retrieves all games for the current week of the NFL season.
        Returns comprehensive game data including teams, venues, broadcast information,
        scores (for completed games), and ticket details. The endpoint automatically
        determines the current week based on the current date.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/current",
            base_url=base_url,
            url_variables=None,
            request=None,
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
            hook_ctx=self._create_hook_context("getCurrentWeekGames", base_url),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.CurrentGamesResponse, ["401", "4XX", "500", "5XX"]
        )

    def get_future_betting_odds(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FuturesOddsResponseData:
        r"""Get Future Betting Odds

        Retrieves comprehensive betting futures data including Super Bowl odds,
        conference championship odds, and division winner odds for all teams.
        Returns decimal odds for each selection along with availability status.
        This endpoint provides futures market data across multiple betting hierarchies.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        req = self._build_request(
            method="GET",
            path="/api/schedules/genius/future/odds",
            base_url=base_url,
            url_variables=None,
            request=None,
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
            hook_ctx=self._create_hook_context("getFutureBettingOdds", base_url),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.FuturesOddsResponse, ["401", "4XX", "500", "5XX"]
        )

    async def get_future_betting_odds_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FuturesOddsResponseData:
        r"""Get Future Betting Odds

        Retrieves comprehensive betting futures data including Super Bowl odds,
        conference championship odds, and division winner odds for all teams.
        Returns decimal odds for each selection along with availability status.
        This endpoint provides futures market data across multiple betting hierarchies.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/genius/future/odds",
            base_url=base_url,
            url_variables=None,
            request=None,
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
            hook_ctx=self._create_hook_context("getFutureBettingOdds", base_url),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.FuturesOddsResponse, ["401", "4XX", "500", "5XX"]
        )

    def get_team_standings(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.StandingsResponse:
        r"""Get Team Standings

        Retrieves comprehensive team standings for a specific season, season type, and week.
        Returns detailed standings information including division, conference, home/away records,
        win percentages, points for/against, current streaks, and clinching scenarios.
        Standings are calculated through the specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamStandingsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/schedules/standings",
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
            hook_ctx=self._create_hook_context("getTeamStandings", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.StandingsResponse, self._COLLECTION_ERROR_CODES
        )

    async def get_team_standings_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.StandingsResponse:
        r"""Get Team Standings

        Retrieves comprehensive team standings for a specific season, season type, and week.
        Returns detailed standings information including division, conference, home/away records,
        win percentages, points for/against, current streaks, and clinching scenarios.
        Standings are calculated through the specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamStandingsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/standings",
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
            hook_ctx=self._create_hook_context("getTeamStandings", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.StandingsResponse, self._COLLECTION_ERROR_CODES
        )

    def get_schedule_season_weeks(
        self,
        *,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SeasonWeeksResponse:
        r"""Get Season Weeks

        Retrieves all weeks for a specific season including preseason, regular season,
        and postseason weeks. Returns week dates, types, and teams on bye for each week.
        This endpoint provides a comprehensive season calendar with all scheduling information.


        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduleSeasonWeeksRequest(
            season=season,
        )

        req = self._build_request(
            method="GET",
            path="/api/schedules/weeks",
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
            hook_ctx=self._create_hook_context("getScheduleSeasonWeeks", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.SeasonWeeksResponse, self._COLLECTION_ERROR_CODES
        )

    async def get_schedule_season_weeks_async(
        self,
        *,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SeasonWeeksResponse:
        r"""Get Season Weeks

        Retrieves all weeks for a specific season including preseason, regular season,
        and postseason weeks. Returns week dates, types, and teams on bye for each week.
        This endpoint provides a comprehensive season calendar with all scheduling information.


        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetScheduleSeasonWeeksRequest(
            season=season,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/weeks",
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
            hook_ctx=self._create_hook_context("getScheduleSeasonWeeks", base_url),
            request=req,
            error_status_codes=self._COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.SeasonWeeksResponse, self._COLLECTION_ERROR_CODES
        )
