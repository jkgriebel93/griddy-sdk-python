from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import STATS_ERROR_CODES
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable

# TODO: All the requests in this file have broken Pydantic models


class PlayerDefenseStats(ProSDK):

    def get_season_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensiveOverviewStatsBySeasonSortKey] = "snap",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        team_defense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DefensiveOverviewStatsResponse:
        r"""Get Defensive Player Overview Statistics by Season

        Retrieves comprehensive defensive overview statistics for NFL players during a specified season.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders
        :param team_defense: Filter by specific team IDs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveOverviewStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            team_defense=team_defense,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/overview/season",
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
                "getDefensiveOverviewStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.DefensiveOverviewStatsResponse, STATS_ERROR_CODES
        )

    async def get_season_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensiveOverviewStatsBySeasonSortKey] = "snap",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        team_defense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DefensiveOverviewStatsResponse:
        r"""Get Defensive Player Overview Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveOverviewStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            team_defense=team_defense,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/overview/season",
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
                "getDefensiveOverviewStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.DefensiveOverviewStatsResponse, STATS_ERROR_CODES
        )

    def get_weekly_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensiveOverviewStatsBySeasonSortKey] = "snap",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        team_defense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DefensiveOverviewStatsResponse:
        r"""Get Defensive Player Overview Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveOverviewStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            team_defense=team_defense,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/overview/season",
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
                "getDefensiveOverviewStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.DefensiveOverviewStatsResponse, STATS_ERROR_CODES
        )

    async def get_weekly_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensiveOverviewStatsBySeasonSortKey] = "snap",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        team_defense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DefensiveOverviewStatsResponse:
        r"""Get Defensive Player Overview Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveOverviewStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            team_defense=team_defense,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/overview/season",
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
                "getDefensiveOverviewStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.DefensiveOverviewStatsResponse, STATS_ERROR_CODES
        )

    def get_season_pass_rush_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensivePassRushStatsBySeasonSortKey] = "pr",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PassRushStatsResponse:
        r"""Get Defensive Pass Rush Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensivePassRushStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/passRush/season",
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
                "getDefensivePassRushStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.PassRushStatsResponse, STATS_ERROR_CODES
        )

    async def get_season_pass_rush_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensivePassRushStatsBySeasonSortKey] = "pr",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PassRushStatsResponse:
        r"""Get Defensive Pass Rush Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensivePassRushStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/passRush/season",
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
                "getDefensivePassRushStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.PassRushStatsResponse, STATS_ERROR_CODES
        )

    def get_weekly_pass_rush_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensivePassRushStatsBySeasonSortKey] = "pr",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PassRushStatsResponse:
        r"""Get Defensive Pass Rush Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensivePassRushStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/passRush/week",
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
                "getDefensivePassRushStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.PassRushStatsResponse, STATS_ERROR_CODES
        )

    async def get_weekly_pass_rush_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetDefensivePassRushStatsBySeasonSortKey] = "pr",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PassRushStatsResponse:
        r"""Get Defensive Pass Rush Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensivePassRushStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/passRush/season",
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
                "getDefensivePassRushStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.PassRushStatsResponse, STATS_ERROR_CODES
        )

    def get_season_nearest_defender_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "cov",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Defensive Nearest Defender Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveNearestDefenderStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/nearest/season",
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
                "getDefensiveNearestDefenderStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(http_res, dict, STATS_ERROR_CODES)

    async def get_season_nearest_defender_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "cov",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Defensive Nearest Defender Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveNearestDefenderStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/nearest/season",
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
                "getDefensiveNearestDefenderStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(http_res, dict, STATS_ERROR_CODES)

    def get_weekly_nearest_defender_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "cov",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Defensive Nearest Defender Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveNearestDefenderStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/defense/nearest/week",
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
                "getDefensiveNearestDefenderStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(http_res, dict, STATS_ERROR_CODES)

    async def get_weekly_nearest_defender_summary_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "cov",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Defensive Nearest Defender Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetDefensiveNearestDefenderStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/defense/nearest/week",
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
                "getDefensiveNearestDefenderStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=STATS_ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(http_res, dict, STATS_ERROR_CODES)
