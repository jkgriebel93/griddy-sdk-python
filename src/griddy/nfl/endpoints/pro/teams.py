from typing import List, Mapping, Optional

from griddy.nfl import models, utils
from griddy.nfl._constants import COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES
from griddy.nfl.basesdk import EndpointConfig
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable


class Teams(ProSDK):

    def _get_all_teams_config(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_all_teams."""
        return EndpointConfig(
            method="GET",
            path="/api/teams/all",
            operation_id="getAllTeams",
            request=None,
            response_type=List[models.ProTeam],
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_all_teams(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ProTeam]:
        r"""Get All Teams

        Retrieves information for all NFL teams including regular teams and Pro Bowl teams.
        Returns comprehensive team data including colors, logos, stadiums, and contact information.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_all_teams_config(
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_all_teams_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ProTeam]:
        r"""Get All Teams

        Retrieves information for all NFL teams including regular teams and Pro Bowl teams.
        Returns comprehensive team data including colors, logos, stadiums, and contact information.


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_all_teams_config(
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_team_roster_config(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_team_roster."""
        return EndpointConfig(
            method="GET",
            path="/api/teams/roster",
            operation_id="getTeamRoster",
            request=models.GetTeamRosterRequest(team_id=team_id, season=season),
            response_type=models.TeamRosterResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_team_roster(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRosterResponse:
        r"""Get Team Roster

        Retrieves the complete roster for a specific team and season.
        Returns detailed player information including physical attributes, college info, and experience.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_roster_config(
            team_id=team_id,
            season=season,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_team_roster_async(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TeamRosterResponse:
        r"""Get Team Roster

        Retrieves the complete roster for a specific team and season.
        Returns detailed player information including physical attributes, college info, and experience.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_roster_config(
            team_id=team_id,
            season=season,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_weekly_team_roster_config(
        self,
        *,
        team_id: str,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_weekly_team_roster."""
        return EndpointConfig(
            method="GET",
            path="/api/teams/rosterWeek",
            operation_id="getWeeklyTeamRoster",
            request=models.GetWeeklyTeamRosterRequest(
                team_id=team_id,
                season=season,
                season_type=season_type,
                week=week,
            ),
            response_type=models.WeeklyRosterResponse,
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_weekly_team_roster(
        self,
        *,
        team_id: str,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyRosterResponse:
        r"""Get Weekly Team Roster

        Retrieves the roster for a specific team, season, season type, and week.
        Returns player information with weekly status and availability.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_weekly_team_roster_config(
            team_id=team_id,
            season=season,
            season_type=season_type,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_weekly_team_roster_async(
        self,
        *,
        team_id: str,
        season: int,
        season_type: models.SeasonTypeEnum,
        week: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.WeeklyRosterResponse:
        r"""Get Weekly Team Roster

        Retrieves the roster for a specific team, season, season type, and week.
        Returns player information with weekly status and availability.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param season_type: Type of season
        :param week: Week number within the season
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_weekly_team_roster_config(
            team_id=team_id,
            season=season,
            season_type=season_type,
            week=week,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    def _get_team_schedule_config(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_team_schedule."""
        return EndpointConfig(
            method="GET",
            path="/api/teams/schedule",
            operation_id="getTeamSchedule",
            request=models.GetTeamScheduleRequest(team_id=team_id, season=season),
            response_type=List[models.ScheduledGame],
            error_status_codes=RESOURCE_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_team_schedule(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ScheduledGame]:
        r"""Get Team Schedule

        Retrieves the complete schedule for a specific team and season.
        Returns all games including preseason, regular season, and postseason with scores for completed games.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_schedule_config(
            team_id=team_id,
            season=season,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_team_schedule_async(
        self,
        *,
        team_id: str,
        season: int,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ScheduledGame]:
        r"""Get Team Schedule

        Retrieves the complete schedule for a specific team and season.
        Returns all games including preseason, regular season, and postseason with scores for completed games.


        :param team_id: Team identifier (4-digit string)
        :param season: Season year
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_team_schedule_config(
            team_id=team_id,
            season=season,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)

    # TODO: These ranking methods may fit better in the stats APIs somewhere
    def _get_multiple_rankings_all_teams_config(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        stat0: str,
        stat1: Optional[str] = None,
        stat2: Optional[str] = None,
        stat3: Optional[str] = None,
        stat4: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        """Create endpoint configuration for get_multiple_rankings_all_teams."""
        return EndpointConfig(
            method="GET",
            path="/api/stats/multiple-rankings/all-teams",
            operation_id="getMultipleRankingsAllTeams",
            request=models.GetMultipleRankingsAllTeamsRequest(
                season=season,
                season_type=season_type,
                stat0=stat0,
                stat1=stat1,
                stat2=stat2,
                stat3=stat3,
                stat4=stat4,
            ),
            response_type=List[models.MultipleRankingsCategory],
            error_status_codes=COLLECTION_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_multiple_rankings_all_teams(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        stat0: str,
        stat1: Optional[str] = None,
        stat2: Optional[str] = None,
        stat3: Optional[str] = None,
        stat4: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.MultipleRankingsCategory]:
        r"""Get Multiple Rankings for All Teams

        Retrieves rankings for all 32 NFL teams across multiple specified statistical categories.
        Allows comparison of teams across up to 5 different statistics simultaneously.


        :param season: Season year
        :param season_type: Type of season
        :param stat0: First statistical category
        :param stat1: Second statistical category
        :param stat2: Third statistical category
        :param stat3: Fourth statistical category
        :param stat4: Fifth statistical category
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_multiple_rankings_all_teams_config(
            season=season,
            season_type=season_type,
            stat0=stat0,
            stat1=stat1,
            stat2=stat2,
            stat3=stat3,
            stat4=stat4,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return self._execute_endpoint(config)

    async def get_multiple_rankings_all_teams_async(
        self,
        *,
        season: int,
        season_type: models.SeasonTypeEnum,
        stat0: str,
        stat1: Optional[str] = None,
        stat2: Optional[str] = None,
        stat3: Optional[str] = None,
        stat4: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.MultipleRankingsCategory]:
        r"""Get Multiple Rankings for All Teams

        Retrieves rankings for all 32 NFL teams across multiple specified statistical categories.
        Allows comparison of teams across up to 5 different statistics simultaneously.


        :param season: Season year
        :param season_type: Type of season
        :param stat0: First statistical category
        :param stat1: Second statistical category
        :param stat2: Third statistical category
        :param stat3: Fourth statistical category
        :param stat4: Fifth statistical category
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        config = self._get_multiple_rankings_all_teams_config(
            season=season,
            season_type=season_type,
            stat0=stat0,
            stat1=stat1,
            stat2=stat2,
            stat3=stat3,
            stat4=stat4,
            retries=retries,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
        )
        return await self._execute_endpoint_async(config)
