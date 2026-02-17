from typing import Mapping, Optional

from griddy_nfl import models, utils
from griddy_nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy_nfl.basesdk import EndpointConfig
from griddy_nfl.types import UNSET, OptionalNullable


class GameScheduleMixin:
    """Mixin for game schedule-related endpoints.

    These methods are designed to be mixed into classes that inherit from ProSDK/BaseSDK,
    which provides the helper methods (_resolve_base_url, _resolve_timeout, etc.).
    """

    def _get_scheduled_game_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_scheduled_game."""
        return EndpointConfig(
            method="GET",
            path="/api/schedules/game",
            operation_id="getScheduledGame",
            request=models.GetScheduledGameRequest(game_id=game_id),
            response_type=models.GameDetail,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_scheduled_game(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GameDetail:
        r"""Get Single Game Details

        Retrieves detailed information for a specific game by its ID.
        Returns comprehensive game data including teams, score, venue, broadcast information,
        and current game status.


        :param game_id: Game identifier (UUID format)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_scheduled_game_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_scheduled_game_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GameDetail:
        r"""Get Single Game Details

        Retrieves detailed information for a specific game by its ID.
        Returns comprehensive game data including teams, score, venue, broadcast information,
        and current game status.


        :param game_id: Game identifier (UUID format)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_scheduled_game_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_game_matchup_rankings_config(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_game_matchup_rankings."""
        return EndpointConfig(
            method="GET",
            path="/api/schedules/game/matchup/rankings",
            operation_id="getGameMatchupRankings",
            request=models.GetGameMatchupRankingsRequest(game_id=game_id),
            response_type=models.MatchupRankingsResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_game_matchup_rankings(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.MatchupRankingsResponse:
        r"""Get Game Matchup Rankings

        Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
        Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
        for various statistical categories.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_matchup_rankings_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_game_matchup_rankings_async(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.MatchupRankingsResponse:
        r"""Get Game Matchup Rankings

        Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
        Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
        for various statistical categories.


        :param game_id: Game identifier (10-digit format YYYYMMDDNN)
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_matchup_rankings_config(
            game_id=game_id,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_game_team_rankings_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        away_team_id: str,
        home_team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_game_team_rankings."""
        return EndpointConfig(
            method="GET",
            path="/api/stats/game/team-rankings",
            operation_id="getGameTeamRankings",
            request=models.GetGameTeamRankingsRequest(
                season=season,
                season_type=season_type,
                away_team_id=away_team_id,
                home_team_id=home_team_id,
                week=week,
            ),
            response_type=models.TeamRankingsResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )

    def get_game_team_rankings(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        away_team_id: str,
        home_team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRankingsResponse:
        r"""Get Team Rankings for Game

        Retrieves comprehensive statistical rankings for both teams in a specific game.
        Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


        :param season: Season year
        :param season_type: Type of season
        :param away_team_id: Away team UUID
        :param home_team_id: Home team UUID
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_team_rankings_config(
            season=season,
            season_type=season_type,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_game_team_rankings_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        away_team_id: str,
        home_team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRankingsResponse:
        r"""Get Team Rankings for Game

        Retrieves comprehensive statistical rankings for both teams in a specific game.
        Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


        :param season: Season year
        :param season_type: Type of season
        :param away_team_id: Away team UUID
        :param home_team_id: Home team UUID
        :param week: Week number
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_game_team_rankings_config(
            season=season,
            season_type=season_type,
            away_team_id=away_team_id,
            home_team_id=home_team_id,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_team_injuries_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_team_injuries."""
        return EndpointConfig(
            method="GET",
            path="/api/schedules/game/team/injuries",
            operation_id="getTeamInjuries",
            request=models.GetTeamInjuriesRequest(
                season=season,
                season_type=season_type,
                team_id=team_id,
                week=week,
            ),
            response_type=models.InjuryReportResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_team_injuries(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        r"""Get Team Injuries for Game Week

        Retrieves injury report information for a specific team in a given week.
        Returns player injury status and details for the specified team and week.


        :param season: Season year
        :param season_type: Type of season
        :param team_id: Team identifier (UUID format)
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_injuries_config(
            season=season,
            season_type=season_type,
            team_id=team_id,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_team_injuries_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        team_id: str,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.InjuryReportResponse:
        r"""Get Team Injuries for Game Week

        Retrieves injury report information for a specific team in a given week.
        Returns player injury status and details for the specified team and week.


        :param season: Season year
        :param season_type: Type of season
        :param team_id: Team identifier (UUID format)
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_injuries_config(
            season=season,
            season_type=season_type,
            team_id=team_id,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
