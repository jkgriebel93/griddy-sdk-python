from typing import Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import RESOURCE_ERROR_CODES
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class Experience(BaseSDK):

    def _get_game_details_by_slug_config(
        self,
        *,
        slug: str,
        include_replays: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetGameDetailsBySlugRequest(
            slug=slug,
            include_replays=include_replays,
        )

        return EndpointConfig(
            method="GET",
            path="/experience/v1/gamedetailsbyslug/{slug}",
            operation_id="getGameDetailsBySlug",
            request=request,
            response_type=models.WeeklyGameDetail,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_game_details_by_slug(
        self,
        *,
        slug: str,
        include_replays: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyGameDetail:
        r"""Get Game Details by Slug

        Retrieves detailed game information using a game slug identifier.
        Optionally includes replay videos. Returns the same shape as
        WeeklyGameDetail (the experience response is a subset of those fields).


        :param slug: Game slug identifier
        :param include_replays: Include replay videos in response
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_details_by_slug_config(
            slug=slug,
            include_replays=include_replays,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_game_details_by_slug_async(
        self,
        *,
        slug: str,
        include_replays: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyGameDetail:
        r"""Get Game Details by Slug"""
        config = self._get_game_details_by_slug_config(
            slug=slug,
            include_replays=include_replays,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_game_details_config(
        self,
        *,
        game_id: str,
        include_drive_chart: Optional[bool] = None,
        include_replays: Optional[bool] = None,
        include_standings: Optional[bool] = None,
        include_tagged_videos: Optional[bool] = None,
        include_summary: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        request = models.GetGameDetailsRequest(
            game_id=game_id,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
            include_summary=include_summary
        )

        return EndpointConfig(
            method="GET",
            path="/experience/v2/gamedetails/{gameId}",
            operation_id="getGameDetails",
            request=request,
            response_type=models.WeeklyGameDetail,
            error_status_codes=RESOURCE_ERROR_CODES,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_game_details(
        self,
        *,
        game_id: str,
        include_drive_chart: Optional[bool] = None,
        include_replays: Optional[bool] = None,
        include_standings: Optional[bool] = None,
        include_tagged_videos: Optional[bool] = None,
        include_summary: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyGameDetail:
        r"""Get Game Details

        Retrieves detailed game information by game ID. Supports optional
        inclusion of drive chart, replays, standings, and tagged videos.
        Returns the same shape as WeeklyGameDetail.


        :param game_id: Game identifier (UUID)
        :param include_drive_chart: Include drive chart data in response
        :param include_replays: Include replay videos in response
        :param include_standings: Include standings data in response
        :param include_tagged_videos: Include tagged videos in response
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_details_config(
            game_id=game_id,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
            include_summary=include_summary,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_game_details_async(
        self,
        *,
        game_id: str,
        include_drive_chart: Optional[bool] = None,
        include_replays: Optional[bool] = None,
        include_standings: Optional[bool] = None,
        include_tagged_videos: Optional[bool] = None,
        include_summary: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyGameDetail:
        r"""Get Game Details"""
        config = self._get_game_details_config(
            game_id=game_id,
            include_drive_chart=include_drive_chart,
            include_replays=include_replays,
            include_standings=include_standings,
            include_tagged_videos=include_tagged_videos,
            include_summary=include_summary,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
