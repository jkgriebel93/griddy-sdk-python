from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable


# TODO: Not sure where to put this module
class Betting(ProSDK):
    r"""Game betting odds and lines"""

    # Standard error codes for this endpoint
    _ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]

    def get_weekly_betting_odds(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyOddsResponse:
        r"""Get Weekly Betting Odds

        Retrieves comprehensive betting odds for all games in a specified week.
        Returns point spreads, money lines, and totals (over/under) for each game
        with the latest odds updates from betting markets.


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

        request = models.GetWeeklyBettingOddsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request(
            method="GET",
            path="/api/schedules/week/odds",
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
            hook_ctx=self._create_hook_context("getWeeklyBettingOdds", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.WeeklyOddsResponse, self._ERROR_CODES
        )

    async def get_weekly_betting_odds_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyOddsResponse:
        r"""Get Weekly Betting Odds

        Retrieves comprehensive betting odds for all games in a specified week.
        Returns point spreads, money lines, and totals (over/under) for each game
        with the latest odds updates from betting markets.


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

        request = models.GetWeeklyBettingOddsRequest(
            season=season,
            season_type=season_type,
            week=week,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/schedules/week/odds",
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
            hook_ctx=self._create_hook_context("getWeeklyBettingOdds", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.WeeklyOddsResponse, self._ERROR_CODES
        )
