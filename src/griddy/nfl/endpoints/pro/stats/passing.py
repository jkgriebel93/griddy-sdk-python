from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.endpoints.pro.stats import PlayerStats
from griddy.nfl.sdkconfiguration import SDKConfiguration
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class PlayerPassingStats(PlayerStats):
    def __init__(
        self, sdk_config: SDKConfiguration, parent_ref: Optional[object] = None
    ):
        super().__init__(
            category="passing", sdk_config=sdk_config, parent_ref=parent_ref
        )

    def get_player_passing_stats_week(
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
    ) -> models.WeeklyPassingStatsResponse:
        r"""Get Player Passing Statistics by Week

        Retrieves comprehensive passing statistics for NFL players during a specified week and season.
        Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
        data. Supports filtering by teams, qualified passers, and various sorting options.
        Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
        CPOE (Completion Percentage Over Expected), time to throw metrics, and game-specific context.


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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetPlayerPassingStatsByWeekRequest(
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
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/stats/players-offense/passing/week",
            base_url=base_url,
            url_variables=url_variables,
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

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getPlayerPassingStatsByWeek",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            # TODO: Another borked schema
            # return unmarshal_json_response(models.WeeklyPassingStatsResponse, http_res)
            return http_res.json()
        if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    async def get_player_passing_stats_week_async(
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
    ) -> models.WeeklyPassingStatsResponse:
        r"""Get Player Passing Statistics by Week

        Retrieves comprehensive passing statistics for NFL players during a specified week and season.
        Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
        data. Supports filtering by teams, qualified passers, and various sorting options.
        Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
        CPOE (Completion Percentage Over Expected), time to throw metrics, and game-specific context.


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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetPlayerPassingStatsByWeekRequest(
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
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/stats/players-offense/passing/week",
            base_url=base_url,
            url_variables=url_variables,
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

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="getPlayerPassingStatsByWeek",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.WeeklyPassingStatsResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
