from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response

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
        Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage
        metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced
        analytics. Supports filtering by qualified defenders, teams, and various sorting options.
        Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
        :param team_defense: Filter by specific team IDs (supports multiple teams)
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
                operation_id="getDefensiveOverviewStatsBySeason",
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
        r"""Get Defensive Player Overview Statistics by Season

        Retrieves comprehensive defensive overview statistics for NFL players during a specified season.
        Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage
        metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced
        analytics. Supports filtering by qualified defenders, teams, and various sorting options.
        Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
        :param team_defense: Filter by specific team IDs (supports multiple teams)
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
                operation_id="getDefensiveOverviewStatsBySeason",
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
            return http_res.json()
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
        r"""Get Defensive Player Overview Statistics by Season

        Retrieves comprehensive defensive overview statistics for NFL players during a specified season.
        Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage
        metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced
        analytics. Supports filtering by qualified defenders, teams, and various sorting options.
        Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
        :param team_defense: Filter by specific team IDs (supports multiple teams)
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
                operation_id="getDefensiveOverviewStatsBySeason",
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
        r"""Get Defensive Player Overview Statistics by Season

        Retrieves comprehensive defensive overview statistics for NFL players during a specified season.
        Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage
        metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced
        analytics. Supports filtering by qualified defenders, teams, and various sorting options.
        Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
        :param team_defense: Filter by specific team IDs (supports multiple teams)
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
                operation_id="getDefensiveOverviewStatsBySeason",
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
            return http_res.json()
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
        r"""Get Defensive Pass Rush Statistics by Season

        Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
        Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
        pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
        teams, and various sorting options. Data includes traditional pass rush stats and advanced
        analytics like pass rush grade, pressure rate, and time to sack metrics.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
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
                operation_id="getDefensivePassRushStatsBySeason",
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
        r"""Get Defensive Pass Rush Statistics by Season

        Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
        Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
        pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
        teams, and various sorting options. Data includes traditional pass rush stats and advanced
        analytics like pass rush grade, pressure rate, and time to sack metrics.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
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
                operation_id="getDefensivePassRushStatsBySeason",
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
            return http_res.json()
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
        r"""Get Defensive Pass Rush Statistics by Season

        Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
        Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
        pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
        teams, and various sorting options. Data includes traditional pass rush stats and advanced
        analytics like pass rush grade, pressure rate, and time to sack metrics.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
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
                operation_id="getDefensivePassRushStatsByWeek",
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
        r"""Get Defensive Pass Rush Statistics by Season

        Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
        Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
        pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
        teams, and various sorting options. Data includes traditional pass rush stats and advanced
        analytics like pass rush grade, pressure rate, and time to sack metrics.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
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
                operation_id="getDefensivePassRushStatsBySeason",
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
            return http_res.json()
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

    def get_season_nearest_defender_summary(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        limit: Optional[int] = 35,
        offset: Optional[int] = 0,
        page: Optional[int] = 1,
        sort_key: Optional[
            str
        ] = "cov",  # Optional[models.GetDefensiveNearestDefenderStatsBySeasonSortKey] = "pr",
        sort_value: Optional[models.SortOrderEnum] = None,
        qualified_defender: Optional[bool] = False,
        # game_location: Optional[models.GameLocationEnum] = models.GameLocationEnum.ALL,
        # quarter: Optional[models.QuarterEnum] = None,
        # down: Optional[models.DownEnum] = None,
        # yards_to_go: Optional[models.YardsToGoEnum] = None,
        # position_group: Optional[models.DefenseNGSPositionEnum] = None,
        # team_defense: Optional[int] = None,
        # team_offense: Optional[int] = None,
        # split: Optional[models.DefenseNGSSplitEnum] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Get Defensive Pass Rush Statistics by Season

        Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
        Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
        pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
        teams, and various sorting options. Data includes traditional pass rush stats and advanced
        analytics like pass rush grade, pressure rate, and time to sack metrics.


        :param season: Season year
        :param season_type: Type of season
        :param limit: Maximum number of players to return
        :param offset: Number of records to skip for pagination
        :param page: Page number for pagination
        :param sort_key: Field to sort by
        :param sort_value: Sort direction
        :param qualified_defender: Filter to only qualified defenders (minimum snap threshold)
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
                operation_id="getDefensiveNearestDefenderStatsBySeason",
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
