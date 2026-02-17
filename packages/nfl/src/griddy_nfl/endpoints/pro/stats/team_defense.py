from typing import List, Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import STATS_ERROR_CODES
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.pro import ProSDK
from griddy_nfl.types import UNSET, OptionalNullable


class TeamDefenseStats(ProSDK):

    def _get_season_overview_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/overview/season",
            operation_id="getTeamDefenseStatsBySeason",
            request=models.GetTeamDefenseStatsBySeasonRequest(
                season=season,
                season_type=season_type,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
                split=split,
            ),
            response_type=models.TeamDefenseStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )

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
        config = self._get_season_overview_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_season_overview_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_weekly_overview_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/overview/week",
            operation_id="getTeamDefenseStatsByWeek",
            request=models.GetTeamDefenseStatsByWeekRequest(
                season=season,
                season_type=season_type,
                week=week,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
                split=split,
            ),
            response_type=models.TeamDefenseStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_weekly_overview_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_weekly_overview_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            split=split,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_season_pass_stats_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/pass/season",
            operation_id="getTeamDefensePassStatsBySeason",
            request=models.GetTeamDefensePassStatsBySeasonRequest(
                season=season,
                season_type=season_type,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
            ),
            response_type=models.TeamDefensePassStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_season_pass_stats_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_season_pass_stats_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_weekly_pass_stats_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/pass/week",
            operation_id="getTeamDefensePassStatsByWeek",
            request=models.GetTeamDefensePassStatsByWeekRequest(
                season=season,
                season_type=season_type,
                week=week,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
            ),
            response_type=models.TeamDefensePassStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_weekly_pass_stats_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_weekly_pass_stats_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_season_rush_stats_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/rush/season",
            operation_id="getTeamDefenseRushStatsBySeason",
            request=models.GetTeamDefenseRushStatsBySeasonRequest(
                season=season,
                season_type=season_type,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
            ),
            response_type=models.TeamDefenseRushStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_season_rush_stats_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_season_rush_stats_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_weekly_rush_stats_config(
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
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/team-defense/rush/week",
            operation_id="getTeamDefenseRushStatsByWeek",
            request=models.GetTeamDefenseRushStatsByWeekRequest(
                season=season,
                season_type=season_type,
                week=week,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
            ),
            response_type=models.TeamDefenseRushStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
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
        config = self._get_weekly_rush_stats_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

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
        config = self._get_weekly_rush_stats_config(
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
