from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable

# TODO: All the requests in this file have broken Pydantic models


class TeamDefenseStats(ProSDK):
    _ERROR_CODES = ["400", "401", "403", "4XX", "500", "5XX"]

    def get_season_overview(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefenseStatsBySeasonSortKey] = "ypg",
        sort_value: Optional[models.SortOrderEnum] = None,
        split: Optional[List[models.GetTeamDefenseStatsBySeasonSplit]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseStatsResponse:
        r"""Get Team Defense Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/overview/season",
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
            hook_ctx=self._create_hook_context("getTeamDefenseStatsBySeason", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefenseStatsResponse, self._ERROR_CODES
        )

    async def get_season_overview_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefenseStatsBySeasonSortKey] = "ypg",
        sort_value: Optional[models.SortOrderEnum] = None,
        split: Optional[List[models.GetTeamDefenseStatsBySeasonSplit]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseStatsResponse:
        r"""Get Team Defense Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/overview/season",
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
            hook_ctx=self._create_hook_context("getTeamDefenseStatsBySeason", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefenseStatsResponse, self._ERROR_CODES
        )

    def get_weekly_overview(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefenseStatsBySeasonSortKey] = "ypg",
        sort_value: Optional[models.SortOrderEnum] = None,
        split: Optional[List[models.GetTeamDefenseStatsBySeasonSplit]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseStatsResponse:
        r"""Get Team Defense Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/overview/week",
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
            hook_ctx=self._create_hook_context("getTeamDefenseStatsByWeek", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefenseStatsResponse, self._ERROR_CODES
        )

    async def get_weekly_overview_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefenseStatsBySeasonSortKey] = "ypg",
        sort_value: Optional[models.SortOrderEnum] = None,
        split: Optional[List[models.GetTeamDefenseStatsBySeasonSplit]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseStatsResponse:
        r"""Get Team Defense Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/overview/week",
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
            hook_ctx=self._create_hook_context("getTeamDefenseStatsByWeek", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefenseStatsResponse, self._ERROR_CODES
        )

    def get_season_pass_stats(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefensePassStatsBySeasonSortKey] = "passYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefensePassStatsResponse:
        r"""Get Team Defense Pass Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefensePassStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/pass/season",
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
                "getTeamDefensePassStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefensePassStatsResponse, self._ERROR_CODES
        )

    async def get_season_pass_stats_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefensePassStatsBySeasonSortKey] = "passYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefensePassStatsResponse:
        r"""Get Team Defense Pass Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefensePassStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/pass/season",
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
                "getTeamDefensePassStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefensePassStatsResponse, self._ERROR_CODES
        )

    def get_weekly_pass_stats(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefensePassStatsBySeasonSortKey] = "passYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefensePassStatsResponse:
        r"""Get Team Defense Pass Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefensePassStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/pass/week",
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
                "getTeamDefensePassStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefensePassStatsResponse, self._ERROR_CODES
        )

    async def get_weekly_pass_stats_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetTeamDefensePassStatsBySeasonSortKey] = "passYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefensePassStatsResponse:
        r"""Get Team Defense Pass Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefensePassStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/pass/week",
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
                "getTeamDefensePassStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefensePassStatsResponse, self._ERROR_CODES
        )

    def get_season_rush_stats(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "rushYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseRushStatsResponse:
        r"""Get Team Defense Rush Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseRushStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/rush/season",
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
                "getTeamDefenseRushStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefenseRushStatsResponse, self._ERROR_CODES
        )

    async def get_season_rush_stats_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "rushYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseRushStatsResponse:
        r"""Get Team Defense Rush Statistics by Season"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseRushStatsBySeasonRequest(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/rush/season",
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
                "getTeamDefenseRushStatsBySeason", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefenseRushStatsResponse, self._ERROR_CODES
        )

    def get_weekly_rush_stats(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "rushYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseRushStatsResponse:
        r"""Get Team Defense Rush Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseRushStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/team-defense/rush/week",
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
                "getTeamDefenseRushStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return self._handle_json_response(
            http_res, models.TeamDefenseRushStatsResponse, self._ERROR_CODES
        )

    async def get_weekly_rush_stats_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[str] = "rushYpg",
        sort_value: Optional[models.SortOrderEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamDefenseRushStatsResponse:
        r"""Get Team Defense Rush Statistics by Week"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetTeamDefenseRushStatsByWeekRequest(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/team-defense/rush/week",
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
                "getTeamDefenseRushStatsByWeek", base_url
            ),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return http_res.json()
        return await self._handle_json_response_async(
            http_res, models.TeamDefenseRushStatsResponse, self._ERROR_CODES
        )
