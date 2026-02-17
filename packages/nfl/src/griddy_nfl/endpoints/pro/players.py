from typing import List, Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.endpoints.pro import ProSDK
from griddy_nfl.types import UNSET, OptionalNullable


class Players(ProSDK):

    def _get_player_config(
        self,
        *,
        nfl_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_player."""
        return EndpointConfig(
            method="GET",
            path="/api/players/player",
            operation_id="getPlayer",
            request=models.GetPlayerRequest(nfl_id=nfl_id),
            response_type=models.PlayerDetail,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,  # TODO: Fix unmarshaling issue
        )

    def get_player(
        self,
        *,
        nfl_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayerDetail:
        r"""Get Player Details

        Retrieves detailed information about a specific NFL player including physical attributes,
        team information, draft details, and current status.


        :param nfl_id: NFL player identifier
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_player_config(
            nfl_id=nfl_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_player_async(
        self,
        *,
        nfl_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayerDetail:
        r"""Get Player Details

        Retrieves detailed information about a specific NFL player including physical attributes,
        team information, draft details, and current status.


        :param nfl_id: NFL player identifier
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_player_config(
            nfl_id=nfl_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_projected_stats_config(
        self,
        *,
        season: int,
        week: int,
        filter_nfl_team_id: Optional[str] = None,
        page_size: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_projected_stats."""
        return EndpointConfig(
            method="GET",
            path="/api/players/projectedStats",
            operation_id="getProjectedStats",
            request=models.GetProjectedStatsRequest(
                filter_nfl_team_id=filter_nfl_team_id,
                season=season,
                week=week,
                page_size=page_size,
            ),
            response_type=models.ProjectedStatsResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_projected_stats(
        self,
        *,
        season: int,
        week: int,
        filter_nfl_team_id: Optional[str] = None,
        page_size: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.PlayerProjection]:
        r"""Get Projected Player Statistics

        Retrieves projected fantasy statistics for players based on team, season, and week.
        Returns data in JSON:API format with relationships between players and their projected stats.


        :param season: Season year
        :param week: Week number within the season
        :param filter_nfl_team_id: Filter by NFL team ID (UUID format)
        :param page_size: Number of results per page
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_projected_stats_config(
            season=season,
            week=week,
            filter_nfl_team_id=filter_nfl_team_id,
            page_size=page_size,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_projected_stats_async(
        self,
        *,
        season: int,
        week: int,
        filter_nfl_team_id: Optional[str] = None,
        page_size: Optional[int] = 20,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.PlayerProjection]:
        r"""Get Projected Player Statistics

        Retrieves projected fantasy statistics for players based on team, season, and week.
        Returns data in JSON:API format with relationships between players and their projected stats.


        :param season: Season year
        :param week: Week number within the season
        :param filter_nfl_team_id: Filter by NFL team ID (UUID format)
        :param page_size: Number of results per page
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_projected_stats_config(
            season=season,
            week=week,
            filter_nfl_team_id=filter_nfl_team_id,
            page_size=page_size,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _search_players_config(
        self,
        *,
        term: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for search_players."""
        return EndpointConfig(
            method="GET",
            path="/api/players/search",
            operation_id="searchPlayers",
            request=models.SearchPlayersRequest(term=term),
            response_type=models.PlayerSearchResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def search_players(
        self,
        *,
        term: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayerSearchResponse:
        r"""Search Players

        Searches for NFL players by name or term. Returns a list of players matching the search criteria
        including both active and retired players.


        :param term: Search term for player name (first or last name)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._search_players_config(
            term=term,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def search_players_async(
        self,
        *,
        term: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlayerSearchResponse:
        r"""Search Players

        Searches for NFL players by name or term. Returns a list of players matching the search criteria
        including both active and retired players.


        :param term: Search term for player name (first or last name)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._search_players_config(
            term=term,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
