from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class Rosters(BaseSDK):

    def _get_rosters_config(
        self,
        *,
        season: int,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetFootballRostersRequest(
            season=season,
            limit=limit,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/rosters",
            operation_id="getFootballRosters",
            request=request,
            response_type=models.FootballRostersResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_rosters(
        self,
        *,
        season: int,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballRostersResponse:
        r"""Get Rosters

        :param season: Season year
        :param limit: Maximum number of results to return
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_rosters_config(
            season=season,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_rosters_async(
        self,
        *,
        season: int,
        limit: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.FootballRostersResponse:
        r"""Get Rosters"""
        config = self._get_rosters_config(
            season=season,
            limit=limit,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
