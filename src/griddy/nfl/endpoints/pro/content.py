from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.mixins import GameContentMixin
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class Content(ProSDK, GameContentMixin):
    def get_home_film_cards(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HomeFilmCardsResponse:
        r"""Get Home Film Cards

        Retrieves featured film room content cards for the home page.
        Returns weekly playlists and featured player film breakdowns.


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
        req = self._build_request(
            method="GET",
            path="/api/content/home-film-cards",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
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
                operation_id="getHomeFilmCards",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.HomeFilmCardsResponse, http_res)
        if utils.match_response(http_res, ["401", "4XX"], "*"):
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

    async def get_home_film_cards_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.HomeFilmCardsResponse:
        r"""Get Home Film Cards

        Retrieves featured film room content cards for the home page.
        Returns weekly playlists and featured player film breakdowns.


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
        req = self._build_request_async(
            method="GET",
            path="/api/content/home-film-cards",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
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
                operation_id="getHomeFilmCards",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.HomeFilmCardsResponse, http_res)
        if utils.match_response(http_res, ["401", "4XX"], "*"):
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

    def get_season_insights(
        self,
        *,
        season: int,
        limit: Optional[int] = 20,
        tags: Optional[List[models.Tag]] = None,
        team_id: Optional[str] = None,
        nfl_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.Insight]:
        r"""Get Season Content Insights

        Retrieves curated editorial insights and analytics content for NFL players during
        a specified season. Returns expert commentary combining Next Gen Stats data with
        editorial analysis, including pregame previews, postgame breakdowns, fantasy insights,
        and evergreen content. Supports filtering by player, team, content tags, and publication
        limits for targeted content discovery.


        :param season: Season year
        :param limit: Maximum number of insights to return
        :param tags: Content tags to filter by (supports multiple comma-separated tags)
        :param team_id: Filter by specific team identifier
        :param nfl_id: Filter by specific player NFL identifier
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

        request = models.GetSeasonContentInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            team_id=team_id,
            nfl_id=nfl_id,
        )

        req = self._build_request(
            method="GET",
            path="/api/content/insights/season",
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
                operation_id="getSeasonContentInsights",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            # TODO: unmarshal is borked. Fix pydantic model
            # return unmarshal_json_response(List[models.Insight], http_res)
            return http_res.json()
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
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

    async def get_season_insights_async(
        self,
        *,
        season: int,
        limit: Optional[int] = 20,
        tags: Optional[List[models.Tag]] = None,
        team_id: Optional[str] = None,
        nfl_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.Insight]:
        r"""Get Season Content Insights

        Retrieves curated editorial insights and analytics content for NFL players during
        a specified season. Returns expert commentary combining Next Gen Stats data with
        editorial analysis, including pregame previews, postgame breakdowns, fantasy insights,
        and evergreen content. Supports filtering by player, team, content tags, and publication
        limits for targeted content discovery.


        :param season: Season year
        :param limit: Maximum number of insights to return
        :param tags: Content tags to filter by (supports multiple comma-separated tags)
        :param team_id: Filter by specific team identifier
        :param nfl_id: Filter by specific player NFL identifier
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

        request = models.GetSeasonContentInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            team_id=team_id,
            nfl_id=nfl_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/content/insights/season",
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
                operation_id="getSeasonContentInsights",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(List[models.Insight], http_res)
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
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

    # TODO: Consider how this method signature might be cleaned up
    def get_filmroom_plays(
        self,
        *,
        game_id: Optional[List[str]] = None,
        week_slug: Optional[List[models.WeekSlugEnum]] = None,
        season: Optional[List[int]] = None,
        season_type: Optional[List[models.SeasonTypeEnum]] = None,
        nfl_id: Optional[List[str]] = None,
        quarter: Optional[List[int]] = None,
        down: Optional[List[int]] = None,
        yards_to_go_type: Optional[List[models.YardsToGoType]] = None,
        touchdown: Optional[List[models.BinaryFlagEnum]] = None,
        rush10_plus_yards: Optional[List[models.BinaryFlagEnum]] = None,
        fumble_lost: Optional[List[models.BinaryFlagEnum]] = None,
        fumble: Optional[List[models.BinaryFlagEnum]] = None,
        qb_alignment: Optional[List[models.QbAlignment]] = None,
        redzone: Optional[List[models.BinaryFlagEnum]] = None,
        goal_to_go: Optional[List[models.BinaryFlagEnum]] = None,
        pass_play: Optional[List[models.BinaryFlagEnum]] = None,
        run_play: Optional[List[models.BinaryFlagEnum]] = None,
        play_type: Optional[List[models.PlayTypeEnum]] = None,
        attempt: Optional[List[models.BinaryFlagEnum]] = None,
        completion: Optional[List[models.BinaryFlagEnum]] = None,
        interception: Optional[List[models.BinaryFlagEnum]] = None,
        reception: Optional[List[models.BinaryFlagEnum]] = None,
        sack: Optional[List[models.BinaryFlagEnum]] = None,
        rec_motion: Optional[List[models.BinaryFlagEnum]] = None,
        target_location: Optional[List[models.TargetLocation]] = None,
        air_yard_type: Optional[List[models.AirYardType]] = None,
        dropback_time_type: Optional[List[models.DropbackTimeType]] = None,
        pressure: Optional[List[models.BinaryFlagEnum]] = None,
        blitz: Optional[List[models.BinaryFlagEnum]] = None,
        play_action: Optional[List[models.BinaryFlagEnum]] = None,
        rush_direction: Optional[List[models.RushDirection]] = None,
        run_stuff: Optional[List[models.BinaryFlagEnum]] = None,
        receiver_alignment: Optional[List[models.ReceiverAlignment]] = None,
        separation_type: Optional[List[models.SeparationType]] = None,
        personnel: Optional[List[models.Personnel]] = None,
        defenders_in_the_box_type: Optional[List[models.DefendersInTheBoxType]] = None,
        def_coverage_type: Optional[List[models.DefCoverageType]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FilmroomPlaysResponse:
        # TODO: Note that the actual video file itself is acquired by:
        # 1.) Extract the mcpPlaybackId of the game
        # 2.) Using it (and other stuff I've yet to dechipher the meaning of
        #       to send a POST request to https://api.nfl.com/play/v1/asset/<mcpPlaybackId>
        # This request will return a JSON response with:
        # accessUrl, init, and metadata fields
        r"""Get Filmroom Plays with Advanced Filtering

        Retrieves detailed play-by-play data with extensive filtering capabilities for film study.
        Returns comprehensive play information including formations, personnel packages, game situations,
        and detailed play descriptions. This endpoint supports advanced filtering by game situation,
        player involvement, formation types, and tactical elements.


        :param game_id: Filter by specific game IDs (supports multiple values)
        :param week_slug: Filter by week identifier (supports multiple values)
        :param season: Filter by season year (supports multiple values)
        :param season_type: Filter by season type
        :param nfl_id: Filter by player NFL ID
        :param quarter: Filter by quarter
        :param down: Filter by down
        :param yards_to_go_type: Filter by yards to go category
        :param touchdown: Filter for touchdown plays (1 = yes, 0 = no)
        :param rush10_plus_yards: Filter for rushing plays of 10+ yards
        :param fumble_lost: Filter for plays with fumbles lost
        :param fumble: Filter for plays with fumbles
        :param qb_alignment: Filter by quarterback alignment
        :param redzone: Filter for red zone plays
        :param goal_to_go: Filter for goal-to-go situations
        :param pass_play: Filter for passing plays
        :param run_play: Filter for running plays
        :param play_type: Filter by specific play types
        :param attempt: Filter for passing attempts
        :param completion: Filter for completed passes
        :param interception: Filter for interceptions
        :param reception: Filter for receptions
        :param sack: Filter for sacks
        :param rec_motion: Filter by receiver motion
        :param target_location: Filter by target location on field
        :param air_yard_type: Filter by air yards category
        :param dropback_time_type: Filter by dropback time
        :param pressure: Filter by quarterback pressure
        :param blitz: Filter by defensive blitz
        :param play_action: Filter by play action usage
        :param rush_direction: Filter by rush direction
        :param run_stuff: Filter for stuffed runs
        :param receiver_alignment: Filter by receiver alignment
        :param separation_type: Filter by receiver separation
        :param personnel: Filter by defensive personnel package
        :param defenders_in_the_box_type: Filter by defenders in the box
        :param def_coverage_type: Filter by defensive coverage type
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

        request = models.GetFilmroomPlaysRequest(
            game_id=game_id,
            week_slug=week_slug,
            season=season,
            season_type=season_type,
            nfl_id=nfl_id,
            quarter=quarter,
            down=down,
            yards_to_go_type=yards_to_go_type,
            touchdown=touchdown,
            rush10_plus_yards=rush10_plus_yards,
            fumble_lost=fumble_lost,
            fumble=fumble,
            qb_alignment=qb_alignment,
            redzone=redzone,
            goal_to_go=goal_to_go,
            pass_play=pass_play,
            run_play=run_play,
            play_type=play_type,
            attempt=attempt,
            completion=completion,
            interception=interception,
            reception=reception,
            sack=sack,
            rec_motion=rec_motion,
            target_location=target_location,
            air_yard_type=air_yard_type,
            dropback_time_type=dropback_time_type,
            pressure=pressure,
            blitz=blitz,
            play_action=play_action,
            rush_direction=rush_direction,
            run_stuff=run_stuff,
            receiver_alignment=receiver_alignment,
            separation_type=separation_type,
            personnel=personnel,
            defenders_in_the_box_type=defenders_in_the_box_type,
            def_coverage_type=def_coverage_type,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/videos/filmroom/plays",
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
                operation_id="getFilmroomPlays",
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
            return unmarshal_json_response(models.FilmroomPlaysResponse, http_res)
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

    async def get_filmroom_plays_async(
        self,
        *,
        game_id: Optional[List[str]] = None,
        week_slug: Optional[List[models.WeekSlugEnum]] = None,
        season: Optional[List[int]] = None,
        season_type: Optional[List[models.SeasonTypeEnum]] = None,
        nfl_id: Optional[List[str]] = None,
        quarter: Optional[List[int]] = None,
        down: Optional[List[int]] = None,
        yards_to_go_type: Optional[List[models.YardsToGoType]] = None,
        touchdown: Optional[List[models.BinaryFlagEnum]] = None,
        rush10_plus_yards: Optional[List[models.BinaryFlagEnum]] = None,
        fumble_lost: Optional[List[models.BinaryFlagEnum]] = None,
        fumble: Optional[List[models.BinaryFlagEnum]] = None,
        qb_alignment: Optional[List[models.QbAlignment]] = None,
        redzone: Optional[List[models.BinaryFlagEnum]] = None,
        goal_to_go: Optional[List[models.BinaryFlagEnum]] = None,
        pass_play: Optional[List[models.BinaryFlagEnum]] = None,
        run_play: Optional[List[models.BinaryFlagEnum]] = None,
        play_type: Optional[List[models.PlayTypeEnum]] = None,
        attempt: Optional[List[models.BinaryFlagEnum]] = None,
        completion: Optional[List[models.BinaryFlagEnum]] = None,
        interception: Optional[List[models.BinaryFlagEnum]] = None,
        reception: Optional[List[models.BinaryFlagEnum]] = None,
        sack: Optional[List[models.BinaryFlagEnum]] = None,
        rec_motion: Optional[List[models.BinaryFlagEnum]] = None,
        target_location: Optional[List[models.TargetLocation]] = None,
        air_yard_type: Optional[List[models.AirYardType]] = None,
        dropback_time_type: Optional[List[models.DropbackTimeType]] = None,
        pressure: Optional[List[models.BinaryFlagEnum]] = None,
        blitz: Optional[List[models.BinaryFlagEnum]] = None,
        play_action: Optional[List[models.BinaryFlagEnum]] = None,
        rush_direction: Optional[List[models.RushDirection]] = None,
        run_stuff: Optional[List[models.BinaryFlagEnum]] = None,
        receiver_alignment: Optional[List[models.ReceiverAlignment]] = None,
        separation_type: Optional[List[models.SeparationType]] = None,
        personnel: Optional[List[models.Personnel]] = None,
        defenders_in_the_box_type: Optional[List[models.DefendersInTheBoxType]] = None,
        def_coverage_type: Optional[List[models.DefCoverageType]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FilmroomPlaysResponse:
        r"""Get Filmroom Plays with Advanced Filtering

        Retrieves detailed play-by-play data with extensive filtering capabilities for film study.
        Returns comprehensive play information including formations, personnel packages, game situations,
        and detailed play descriptions. This endpoint supports advanced filtering by game situation,
        player involvement, formation types, and tactical elements.


        :param game_id: Filter by specific game IDs (supports multiple values)
        :param week_slug: Filter by week identifier (supports multiple values)
        :param season: Filter by season year (supports multiple values)
        :param season_type: Filter by season type
        :param nfl_id: Filter by player NFL ID
        :param quarter: Filter by quarter
        :param down: Filter by down
        :param yards_to_go_type: Filter by yards to go category
        :param touchdown: Filter for touchdown plays (1 = yes, 0 = no)
        :param rush10_plus_yards: Filter for rushing plays of 10+ yards
        :param fumble_lost: Filter for plays with fumbles lost
        :param fumble: Filter for plays with fumbles
        :param qb_alignment: Filter by quarterback alignment
        :param redzone: Filter for red zone plays
        :param goal_to_go: Filter for goal-to-go situations
        :param pass_play: Filter for passing plays
        :param run_play: Filter for running plays
        :param play_type: Filter by specific play types
        :param attempt: Filter for passing attempts
        :param completion: Filter for completed passes
        :param interception: Filter for interceptions
        :param reception: Filter for receptions
        :param sack: Filter for sacks
        :param rec_motion: Filter by receiver motion
        :param target_location: Filter by target location on field
        :param air_yard_type: Filter by air yards category
        :param dropback_time_type: Filter by dropback time
        :param pressure: Filter by quarterback pressure
        :param blitz: Filter by defensive blitz
        :param play_action: Filter by play action usage
        :param rush_direction: Filter by rush direction
        :param run_stuff: Filter for stuffed runs
        :param receiver_alignment: Filter by receiver alignment
        :param separation_type: Filter by receiver separation
        :param personnel: Filter by defensive personnel package
        :param defenders_in_the_box_type: Filter by defenders in the box
        :param def_coverage_type: Filter by defensive coverage type
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

        request = models.GetFilmroomPlaysRequest(
            game_id=game_id,
            week_slug=week_slug,
            season=season,
            season_type=season_type,
            nfl_id=nfl_id,
            quarter=quarter,
            down=down,
            yards_to_go_type=yards_to_go_type,
            touchdown=touchdown,
            rush10_plus_yards=rush10_plus_yards,
            fumble_lost=fumble_lost,
            fumble=fumble,
            qb_alignment=qb_alignment,
            redzone=redzone,
            goal_to_go=goal_to_go,
            pass_play=pass_play,
            run_play=run_play,
            play_type=play_type,
            attempt=attempt,
            completion=completion,
            interception=interception,
            reception=reception,
            sack=sack,
            rec_motion=rec_motion,
            target_location=target_location,
            air_yard_type=air_yard_type,
            dropback_time_type=dropback_time_type,
            pressure=pressure,
            blitz=blitz,
            play_action=play_action,
            rush_direction=rush_direction,
            run_stuff=run_stuff,
            receiver_alignment=receiver_alignment,
            separation_type=separation_type,
            personnel=personnel,
            defenders_in_the_box_type=defenders_in_the_box_type,
            def_coverage_type=def_coverage_type,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/videos/filmroom/plays",
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
                operation_id="getFilmroomPlays",
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
            return unmarshal_json_response(models.FilmroomPlaysResponse, http_res)
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

    def get_coaches_film_videos(
        self,
        *,
        game_id: List[str],
        play_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CoachesFilmResponse:
        # TODO: Note that the game_id used in this request
        # corresponds to the Game's UUID often labeled fapi_game_id by the NFL.
        # Why is it different? Nobody knows
        r"""Get Coaches Film Videos

        Retrieves premium coaches film video content for specified games and plays.
        Returns multiple camera angles (endzone, sideline, broadcast) for each play,
        providing comprehensive film study material. Requires NFL Plus Premium subscription
        and appropriate geographic restrictions apply (US only).


        :param game_id: Game identifiers (UUID format, supports multiple games)
        :param play_id: Play identifiers for specific plays within the games
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

        request = models.GetCoachesFilmVideosRequest(
            game_id=game_id,
            play_id=play_id,
        )

        req = self._build_request(
            method="GET",
            path="/api/secured/videos/coaches",
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
                operation_id="getCoachesFilmVideos",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.CoachesFilmResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "403", "404", "4XX"], "*"):
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

    async def get_coaches_film_videos_async(
        self,
        *,
        game_id: List[str],
        play_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CoachesFilmResponse:
        r"""Get Coaches Film Videos

        Retrieves premium coaches film video content for specified games and plays.
        Returns multiple camera angles (endzone, sideline, broadcast) for each play,
        providing comprehensive film study material. Requires NFL Plus Premium subscription
        and appropriate geographic restrictions apply (US only).


        :param game_id: Game identifiers (UUID format, supports multiple games)
        :param play_id: Play identifiers for specific plays within the games
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

        request = models.GetCoachesFilmVideosRequest(
            game_id=game_id,
            play_id=play_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/secured/videos/coaches",
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
                operation_id="getCoachesFilmVideos",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.CoachesFilmResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "403", "404", "4XX"], "*"):
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
