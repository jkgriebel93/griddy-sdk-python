from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import RESOURCE_ERROR_CODES
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class Combine(BaseSDK):

    def _get_profiles_config(
        self,
        *,
        year: int,
        limit: int = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetCombineProfilesRequest(year=year, limit=limit)

        return EndpointConfig(
            method="GET",
            path="/football/v2/combine/profiles",
            operation_id="getCombineProfiles",
            request=request,
            response_type=models.CombineProfilesResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_profiles(
        self,
        *,
        year: int,
        limit: int = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CombineProfilesResponse:
        r"""Get Combine Profiles

        :param year: Draft year
        :param limit: Maximum number of combine profiles to return
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_profiles_config(
            year=year,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_profiles_async(
        self,
        *,
        year: int,
        limit: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CombineProfilesResponse:
        r"""Get Combine Profiles"""
        # Note: sync version has limit=1000, async has limit=None - keeping original behavior
        config = self._get_profiles_config(
            year=year,
            limit=limit if limit is not None else 1000,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_rankings_config(
        self,
        *,
        rank_attribute: models.EventFilterEnum,
        sort_order: models.SortOrderEnum,
        year: int,
        limit: int = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetCombineRankingsRequest(
            rank_attribute=rank_attribute,
            sort_order=sort_order,
            year=year,
            limit=limit,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/combine/rankings",
            operation_id="getCombineRankings",
            request=request,
            response_type=models.CombineRankingsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_rankings(
        self,
        *,
        rank_attribute: models.EventFilterEnum,
        sort_order: models.SortOrderEnum,
        year: int,
        limit: int = 1000,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CombineRankingsResponse:
        r"""Get Combine Rankings

        :param rank_attribute: Attribute to rank by
        :param sort_order: Sort order
        :param year: Draft year
        :param limit: Maximum number of combine profiles to return
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_rankings_config(
            rank_attribute=rank_attribute,
            sort_order=sort_order,
            year=year,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_rankings_async(
        self,
        *,
        rank_attribute: models.EventFilterEnum,
        sort_order: models.SortOrderEnum,
        year: int,
        limit: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CombineRankingsResponse:
        r"""Get Combine Rankings"""
        # Note: sync version has limit=1000, async has limit=None - keeping original behavior
        config = self._get_rankings_config(
            rank_attribute=rank_attribute,
            sort_order=sort_order,
            year=year,
            limit=limit if limit is not None else 1000,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
