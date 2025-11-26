from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import STATS_ERROR_CODES
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable

# TODO: All the requests in this file have broken Pydantic models


class PlayerReceivingStats(ProSDK):

    def get_season_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.ReceivingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_receiver: Optional[bool] = False,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReceivingStatsResponse:
        r"""Get Player Receiving Statistics by Season

        Retrieves comprehensive receiving statistics for NFL players during a specified season.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_receiver: Filter to only qualified receivers
        :param team_offense: Filter by specific team IDs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayerReceivingStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_receiver=qualified_receiver,
            team_offense=team_offense,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/players-offense/receiving/season",
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
            hook_ctx=self._create_hook_context(
                "getPlayerReceivingStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model - schema is broken
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.ReceivingStatsResponse, STATS_ERROR_CODES
        )

    async def get_season_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.ReceivingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_receiver: Optional[bool] = False,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReceivingStatsResponse:
        r"""Get Player Receiving Statistics by Season

        Retrieves comprehensive receiving statistics for NFL players during a specified season.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_receiver: Filter to only qualified receivers
        :param team_offense: Filter by specific team IDs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayerReceivingStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_receiver=qualified_receiver,
            team_offense=team_offense,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/players-offense/receiving/season",
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
            hook_ctx=self._create_hook_context(
                "getPlayerReceivingStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model - schema is broken
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.ReceivingStatsResponse, STATS_ERROR_CODES
        )

    def get_weekly_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 50,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.ReceivingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_receiver: Optional[bool] = False,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReceivingStatsResponse:
        r"""Get Player Receiving Statistics by Week

        Retrieves comprehensive receiving statistics for NFL players during a specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week identifier
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_receiver: Filter to only qualified receivers
        :param team_offense: Filter by specific team IDs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayerReceivingStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_receiver=qualified_receiver,
            team_offense=team_offense,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/players-offense/receiving/week",
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
            hook_ctx=self._create_hook_context(
                "getPlayerReceivingStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model - schema is broken
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.ReceivingStatsResponse, STATS_ERROR_CODES
        )

    async def get_weekly_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 50,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.ReceivingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_receiver: Optional[bool] = False,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReceivingStatsResponse:
        r"""Get Player Receiving Statistics by Week

        Retrieves comprehensive receiving statistics for NFL players during a specified week.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week identifier
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_receiver: Filter to only qualified receivers
        :param team_offense: Filter by specific team IDs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetPlayerReceivingStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_receiver=qualified_receiver,
            team_offense=team_offense,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/players-offense/receiving/week",
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
            hook_ctx=self._create_hook_context(
                "getPlayerReceivingStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: Fix Pydantic model - schema is broken
        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.ReceivingStatsResponse, STATS_ERROR_CODES
        )
