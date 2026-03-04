from typing import List, Mapping, Optional

from griddy.core.decorators import sdk_endpoints
from griddy.nfl import models, utils
from griddy.nfl.endpoints.pro.stats.base import PlayerStatsBase
from griddy.nfl.types import UNSET, OptionalNullable


@sdk_endpoints
class PlayerDefenseStats(PlayerStatsBase):

    def _get_season_summary_config(
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
    ):
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
        return self._make_stats_config(
            "/api/secured/stats/defense/overview/season",
            "getDefensiveOverviewStatsBySeason",
            models.GetDefensiveOverviewStatsBySeasonRequest,
            models.DefensiveOverviewStatsResponse,
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            team_defense=team_defense,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_weekly_summary_config(
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
    ):
        r"""Get Defensive Player Overview Statistics by Week"""
        return self._make_stats_config(
            "/api/secured/stats/defense/overview/season",
            "getDefensiveOverviewStatsBySeason",
            models.GetDefensiveOverviewStatsByWeekRequest,
            models.DefensiveOverviewStatsResponse,
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
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_season_pass_rush_summary_config(
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
    ):
        r"""Get Defensive Pass Rush Statistics by Season"""
        return self._make_stats_config(
            "/api/secured/stats/defense/passRush/season",
            "getDefensivePassRushStatsBySeason",
            models.GetDefensivePassRushStatsBySeasonRequest,
            models.PassRushStatsResponse,
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_weekly_pass_rush_summary_config(
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
    ):
        r"""Get Defensive Pass Rush Statistics by Week"""
        return self._make_stats_config(
            "/api/secured/stats/defense/passRush/week",
            "getDefensivePassRushStatsByWeek",
            models.GetDefensivePassRushStatsByWeekRequest,
            models.PassRushStatsResponse,
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_season_nearest_defender_summary_config(
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
        return self._make_stats_config(
            "/api/secured/stats/defense/nearest/season",
            "getDefensiveNearestDefenderStatsBySeason",
            models.GetDefensiveNearestDefenderStatsBySeasonRequest,
            models.NearestDefenderStatsResponse,
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_weekly_nearest_defender_summary_config(
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
        return self._make_stats_config(
            "/api/secured/stats/defense/nearest/week",
            "getDefensiveNearestDefenderStatsByWeek",
            models.GetDefensiveNearestDefenderStatsByWeekRequest,
            models.NearestDefenderStatsResponse,
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_defender=qualified_defender,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
