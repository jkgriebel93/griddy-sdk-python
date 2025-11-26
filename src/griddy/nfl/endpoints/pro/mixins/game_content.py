from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES
from griddy.nfl.types import UNSET, OptionalNullable


class GameContentMixin:
    """Mixin for game content-related endpoints."""

    def get_game_preview(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        visitor_display_name: str,
        home_display_name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamePreviewResponse:
        r"""Get Game Preview Content

        Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param visitor_display_name: Visiting team display name
        :param home_display_name: Home team display name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamePreviewRequest(
            season=season,
            season_type=season_type,
            week=week,
            visitor_display_name=visitor_display_name,
            home_display_name=home_display_name,
        )

        req = self._build_request(
            method="GET",
            path="/api/content/game/preview",
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
            hook_ctx=self._create_hook_context("getGamePreview", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        # TODO: The model is busted, so unmarshaling returns an empty dict
        return self._handle_json_response(
            http_res, models.GamePreviewResponse, COLLECTION_ERROR_CODES
        )

    async def get_game_preview_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        visitor_display_name: str,
        home_display_name: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GamePreviewResponse:
        r"""Get Game Preview Content

        Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

        :param season: Season year
        :param season_type: Type of season
        :param week: Week number
        :param visitor_display_name: Visiting team display name
        :param home_display_name: Home team display name
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGamePreviewRequest(
            season=season,
            season_type=season_type,
            week=week,
            visitor_display_name=visitor_display_name,
            home_display_name=home_display_name,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/content/game/preview",
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
            hook_ctx=self._create_hook_context("getGamePreview", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, models.GamePreviewResponse, COLLECTION_ERROR_CODES
        )

    def get_game_insights(
        self,
        *,
        season: int,
        fapi_game_id: str,
        away_team_id: str,
        home_team_id: str,
        limit: Optional[int] = 20,
        tags: Optional[str] = None,
        exclude_tags: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.GameInsight]:
        r"""Get Game-Specific Insights

        Retrieves analytical insights and advanced statistics for a specific game.
        Can filter by tags and exclude specific content types.


        :param season: Season year
        :param fapi_game_id: FAPI Game identifier (UUID)
        :param away_team_id: Away team identifier
        :param home_team_id: Home team identifier
        :param limit: Maximum number of insights to return
        :param tags: Comma-separated list of tags to filter by
        :param exclude_tags: Comma-separated list of tags to exclude
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            exclude_tags=exclude_tags,
            fapi_game_id=fapi_game_id,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
        )

        req = self._build_request(
            method="GET",
            path="/api/content/insights/game",
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
            hook_ctx=self._create_hook_context("getGameInsights", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return self._handle_json_response(
            http_res, List[models.GameInsight], COLLECTION_ERROR_CODES
        )

    async def get_game_insights_async(
        self,
        *,
        season: int,
        fapi_game_id: str,
        away_team_id: str,
        home_team_id: str,
        limit: Optional[int] = 20,
        tags: Optional[str] = None,
        exclude_tags: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.GameInsight]:
        r"""Get Game-Specific Insights

        Retrieves analytical insights and advanced statistics for a specific game.
        Can filter by tags and exclude specific content types.


        :param season: Season year
        :param fapi_game_id: FAPI Game identifier (UUID)
        :param away_team_id: Away team identifier
        :param home_team_id: Home team identifier
        :param limit: Maximum number of insights to return
        :param tags: Comma-separated list of tags to filter by
        :param exclude_tags: Comma-separated list of tags to exclude
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = self._resolve_base_url(server_url)
        timeout_ms = self._resolve_timeout(timeout_ms)

        request = models.GetGameInsightsRequest(
            season=season,
            limit=limit,
            tags=tags,
            exclude_tags=exclude_tags,
            fapi_game_id=fapi_game_id,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
        )

        req = self._build_request_async(
            method="GET",
            path="/api/content/insights/game",
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
            hook_ctx=self._create_hook_context("getGameInsights", base_url),
            request=req,
            error_status_codes=COLLECTION_ERROR_CODES,
            retry_config=retry_config,
        )

        return await self._handle_json_response_async(
            http_res, List[models.GameInsight], COLLECTION_ERROR_CODES
        )
