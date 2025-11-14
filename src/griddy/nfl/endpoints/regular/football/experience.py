from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class Experience(BaseSDK):
    def get_weekly_game_details(
        self,
        *,
        season: int,
        type_: models.SeasonTypeEnum,
        week: int,
        include_drive_chart: Optional[bool] = False,
        include_replays: Optional[bool] = False,
        include_standings: Optional[bool] = False,
        include_tagged_videos: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.WeeklyGameDetail]:
        r"""Get Weekly Game Details

        Retrieves detailed game information for a specific week including team standings,
        drive charts, replays, and tagged videos.


        :param season: Season year
        :param type_: Season type
        :param week: Week number
        :param include_drive_chart: Include drive chart data
        :param include_replays: Include replay videos
        :param include_standings: Include team standings
        :param include_tagged_videos: Include tagged video content
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

        request = models.GetWeeklyGameDetailsRequest(
            season=season,
            type=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/experience/weekly-game-details",
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
                operation_id="getWeeklyGameDetails",
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
            # return unmarshal_json_response(List[models.WeeklyGameDetail], http_res)
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

    async def get_weekly_game_details_async(
        self,
        *,
        season: int,
        type_: models.SeasonTypeEnum,
        week: int,
        include_drive_chart: Optional[bool] = False,
        include_replays: Optional[bool] = False,
        include_standings: Optional[bool] = False,
        include_tagged_videos: Optional[bool] = False,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.WeeklyGameDetail]:
        r"""Get Weekly Game Details with Standings

        Retrieves detailed game information for a specific week including team standings,
        drive charts, replays, and tagged videos.


        :param season: Season year
        :param type: Season type
        :param week: Week number
        :param include_drive_chart: Include drive chart data
        :param include_replays: Include replay videos
        :param include_standings: Include team standings
        :param include_tagged_videos: Include tagged video content
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

        request = models.GetWeeklyGameDetailsRequest(
            season=season,
            type=type_,
            week=week,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
        )

        req = self._build_request_async(
            method="GET",
            path="/football/v2/experience/weekly-game-details",
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
                operation_id="getWeeklyGameDetails",
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
            return unmarshal_json_response(List[models.WeeklyGameDetail], http_res)
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
