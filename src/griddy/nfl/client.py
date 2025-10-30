import base64
import json
import time
import urllib
from typing import Any, Dict, List, Optional
from uuid import uuid4

import requests

from griddy import settings

from ..core.base_client import BaseClient
from ..core.utils import clean_text, extract_cookies_as_dict, parse_date, safe_int
from .models_original import (
    NFLGame,
    NFLNews,
    NFLPlayer,
    NFLPlayerStats,
    NFLSchedule,
    NFLStandings,
    NFLTeam,
)


class NFLClient(BaseClient):
    """Client for accessing NFL.com data."""

    _client_data = {
        "clientKey": settings.NFL["clientKey"],
        "clientSecret": settings.NFL["clientSecret"],
        "deviceId": str(uuid4()),
        "deviceInfo": base64.b64encode(
            json.dumps(
                {
                    "model": "desktop",
                    "version": "Chrome",
                    "osName": "Windows",
                    "osVersion": "10.0",
                },
                separators=(",", ":"),
            ).encode()
        ).decode(),
        "networkType": "other",
        "peacockUUID": "undefined",
    }

    def __init__(self, **kwargs):
        """
        Initialize NFL client.

        Args:
            **kwargs: Additional arguments passed to BaseClient
        """
        super().__init__(
            base_url=settings.NFL["base_api_url"],
            headers={"Accept": "application/json"},
            **kwargs,
        )
        self._account_info = self.load_account_info()
        self._token = {}
        self._token = self.get_auth_token()

    def _token_is_fresh(self) -> bool:
        """
        Determine if it's time to refresh our access token

        Returns:
            A bool which is True if the token is fresh; False otherwise
        """
        return (self._token.get("accessToken") is not None) and self._token.get(
            "expiresIn"
        ) > time.time() + 30

    def get_auth_token(self):
        """
        Get and store an authentication token if necessary.
        """
        if self._token_is_fresh():
            return

        token_url = settings.NFL["token_url"]
        if self._token.get("refreshToken"):
            token_url += "/refresh"

        token_request_data = json.dumps(
            {**self._client_data, **self._account_info}, separators=(",", ":")
        ).encode()
        response = requests.post(
            token_url,
            data=token_request_data,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()

        self._token = response.json()
        self.session.headers.update(
            {"Authorization": f"Bearer {self._token['accessToken']}"}
        )

    def load_account_info(self):
        """
        Load account information to be used in token requests.
        """
        nfl_auth_cookies = extract_cookies_as_dict(
            self.cookies_file, settings.NFL["auth_url"]
        )
        login_token = nfl_auth_cookies.get(f"glt_{settings.NFL['api_key']}")
        account_post_data = {
            "include": "profile,data",
            "lang": "en",
            "APIKey": settings.NFL["api_key"],
            "sdk": "js_latest",
            "login_token": login_token,
            "authMode": "cookie",
            "pageURL": "https://www.nfl.com/",
            "sdkBuild": settings.NFL["sdk_build"],
            "format": "json",
        }
        response = requests.post(
            settings.NFL["account_url"],
            data=urllib.parse.urlencode(account_post_data).encode("ascii"),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        ).json()
        info = {}
        for key in ["signatureTimestamp", "UID", "UIDSignature"]:
            if key in response:
                info[key] = response[key]

        return info

    def get_games(
        self,
        season: int,
        week: int,
        season_type: str = "REG",
        team: str | None = None,
        include_replays: bool = False,
        include_standings: bool = False,
    ) -> List[Dict]:
        """
        Get NFL games for a specific season and week.

        Args:
            season: Season year
            week: Week number (if None, returns all weeks)
            season_type: Season type (regular, playoffs, preseason)
            team: Team abbreviation to filter by
            include_replays: Whether to include information needed to access game replays
            include_standings: Whether to include standings information

        Returns:
            List of NFL games
        """
        params = {
            "season": season,
            "type": season_type,
            "week": week,
            "includeReplays": include_replays,
            "includeStandings": include_standings,
        }

        return self.get("experience/weekly-game-details", params=params)

    def get_teams(self) -> List[NFLTeam]:
        """
        Get all NFL teams.

        Returns:
            List of NFL teams
        """
        try:
            response = self.get("teams")
            teams_data = response.get("teams", [])

            teams = []
            for team_data in teams_data:
                team = self._parse_team(team_data)
                if team:
                    teams.append(team)

            return teams
        except Exception:
            return []

    def get_team(self, team_id: str) -> NFLTeam | None:
        """
        Get a specific NFL team.

        Args:
            team_id: Team identifier

        Returns:
            NFL team or None if not found
        """
        try:
            response = self.get(f"teams/{team_id}")
            team_data = response.get("team")
            return self._parse_team(team_data) if team_data else None
        except Exception:
            return None

    def get_players(
        self,
        team: Optional[str] = None,
        position: Optional[str] = None,
        status: str = "active",
    ) -> List[NFLPlayer]:
        """
        Get NFL players.

        Args:
            team: Team abbreviation to filter by
            position: Position to filter by
            status: Player status (active, inactive, etc.)

        Returns:
            List of NFL players
        """
        params = {"status": status}
        if team:
            params["team"] = team
        if position:
            params["position"] = position

        try:
            response = self.get("players", params=params)
            players_data = response.get("players", [])

            players = []
            for player_data in players_data:
                player = self._parse_player(player_data)
                if player:
                    players.append(player)

            return players
        except Exception:
            return []

    def get_player(self, player_id: str) -> Optional[NFLPlayer]:
        """
        Get a specific NFL player.

        Args:
            player_id: Player identifier

        Returns:
            NFL player or None if not found
        """
        try:
            response = self.get(f"players/{player_id}")
            player_data = response.get("player")
            return self._parse_player(player_data) if player_data else None
        except Exception:
            return None

    def get_player_stats(
        self,
        player_id: str,
        season: int,
        week: Optional[int] = None,
        season_type: str = "regular",
    ) -> List[NFLPlayerStats]:
        """
        Get player statistics.

        Args:
            player_id: Player identifier
            season: Season year
            week: Week number (if None, returns season stats)
            season_type: Season type

        Returns:
            List of player statistics
        """
        params = {
            "season": season,
            "seasonType": season_type,
        }
        if week is not None:
            params["week"] = week

        try:
            response = self.get(f"players/{player_id}/stats", params=params)
            stats_data = response.get("stats", [])

            stats = []
            for stat_data in stats_data:
                stat = self._parse_player_stats(stat_data, player_id)
                if stat:
                    stats.append(stat)

            return stats
        except Exception:
            return []

    def get_schedule(
        self, season: int, week: Optional[int] = None, season_type: str = "regular"
    ) -> NFLSchedule:
        """
        Get NFL schedule.

        Args:
            season: Season year
            week: Week number (if None, returns all weeks)
            season_type: Season type

        Returns:
            NFL schedule
        """
        games = self.get_games(season=season, week=week, season_type=season_type)

        return NFLSchedule(
            week=week or 1, season=season, season_type=season_type, games=games
        )

    def get_standings(self, season: int) -> List[NFLStandings]:
        """
        Get NFL standings.

        Args:
            season: Season year

        Returns:
            List of division standings
        """
        try:
            response = self.get("standings", params={"season": season})
            standings_data = response.get("standings", [])

            standings = []
            for standing_data in standings_data:
                standing = self._parse_standings(standing_data)
                if standing:
                    standings.append(standing)

            return standings
        except Exception:
            return []

    def get_news(
        self, team: Optional[str] = None, player: Optional[str] = None, limit: int = 10
    ) -> List[NFLNews]:
        """
        Get NFL news.

        Args:
            team: Team abbreviation to filter by
            player: Player ID to filter by
            limit: Maximum number of articles

        Returns:
            List of news articles
        """
        params = {"limit": limit}
        if team:
            params["team"] = team
        if player:
            params["player"] = player

        try:
            response = self.get("news", params=params)
            news_data = response.get("articles", [])

            articles = []
            for article_data in news_data:
                article = self._parse_news(article_data)
                if article:
                    articles.append(article)

            return articles
        except Exception:
            return []

    def _parse_game(self, data: Dict[str, Any]) -> NFLGame | None:
        """Parse game data from API response."""
        try:
            return NFLGame(
                id=str(data.get("id", "")),
                home_team=clean_text(data.get("homeTeam", {}).get("abbreviation"))
                or "",
                away_team=clean_text(data.get("awayTeam", {}).get("abbreviation"))
                or "",
                home_score=safe_int(data.get("homeScore")),
                away_score=safe_int(data.get("awayScore")),
                status=clean_text(data.get("status")) or "unknown",
                start_time=parse_date(data.get("startTime")),
                week=safe_int(data.get("week")),
                season=safe_int(data.get("season")),
                season_type=clean_text(data.get("seasonType")),
                quarter=safe_int(data.get("quarter")),
                time_remaining=clean_text(data.get("timeRemaining")),
                possession=clean_text(data.get("possession")),
                down=safe_int(data.get("down")),
                distance=safe_int(data.get("distance")),
                yard_line=clean_text(data.get("yardLine")),
                redzone=data.get("redzone"),
                weather=clean_text(data.get("weather")),
                temperature=safe_int(data.get("temperature")),
                wind=clean_text(data.get("wind")),
            )
        except Exception:
            return None

    def _parse_team(self, data: Dict[str, Any]) -> Optional[NFLTeam]:
        """Parse team data from API response."""
        try:
            return NFLTeam(
                id=str(data.get("id", "")),
                name=clean_text(data.get("name")) or "",
                abbreviation=clean_text(data.get("abbreviation")) or "",
                city=clean_text(data.get("city")),
                conference=clean_text(data.get("conference")),
                division=clean_text(data.get("division")),
                logo_url=clean_text(data.get("logoUrl")),
                primary_color=clean_text(data.get("primaryColor")),
                secondary_color=clean_text(data.get("secondaryColor")),
                wins=safe_int(data.get("wins")),
                losses=safe_int(data.get("losses")),
                ties=safe_int(data.get("ties")),
                playoff_seed=safe_int(data.get("playoffSeed")),
            )
        except Exception:
            return None

    def _parse_player(self, data: Dict[str, Any]) -> Optional[NFLPlayer]:
        """Parse player data from API response."""
        try:
            return NFLPlayer(
                id=str(data.get("id", "")),
                name=clean_text(data.get("name")) or "",
                team_id=clean_text(data.get("teamId")),
                position=clean_text(data.get("position")),
                jersey_number=safe_int(data.get("jerseyNumber")),
                height=clean_text(data.get("height")),
                weight=safe_int(data.get("weight")),
                age=safe_int(data.get("age")),
                experience=safe_int(data.get("experience")),
                college=clean_text(data.get("college")),
                rookie_year=safe_int(data.get("rookieYear")),
                status=clean_text(data.get("status")),
                photo_url=clean_text(data.get("photoUrl")),
            )
        except Exception:
            return None

    def _parse_player_stats(
        self, data: Dict[str, Any], player_id: str
    ) -> Optional[NFLPlayerStats]:
        """Parse player stats data from API response."""
        try:
            return NFLPlayerStats(
                player_id=player_id,
                game_id=clean_text(data.get("gameId")),
                season=safe_int(data.get("season")),
                week=safe_int(data.get("week")),
                stats=data.get("stats", {}),
                passing_yards=safe_int(data.get("passingYards")),
                passing_touchdowns=safe_int(data.get("passingTouchdowns")),
                interceptions=safe_int(data.get("interceptions")),
                completions=safe_int(data.get("completions")),
                attempts=safe_int(data.get("attempts")),
                rushing_yards=safe_int(data.get("rushingYards")),
                rushing_touchdowns=safe_int(data.get("rushingTouchdowns")),
                rushing_attempts=safe_int(data.get("rushingAttempts")),
                receiving_yards=safe_int(data.get("receivingYards")),
                receiving_touchdowns=safe_int(data.get("receivingTouchdowns")),
                receptions=safe_int(data.get("receptions")),
                targets=safe_int(data.get("targets")),
                tackles=safe_int(data.get("tackles")),
                sacks=data.get("sacks"),
                interceptions_defense=safe_int(data.get("interceptionsDefense")),
                fumbles_forced=safe_int(data.get("fumblesForced")),
                fumbles_recovered=safe_int(data.get("fumblesRecovered")),
            )
        except Exception:
            return None

    def _parse_standings(self, data: Dict[str, Any]) -> Optional[NFLStandings]:
        """Parse standings data from API response."""
        try:
            teams_data = data.get("teams", [])
            teams = []
            for team_data in teams_data:
                team = self._parse_team(team_data)
                if team:
                    teams.append(team)

            return NFLStandings(
                conference=clean_text(data.get("conference")) or "",
                division=clean_text(data.get("division")) or "",
                teams=teams,
            )
        except Exception:
            return None

    def _parse_news(self, data: Dict[str, Any]) -> Optional[NFLNews]:
        """Parse news data from API response."""
        try:
            return NFLNews(
                id=str(data.get("id", "")),
                title=clean_text(data.get("title")) or "",
                summary=clean_text(data.get("summary")),
                content=clean_text(data.get("content")),
                author=clean_text(data.get("author")),
                published_date=parse_date(data.get("publishedDate")),
                url=clean_text(data.get("url")),
                image_url=clean_text(data.get("imageUrl")),
                tags=data.get("tags", []),
                related_players=data.get("relatedPlayers", []),
                related_teams=data.get("relatedTeams", []),
            )
        except Exception:
            return None
