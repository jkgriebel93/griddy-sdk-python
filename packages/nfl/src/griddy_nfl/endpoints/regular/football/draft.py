from typing import Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import RESOURCE_ERROR_CODES
from griddy_nfl.basesdk import BaseSDK, EndpointConfig
from griddy_nfl.types import UNSET, OptionalNullable


class Draft(BaseSDK):

    def _get_picks_report_config(
        self,
        *,
        year: int,
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetDraftPicksReportRequest(year=year, limit=limit)

        return EndpointConfig(
            method="GET",
            path="/football/v2/draft/picks/report",
            operation_id="getDraftInfo",
            request=request,
            response_type=models.DraftResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )

    def get_picks_report(
        self,
        *,
        year: int,
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DraftResponse:
        r"""Get Draft Information

        Retrieves draft information for a specific year including all rounds,
        picks, traded picks, and compensatory selections.


        :param year: Draft year
        :param limit: Maximum number of picks to return
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_picks_report_config(
            year=year,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_picks_report_async(
        self,
        *,
        year: int,
        limit: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DraftResponse:
        r"""Get Draft Information"""
        # Note: sync version has limit=1000, async has limit=None - keeping original behavior
        config = self._get_picks_report_config(
            year=year,
            limit=limit if limit is not None else 1000,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_teamneeds_config(
        self,
        *,
        year: int,
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetTeamNeedsRequest(year=year, limit=limit)

        return EndpointConfig(
            method="GET",
            path="/football/v2/draft/teamneeds",
            operation_id="getTeamNeeds",
            request=request,
            response_type=models.TeamNeedsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_teamneeds(
        self,
        *,
        year: int,
        limit: Optional[int] = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamNeedsResponse:
        r"""Get Team Needs for Draft

        :param year: Draft year
        :param limit: Maximum number of results
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_teamneeds_config(
            year=year,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_teamneeds_async(
        self,
        *,
        year: int,
        limit: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.DraftResponse:
        r"""Get Team Needs for Draft"""
        # Note: sync version has limit=1000, async has limit=None - keeping original behavior
        config = self._get_teamneeds_config(
            year=year,
            limit=limit if limit is not None else 1000,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
