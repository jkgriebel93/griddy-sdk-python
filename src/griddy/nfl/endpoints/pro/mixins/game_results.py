from typing import List, Mapping, Optional, Union

from griddy.nfl import models, utils
from griddy.nfl._constants import RESOURCE_ERROR_CODES
from griddy.nfl.basesdk import EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


class GameResultsDataMixin:
    """Mixin for game results and play data endpoints."""

    def _get_stats_boxscore_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_stats_boxscore."""
        return EndpointConfig(
            method="GET",
            path="/api/stats/boxscore",
            operation_id="getStatsBoxscore",
            request=models.GetStatsBoxscoreRequest(game_id=game_id),
            response_type=models.BoxscoreResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_stats_boxscore(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.BoxscoreResponse:
        r"""Get Game Boxscore (Stats API)

        Retrieves comprehensive boxscore data for a specific game including team statistics,
        individual player statistics, and scoring summary. Returns empty arrays for future games.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_stats_boxscore_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    def _get_playlist_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_playlist."""
        return EndpointConfig(
            method="GET",
            path="/api/secured/plays/playlist/game",
            operation_id="getPlaysWinProbability",
            request=models.GetPlayListRequest(game_id=game_id),
            response_type=dict,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Implement the pydantic models for PlayList
        )

    def get_playlist(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""
        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_playlist_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    def _get_summary_play_config(
        self,
        *,
        game_id: str,
        play_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_summary_play."""
        return EndpointConfig(
            method="GET",
            path="/api/plays/summaryPlay",
            operation_id="getSummaryPlay",
            request=models.GetSummaryPlayRequest(
                game_id=game_id,
                play_id=play_id,
            ),
            response_type=models.PlaySummaryResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_summary_play(
        self,
        *,
        game_id: str,
        play_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlaySummaryResponse:
        r"""Get Play Summary

        Retrieves detailed information about a specific play in a game including play description,
        statistics, involved players, win probability, and expected points.


        :param game_id: Game identifier (UUID format)
        :param play_id: Play identifier within the game
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_summary_play_config(
            game_id=game_id,
            play_id=play_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_summary_play_async(
        self,
        *,
        game_id: str,
        play_id: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.PlaySummaryResponse:
        r"""Get Play Summary

        Retrieves detailed information about a specific play in a game including play description,
        statistics, involved players, win probability, and expected points.


        :param game_id: Game identifier (UUID format)
        :param play_id: Play identifier within the game
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_summary_play_config(
            game_id=game_id,
            play_id=play_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_plays_win_probability_config(
        self,
        *,
        game_id: Union[models.GameID, models.GameIDTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_plays_win_probability."""
        return EndpointConfig(
            method="GET",
            path="/api/secured/plays/winProbability",
            operation_id="getPlaysWinProbability",
            request=models.GetPlaysWinProbabilityRequest(game_id=game_id),
            response_type=models.GetPlaysWinProbabilityResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=True,  # TODO: Fix Pydantic model
        )

    def get_plays_win_probability(
        self,
        *,
        game_id: Union[models.GameID, models.GameIDTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetPlaysWinProbabilityResponse:
        r"""Get Game Win Probability by Plays

        Retrieves comprehensive win probability data for every play in specified games.
        Returns pre-game win probabilities and detailed play-by-play probability changes,
        including Win Probability Added (WPA) metrics for each play. This advanced analytics
        endpoint tracks how each play impacts the probability of each team winning the game.
        Supports querying multiple games simultaneously.


        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_plays_win_probability_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_plays_win_probability_async(
        self,
        *,
        game_id: Union[models.GameID, models.GameIDTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetPlaysWinProbabilityResponse:
        r"""Get Game Win Probability by Plays

        Retrieves comprehensive win probability data for every play in specified games.
        Returns pre-game win probabilities and detailed play-by-play probability changes,
        including Win Probability Added (WPA) metrics for each play. This advanced analytics
        endpoint tracks how each play impacts the probability of each team winning the game.
        Supports querying multiple games simultaneously.


        :param game_id: Game identifier(s) in 10-digit format (YYYYMMDDNN).  Can be a single game ID or multiple game IDs for batch retrieval.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_plays_win_probability_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_win_probability_min_config(
        self,
        *,
        fapi_game_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_win_probability_min."""
        return EndpointConfig(
            method="GET",
            path="/api/secured/plays/winProbabilityMin",
            operation_id="getWinProbabilityMin",
            request=models.GetWinProbabilityMinRequest(fapi_game_id=fapi_game_id),
            response_type=models.WinProbabilityResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_win_probability_min(
        self,
        *,
        fapi_game_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WinProbabilityResponse:
        r"""Get Minimal Win Probability Data

        Retrieves minimal win probability data for specified games, including pregame
        win probabilities and play-by-play probability changes throughout the game.
        This endpoint provides essential win probability metrics with optimized data
        structure for performance. Supports multiple games in a single request.


        :param fapi_game_id: Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_win_probability_min_config(
            fapi_game_id=fapi_game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_win_probability_min_async(
        self,
        *,
        fapi_game_id: List[str],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WinProbabilityResponse:
        r"""Get Minimal Win Probability Data

        Retrieves minimal win probability data for specified games, including pregame
        win probabilities and play-by-play probability changes throughout the game.
        This endpoint provides essential win probability metrics with optimized data
        structure for performance. Supports multiple games in a single request.


        :param fapi_game_id: Football API game identifiers (UUID format). Supports multiple game IDs to retrieve win probability data for multiple games simultaneously.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_win_probability_min_config(
            fapi_game_id=fapi_game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
