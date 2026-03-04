from typing import List, Mapping, Optional

from griddy.core.decorators import sdk_endpoints
from griddy.nfl import models, utils
from griddy.nfl.endpoints.pro.stats.base import PlayerStatsBase
from griddy.nfl.types import UNSET, OptionalNullable


@sdk_endpoints
class PlayerPassingStats(PlayerStatsBase):

    def _get_weekly_summary_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: models.WeekSlugEnum,
        limit: Optional[int] = 50,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.PassingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_passer: Optional[bool] = False,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Player Passing Statistics by Week

        Retrieves comprehensive passing statistics for NFL players during a specified week and season.
        Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
        data. Supports filtering by teams, qualified passers, and various sorting options.


        :param season: Season year
        :param season_type: Type of season
        :param week: Week identifier
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_passer: Filter to only qualified passers (minimum attempts threshold)
        :param team_offense: Filter by specific team IDs (supports multiple teams)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        # TODO: It turns out the NFL includes both traditional and
        # Next Gen Stats on the same object. Pause to think about this for a minute.
        return self._make_stats_config(
            "/api/secured/stats/players-offense/passing/week",
            "getPlayerPassingStatsByWeek",
            models.GetPlayerPassingStatsByWeekRequest,
            models.WeeklyPassingStatsResponse,
            season=season,
            season_type=season_type,
            week=week,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_passer=qualified_passer,
            team_offense=team_offense,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def _get_season_summary_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.PassingStatsCategoryEnum] = None,
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_passer: Optional[bool] = True,
        team_offense: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Player Passing Statistics by Season

        Retrieves comprehensive passing statistics for NFL players during a specified season.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_passer: Filter to only qualified passers (minimum attempts threshold)
        :param team_offense: Filter by specific team IDs (supports multiple teams)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        return self._make_stats_config(
            "/api/secured/stats/players-offense/passing/season",
            "getPlayerPassingStatsBySeason",
            models.GetPlayerPassingStatsBySeasonRequest,
            models.PassingStatsResponse,
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            qualified_passer=qualified_passer,
            team_offense=team_offense,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
