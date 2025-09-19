"""ESPN API client."""

from typing import List, Optional, Dict, Any
from datetime import datetime, date

from ..core.base_client import BaseClient
from ..core.utils import parse_date, safe_int, safe_float, clean_text
from .models import (
    ESPNGame,
    ESPNTeam,
    ESPNPlayer,
    ESPNPlayerStats,
    ESPNScoreboard,
    ESPNStandings,
    ESPNNews,
    ESPNAthlete,
    ESPNEvent,
)


class ESPNClient(BaseClient):
    """Client for accessing ESPN API data."""

    def __init__(self, **kwargs):
        """
        Initialize ESPN client.

        Args:
            **kwargs: Additional arguments passed to BaseClient
        """
        # ESPN has a public API available
        super().__init__(
            base_url="https://site.api.espn.com/apis/site/v2/sports/football/nfl",
            headers={"Accept": "application/json", "User-Agent": "Griddy-SDK/0.1.0"},
            rate_limit_delay=0.5,  # Be respectful with requests
            **kwargs,
        )

    def get_scoreboard(
        self, date_str: Optional[str] = None, limit: int = 50
    ) -> Optional[ESPNScoreboard]:
        """
        Get ESPN scoreboard for a specific date.

        Args:
            date_str: Date string in YYYYMMDD format (if None, uses today)
            limit: Maximum number of games

        Returns:
            ESPN scoreboard or None if error
        """
        params = {"limit": limit}
        if date_str:
            params["dates"] = date_str

        try:
            response = self.get("scoreboard", params=params)
            return self._parse_scoreboard(response)
        except Exception:
            return None

    def get_teams(self) -> List[ESPNTeam]:
        """
        Get all NFL teams from ESPN.

        Returns:
            List of ESPN teams
        """
        try:
            response = self.get("teams")
            teams_data = (
                response.get("sports", [{}])[0].get("leagues", [{}])[0].get("teams", [])
            )

            teams = []
            for team_data in teams_data:
                team = self._parse_team(team_data.get("team", {}))
                if team:
                    teams.append(team)

            return teams
        except Exception:
            return []

    def get_team(self, team_id: str) -> Optional[ESPNTeam]:
        """
        Get specific team information.

        Args:
            team_id: ESPN team ID

        Returns:
            ESPN team or None if not found
        """
        try:
            response = self.get(f"teams/{team_id}")
            team_data = response.get("team", {})
            return self._parse_team(team_data) if team_data else None
        except Exception:
            return None

    def get_team_roster(self, team_id: str) -> List[ESPNPlayer]:
        """
        Get team roster from ESPN.

        Args:
            team_id: ESPN team ID

        Returns:
            List of players on the team
        """
        try:
            response = self.get(f"teams/{team_id}/roster")
            athletes_data = response.get("athletes", [])

            players = []
            for athlete_data in athletes_data:
                for item in athlete_data.get("items", []):
                    player = self._parse_player(item)
                    if player:
                        players.append(player)

            return players
        except Exception:
            return []

    def get_athlete(self, athlete_id: str) -> Optional[ESPNAthlete]:
        """
        Get detailed athlete information.

        Args:
            athlete_id: ESPN athlete ID

        Returns:
            ESPN athlete or None if not found
        """
        try:
            response = self.get(f"athletes/{athlete_id}")
            athlete_data = response.get("athlete", {})
            return self._parse_athlete(athlete_data) if athlete_data else None
        except Exception:
            return None

    def get_standings(self, season: Optional[int] = None) -> List[ESPNStandings]:
        """
        Get NFL standings from ESPN.

        Args:
            season: Season year (if None, uses current season)

        Returns:
            List of standings groups
        """
        params = {}
        if season:
            params["season"] = season

        try:
            response = self.get("standings", params=params)
            standings_data = response.get("standings", [])

            standings_list = []
            for standing_data in standings_data:
                standings = self._parse_standings(standing_data)
                if standings:
                    standings_list.append(standings)

            return standings_list
        except Exception:
            return []

    def get_news(
        self, limit: int = 10, team_id: Optional[str] = None
    ) -> List[ESPNNews]:
        """
        Get NFL news from ESPN.

        Args:
            limit: Maximum number of articles
            team_id: Filter by team ID

        Returns:
            List of news articles
        """
        params = {"limit": limit}

        endpoint = "news"
        if team_id:
            endpoint = f"teams/{team_id}/news"

        try:
            response = self.get(endpoint, params=params)
            articles_data = response.get("articles", [])

            articles = []
            for article_data in articles_data:
                article = self._parse_news(article_data)
                if article:
                    articles.append(article)

            return articles
        except Exception:
            return []

    def get_game_details(self, game_id: str) -> Optional[ESPNEvent]:
        """
        Get detailed game information.

        Args:
            game_id: ESPN game ID

        Returns:
            Detailed event information or None if not found
        """
        try:
            response = self.get(f"summary", params={"event": game_id})
            event_data = response.get("header", {})
            return self._parse_event(event_data) if event_data else None
        except Exception:
            return None

    def get_live_scores(self) -> List[ESPNGame]:
        """
        Get live scores for current games.

        Returns:
            List of games with current scores
        """
        scoreboard = self.get_scoreboard()
        if scoreboard:
            # Filter for live games
            live_games = [
                game
                for game in scoreboard.games
                if game.status and "live" in game.status.lower()
            ]
            return live_games
        return []

    def get_schedule(
        self,
        season: Optional[int] = None,
        season_type: Optional[int] = None,
        week: Optional[int] = None,
    ) -> List[ESPNGame]:
        """
        Get NFL schedule.

        Args:
            season: Season year
            season_type: Season type (1=preseason, 2=regular, 3=postseason)
            week: Week number

        Returns:
            List of scheduled games
        """
        params = {}
        if season:
            params["season"] = season
        if season_type:
            params["seasontype"] = season_type
        if week:
            params["week"] = week

        try:
            response = self.get("scoreboard", params=params)
            scoreboard = self._parse_scoreboard(response)
            return scoreboard.games if scoreboard else []
        except Exception:
            return []

    def _parse_scoreboard(self, data: Dict[str, Any]) -> Optional[ESPNScoreboard]:
        """Parse scoreboard data from ESPN API response."""
        try:
            season_data = data.get("season", {})
            leagues_data = data.get("leagues", [{}])
            league_data = leagues_data[0] if leagues_data else {}

            games_data = data.get("events", [])
            games = []
            for game_data in games_data:
                game = self._parse_game(game_data)
                if game:
                    games.append(game)

            return ESPNScoreboard(
                date=parse_date(data.get("day", {}).get("date")) or datetime.now(),
                league="NFL",
                season=safe_int(season_data.get("year")) or datetime.now().year,
                season_type=clean_text(season_data.get("type")) or "regular",
                week=safe_int(data.get("week", {}).get("number")),
                games=games,
            )
        except Exception:
            return None

    def _parse_game(self, data: Dict[str, Any]) -> Optional[ESPNGame]:
        """Parse game data from ESPN API response."""
        try:
            competitions = data.get("competitions", [{}])
            competition = competitions[0] if competitions else {}
            competitors = competition.get("competitors", [])

            home_team_data = next(
                (c for c in competitors if c.get("homeAway") == "home"), {}
            )
            away_team_data = next(
                (c for c in competitors if c.get("homeAway") == "away"), {}
            )

            venue_data = competition.get("venue", {})
            status_data = data.get("status", {})
            weather_data = competition.get("weather", {})

            return ESPNGame(
                id=str(data.get("id", "")),
                espn_id=str(data.get("id", "")),
                home_team=clean_text(home_team_data.get("team", {}).get("abbreviation"))
                or "",
                away_team=clean_text(away_team_data.get("team", {}).get("abbreviation"))
                or "",
                home_score=safe_int(home_team_data.get("score")),
                away_score=safe_int(away_team_data.get("score")),
                status=clean_text(status_data.get("type", {}).get("detail"))
                or "unknown",
                start_time=parse_date(data.get("date")),
                week=safe_int(data.get("week", {}).get("number")),
                season=safe_int(data.get("season", {}).get("year")),
                season_type=clean_text(data.get("season", {}).get("type")),
                broadcast_network=clean_text(
                    competition.get("broadcasts", [{}])[0].get("names", [None])[0]
                ),
                venue_name=clean_text(venue_data.get("fullName")),
                venue_city=clean_text(venue_data.get("address", {}).get("city")),
                venue_state=clean_text(venue_data.get("address", {}).get("state")),
                attendance=safe_int(competition.get("attendance")),
                temperature=safe_int(weather_data.get("temperature")),
                weather_description=clean_text(weather_data.get("displayValue")),
                is_neutral_site=venue_data.get("neutralSite", False),
                conference_game=competition.get("conferenceCompetition", False),
                odds=(
                    competition.get("odds", [{}])[0]
                    if competition.get("odds")
                    else None
                ),
            )
        except Exception:
            return None

    def _parse_team(self, data: Dict[str, Any]) -> Optional[ESPNTeam]:
        """Parse team data from ESPN API response."""
        try:
            logos = data.get("logos", [{}])
            logo_url = logos[0].get("href") if logos else None

            record_data = data.get("record", {}).get("items", [{}])
            record_summary = record_data[0].get("summary") if record_data else None

            return ESPNTeam(
                id=str(data.get("id", "")),
                espn_id=str(data.get("id", "")),
                name=clean_text(data.get("name")) or "",
                abbreviation=clean_text(data.get("abbreviation")) or "",
                display_name=clean_text(data.get("displayName")),
                short_display_name=clean_text(data.get("shortDisplayName")),
                city=clean_text(data.get("location")),
                conference=clean_text(
                    data.get("groups", {}).get("parent", {}).get("name")
                ),
                division=clean_text(data.get("groups", {}).get("name")),
                color=clean_text(data.get("color")),
                alternate_color=clean_text(data.get("alternateColor")),
                logo=logo_url,
                record=record_summary,
                is_active=data.get("isActive", True),
            )
        except Exception:
            return None

    def _parse_player(self, data: Dict[str, Any]) -> Optional[ESPNPlayer]:
        """Parse player data from ESPN API response."""
        try:
            headshot_data = data.get("headshot", {})
            position_data = data.get("position", {})
            jersey = data.get("jersey")

            return ESPNPlayer(
                id=str(data.get("id", "")),
                espn_id=str(data.get("id", "")),
                name=clean_text(data.get("fullName")) or "",
                display_name=clean_text(data.get("displayName")),
                short_name=clean_text(data.get("shortName")),
                position=clean_text(position_data.get("abbreviation")),
                jersey_number=safe_int(jersey),
                weight=safe_int(data.get("weight")),
                height=clean_text(data.get("displayHeight")),
                age=safe_int(data.get("age")),
                experience=clean_text(data.get("experience", {}).get("displayValue")),
                birth_place=clean_text(data.get("birthPlace", {}).get("displayText")),
                college=clean_text(data.get("college", {}).get("name")),
                headshot=headshot_data.get("href") if headshot_data else None,
                jersey=jersey,
                active=data.get("active", True),
                injured=data.get("injured", False),
                injury_status=(
                    clean_text(data.get("injuries", [{}])[0].get("details"))
                    if data.get("injuries")
                    else None
                ),
            )
        except Exception:
            return None

    def _parse_athlete(self, data: Dict[str, Any]) -> Optional[ESPNAthlete]:
        """Parse athlete data from ESPN API response."""
        try:
            return ESPNAthlete(
                id=str(data.get("id", "")),
                guid=clean_text(data.get("guid")),
                uid=clean_text(data.get("uid")),
                first_name=clean_text(data.get("firstName")) or "",
                last_name=clean_text(data.get("lastName")) or "",
                full_name=clean_text(data.get("fullName")) or "",
                display_name=clean_text(data.get("displayName")) or "",
                short_name=clean_text(data.get("shortName")) or "",
                weight=safe_float(data.get("weight")),
                display_weight=clean_text(data.get("displayWeight")),
                height=safe_float(data.get("height")),
                display_height=clean_text(data.get("displayHeight")),
                age=safe_int(data.get("age")),
                date_of_birth=parse_date(data.get("dateOfBirth")),
                birth_place=data.get("birthPlace"),
                college=data.get("college"),
                slug=clean_text(data.get("slug")),
                headshot=data.get("headshot"),
                jersey=clean_text(data.get("jersey")),
                position=data.get("position"),
                team=data.get("team"),
                status=data.get("status"),
                statistics=data.get("statistics", []),
            )
        except Exception:
            return None

    def _parse_standings(self, data: Dict[str, Any]) -> Optional[ESPNStandings]:
        """Parse standings data from ESPN API response."""
        try:
            return ESPNStandings(
                season=safe_int(data.get("season")) or datetime.now().year,
                season_type=clean_text(data.get("seasonType")) or "regular",
                groups=data.get("groups", []),
            )
        except Exception:
            return None

    def _parse_news(self, data: Dict[str, Any]) -> Optional[ESPNNews]:
        """Parse news data from ESPN API response."""
        try:
            return ESPNNews(
                id=str(data.get("id", "")),
                headline=clean_text(data.get("headline")) or "",
                description=clean_text(data.get("description")),
                story=clean_text(data.get("story")),
                published=parse_date(data.get("published")),
                last_modified=parse_date(data.get("lastModified")),
                premium=data.get("premium", False),
                links=data.get("links"),
                categories=data.get("categories", []),
                keywords=data.get("keywords", []),
                byline=clean_text(data.get("byline")),
                images=data.get("images", []),
                video=data.get("video"),
            )
        except Exception:
            return None

    def _parse_event(self, data: Dict[str, Any]) -> Optional[ESPNEvent]:
        """Parse event data from ESPN API response."""
        try:
            competition_data = data.get("competition", {})
            season_data = data.get("season", {})
            week_data = data.get("week", {})

            return ESPNEvent(
                id=str(data.get("id", "")),
                uid=clean_text(data.get("uid")),
                date=parse_date(data.get("timeStamp")) or datetime.now(),
                name=clean_text(data.get("title")) or "",
                short_name=clean_text(data.get("shortName")) or "",
                season=season_data,
                week=week_data,
                competitions=[competition_data] if competition_data else [],
                links=data.get("links", []),
                weather=competition_data.get("weather"),
                status=data.get("status", {}),
                broadcasts=competition_data.get("broadcasts", []),
                odds=competition_data.get("odds", []),
            )
        except Exception:
            return None
