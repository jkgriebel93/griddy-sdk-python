from typing import List, Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import STATS_ERROR_CODES
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.pro import ProSDK
from griddy_nfl.types import UNSET, OptionalNullable


class Fantasy(ProSDK):
    r"""Fantasy football player statistics and scoring metrics"""

    def _get_stats_by_season_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetFantasyStatsBySeasonSortKey] = "fpStd",
        sort_value: Optional[models.SortOrderEnum] = None,
        position_group: Optional[
            List[models.GetFantasyStatsBySeasonPositionGroup]
        ] = None,
        team_offense: Optional[str] = None,
        team_defense: Optional[str] = None,
        min_offensive_snaps: Optional[int] = 0,
        last_n_weeks: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        return EndpointConfig(
            method="GET",
            path="/api/secured/stats/fantasy/season",
            operation_id="getFantasyStatsBySeason",
            request=models.GetFantasyStatsBySeasonRequest(
                season=season,
                season_type=season_type,
                limit=limit,
                offset=offset,
                page=page,
                sort_key=sort_key,
                sort_value=sort_value,
                position_group=position_group,
                team_offense=team_offense,
                team_defense=team_defense,
                min_offensive_snaps=min_offensive_snaps,
                last_n_weeks=last_n_weeks,
            ),
            response_type=models.FantasyStatsResponse,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )

    def get_stats_by_season(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetFantasyStatsBySeasonSortKey] = "fpStd",
        sort_value: Optional[models.SortOrderEnum] = None,
        position_group: Optional[
            List[models.GetFantasyStatsBySeasonPositionGroup]
        ] = None,
        team_offense: Optional[str] = None,
        team_defense: Optional[str] = None,
        min_offensive_snaps: Optional[int] = 0,
        last_n_weeks: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FantasyStatsResponse:
        r"""Get Fantasy Football Statistics by Season

        Retrieves comprehensive fantasy football statistics for NFL players during a specified season.
        Returns fantasy-relevant metrics including standard scoring, PPR scoring, snap counts, and
        target share data. Supports filtering by position groups (QB, RB, WR, TE, SPEC), teams,
        minimum offensive snap thresholds, and rolling N-week windows for recent performance analysis.
        Data includes traditional fantasy categories and advanced metrics for lineup optimization.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param position_group: Filter by position groups (supports multiple positions)
        :param team_offense: Filter by specific offensive team ID
        :param team_defense: Filter by specific defensive team ID (opponent analysis)
        :param min_offensive_snaps: Minimum offensive snaps threshold for inclusion
        :param last_n_weeks: Number of recent weeks to analyze (rolling window)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_stats_by_season_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            position_group=position_group,
            team_offense=team_offense,
            team_defense=team_defense,
            min_offensive_snaps=min_offensive_snaps,
            last_n_weeks=last_n_weeks,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_stats_by_season_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[models.GetFantasyStatsBySeasonSortKey] = "fpStd",
        sort_value: Optional[models.SortOrderEnum] = None,
        position_group: Optional[
            List[models.GetFantasyStatsBySeasonPositionGroup]
        ] = None,
        team_offense: Optional[str] = None,
        team_defense: Optional[str] = None,
        min_offensive_snaps: Optional[int] = 0,
        last_n_weeks: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FantasyStatsResponse:
        r"""Get Fantasy Football Statistics by Season

        Retrieves comprehensive fantasy football statistics for NFL players during a specified season.
        Returns fantasy-relevant metrics including standard scoring, PPR scoring, snap counts, and
        target share data. Supports filtering by position groups (QB, RB, WR, TE, SPEC), teams,
        minimum offensive snap thresholds, and rolling N-week windows for recent performance analysis.
        Data includes traditional fantasy categories and advanced metrics for lineup optimization.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param position_group: Filter by position groups (supports multiple positions)
        :param team_offense: Filter by specific offensive team ID
        :param team_defense: Filter by specific defensive team ID (opponent analysis)
        :param min_offensive_snaps: Minimum offensive snaps threshold for inclusion
        :param last_n_weeks: Number of recent weeks to analyze (rolling window)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_stats_by_season_config(
            season=season,
            season_type=season_type,
            limit=limit,
            offset=offset,
            page=page,
            sort_key=sort_key,
            sort_value=sort_value,
            position_group=position_group,
            team_offense=team_offense,
            team_defense=team_defense,
            min_offensive_snaps=min_offensive_snaps,
            last_n_weeks=last_n_weeks,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
