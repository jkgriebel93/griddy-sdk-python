from typing import Mapping, Optional

from griddy.core._constants import RESOURCE_ERROR_CODES
from griddy.core.decorators import sdk_endpoints
from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


@sdk_endpoints
class VideoContent(BaseSDK):
    r"""Video content endpoints for game replays."""

    def _get_video_replays_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        r"""Get Video Replays

        Retrieves video replay content for a specific game.

        Args:
            game_id: Game identifier (UUID)
            retries: Override the default retry configuration for this method
            server_url: Override the default server URL for this method
            timeout_ms: Override the default request timeout configuration for this method in milliseconds
            http_headers: Additional headers to set or replace on requests.
        """
        request = models.GetVideoReplaysRequest(
            game_id=game_id,
        )

        return EndpointConfig(
            method="GET",
            path="/content/v1/videos/replays",
            operation_id="getVideoReplays",
            request=request,
            response_type=models.VideoReplaysResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )
