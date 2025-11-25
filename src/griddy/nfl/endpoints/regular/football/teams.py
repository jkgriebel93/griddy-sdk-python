from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.types import UNSET, OptionalNullable


class Teams(BaseSDK):
    _ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]

    def get_teams(
        self,
        *,
        season: int,
        limit: Optional[int] = 32,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballTeamsResponse:
        r"""Get Teams

        Retrieves teams

        :param season: Season year
        :param limit: Maximum number of results to return
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballTeamsRequest(
            season=season,
            limit=limit,
        )

        req = self._build_request(
            method="GET",
            path="/football/v2/teams",
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
            hook_ctx=self._create_hook_context("getFootballTeams", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, models.FootballTeamsResponse, self._ERROR_CODES
        )

    async def get_teams_async(
        self,
        *,
        season: int,
        limit: Optional[int] = 32,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballTeamsResponse:
        r"""Get Teams"""
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetFootballTeamsRequest(
            season=season,
            limit=limit,
        )

        req = self._build_request_async(
            method="GET",
            path="/football/v2/teams",
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
            hook_ctx=self._create_hook_context("getFootballTeams", base_url),
            request=req,
            error_status_codes=self._ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.FootballTeamsResponse, self._ERROR_CODES
        )
