from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class Injuries(BaseSDK):

    def _get_injury_reports_config(
        self,
        *,
        season: int,
        week: int,
        team_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetInjuryReportsRequest(
            season=season,
            week=week,
            team_id=team_id,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/injuries",
            operation_id="getInjuryReports",
            request=request,
            response_type=models.InjuryReportResponse,
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

    def get_injury_reports(
        self,
        *,
        season: int,
        week: int,
        team_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        # TODO: This endpoint resolves (i.e. not a 404)
        # but returns no data
        r"""Get Injury Reports

        Retrieves current injury reports for all teams or specific teams
        with injury status, designation, and practice participation.


        :param season: Season year
        :param week: Week number
        :param team_id: Filter by specific team
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_injury_reports_config(
            season=season,
            week=week,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_injury_reports_async(
        self,
        *,
        season: int,
        week: int,
        team_id: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        r"""Get Injury Reports"""
        config = self._get_injury_reports_config(
            season=season,
            week=week,
            team_id=team_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
