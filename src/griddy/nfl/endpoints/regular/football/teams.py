from typing import Mapping, Optional

from griddy.core._constants import COLLECTION_ERROR_CODES
from griddy.core.decorators import sdk_endpoints
from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


@sdk_endpoints
class Teams(BaseSDK):
    def _get_teams_config(
        self,
        *,
        season: int,
        limit: Optional[int] = 32,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        r"""Get Teams

        Retrieves teams

        Args:
            season: Season year
            limit: Maximum number of results to return
            retries: Override the default retry configuration for this method
            server_url: Override the default server URL for this method
            timeout_ms: Override the default request timeout configuration for this method in milliseconds
            http_headers: Additional headers to set or replace on requests.
        """
        request = models.GetFootballTeamsRequest(
            season=season,
            limit=limit,
        )

        return EndpointConfig(
            method="GET",
            path="/football/v2/teams",
            operation_id="getFootballTeams",
            request=request,
            response_type=models.FootballTeamsResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
