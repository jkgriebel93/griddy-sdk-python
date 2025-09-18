"""Pro Football Reference API client."""

from typing import List, Optional, Dict, Any
from datetime import datetime

from ..core.base_client import BaseClient
from ..core.utils import parse_date, safe_int, safe_float, clean_text
from .models import (
    PFRPlayer,
    PFRPlayerStats,
    PFRTeamStats,
    PFRGame,
    PFRDraftPick,
    PFRSeasonStats,
    PFRCareerStats,
)


class PFRClient(BaseClient):
    """Client for accessing Pro Football Reference data."""

    def __init__(self, **kwargs):
        """
        Initialize Pro Football Reference client.

        Args:
            **kwargs: Additional arguments passed to BaseClient
        """
        # Note: Pro Football Reference doesn't have an official API
        # This would need to be adapted for web scraping or unofficial APIs
        super().__init__(
            base_url="https://api.pro-football-reference.com",  # Placeholder URL
            headers={"Accept": "application/json"},
            rate_limit_delay=2.0,  # Be respectful with scraping
            **kwargs,
        )

    def search_players(
        self, name: str, position: Optional[str] = None
    ) -> List[PFRPlayer]:
        """
        Search for players by name.

        Args:
            name: Player name to search for
            position: Position filter

        Returns:
            List of matching players
        """
        params = {"name": name}
        if position:
            params["position"] = position

        try:
            response = self.get("players/search", params=params)
            players_data = response.get("players", [])

            players = []
            for player_data in players_data:
                player = self._parse_player(player_data)
                if player:
                    players.append(player)

            return players
        except Exception:
            return []

    def get_player(self, player_id: str) -> Optional[PFRPlayer]:
        """
        Get detailed player information.

        Args:
            player_id: Player identifier

        Returns:
            Player information or None if not found
        """
        try:
            response = self.get(f"players/{player_id}")
            player_data = response.get("player")
            return self._parse_player(player_data) if player_data else None
        except Exception:
            return None

    def get_player_season_stats(
        self, player_id: str, season: int
    ) -> Optional[PFRSeasonStats]:
        """
        Get player statistics for a specific season.

        Args:
            player_id: Player identifier
            season: Season year

        Returns:
            Season statistics or None if not found
        """
        try:
            response = self.get(f"players/{player_id}/seasons/{season}")
            season_data = response.get("season")
            return self._parse_season_stats(season_data) if season_data else None
        except Exception:
            return None

    def get_player_career_stats(self, player_id: str) -> Optional[PFRCareerStats]:
        """
        Get complete career statistics for a player.

        Args:
            player_id: Player identifier

        Returns:
            Career statistics or None if not found
        """
        try:
            response = self.get(f"players/{player_id}/career")
            career_data = response.get("career")
            return self._parse_career_stats(career_data) if career_data else None
        except Exception:
            return None

    def get_player_game_stats(
        self, player_id: str, season: int, week: Optional[int] = None
    ) -> List[PFRPlayerStats]:
        """
        Get player game-by-game statistics.

        Args:
            player_id: Player identifier
            season: Season year
            week: Specific week (if None, returns all weeks)

        Returns:
            List of game statistics
        """
        params = {"season": season}
        if week is not None:
            params["week"] = week

        try:
            response = self.get(f"players/{player_id}/games", params=params)
            games_data = response.get("games", [])

            stats = []
            for game_data in games_data:
                stat = self._parse_player_stats(game_data, player_id)
                if stat:
                    stats.append(stat)

            return stats
        except Exception:
            return []

    def get_team_stats(self, team: str, season: int) -> Optional[PFRTeamStats]:
        """
        Get team statistics for a season.

        Args:
            team: Team abbreviation
            season: Season year

        Returns:
            Team statistics or None if not found
        """
        try:
            response = self.get(f"teams/{team}/seasons/{season}")
            team_data = response.get("team")
            return self._parse_team_stats(team_data) if team_data else None
        except Exception:
            return None

    def get_draft_class(self, year: int) -> List[PFRDraftPick]:
        """
        Get NFL draft picks for a specific year.

        Args:
            year: Draft year

        Returns:
            List of draft picks
        """
        try:
            response = self.get(f"draft/{year}")
            picks_data = response.get("picks", [])

            picks = []
            for pick_data in picks_data:
                pick = self._parse_draft_pick(pick_data)
                if pick:
                    picks.append(pick)

            return picks
        except Exception:
            return []

    def get_hall_of_fame_players(self) -> List[PFRPlayer]:
        """
        Get all Hall of Fame players.

        Returns:
            List of Hall of Fame players
        """
        try:
            response = self.get("hall-of-fame")
            players_data = response.get("players", [])

            players = []
            for player_data in players_data:
                player = self._parse_player(player_data)
                if player:
                    players.append(player)

            return players
        except Exception:
            return []

    def get_season_leaders(
        self,
        season: int,
        stat_category: str,
        position: Optional[str] = None,
        limit: int = 10,
    ) -> List[PFRPlayerStats]:
        """
        Get statistical leaders for a season.

        Args:
            season: Season year
            stat_category: Statistical category (passing_yards, rushing_yards, etc.)
            position: Position filter
            limit: Number of leaders to return

        Returns:
            List of statistical leaders
        """
        params = {"season": season, "category": stat_category, "limit": limit}
        if position:
            params["position"] = position

        try:
            response = self.get("leaders", params=params)
            leaders_data = response.get("leaders", [])

            leaders = []
            for leader_data in leaders_data:
                leader = self._parse_player_stats(
                    leader_data, leader_data.get("playerId", "")
                )
                if leader:
                    leaders.append(leader)

            return leaders
        except Exception:
            return []

    def get_historical_games(
        self, season: int, week: Optional[int] = None, team: Optional[str] = None
    ) -> List[PFRGame]:
        """
        Get historical game data.

        Args:
            season: Season year
            week: Week number (if None, returns all weeks)
            team: Team abbreviation filter

        Returns:
            List of historical games
        """
        params = {"season": season}
        if week is not None:
            params["week"] = week
        if team:
            params["team"] = team

        try:
            response = self.get("games", params=params)
            games_data = response.get("games", [])

            games = []
            for game_data in games_data:
                game = self._parse_game(game_data)
                if game:
                    games.append(game)

            return games
        except Exception:
            return []

    def _parse_player(self, data: Dict[str, Any]) -> Optional[PFRPlayer]:
        """Parse player data from API response."""
        try:
            return PFRPlayer(
                id=str(data.get("id", "")),
                name=clean_text(data.get("name")) or "",
                team_id=clean_text(data.get("teamId")),
                position=clean_text(data.get("position")),
                jersey_number=safe_int(data.get("jerseyNumber")),
                birth_date=parse_date(data.get("birthDate")),
                height_inches=safe_int(data.get("heightInches")),
                weight=safe_int(data.get("weight")),
                college=clean_text(data.get("college")),
                draft_year=safe_int(data.get("draftYear")),
                draft_round=safe_int(data.get("draftRound")),
                draft_pick=safe_int(data.get("draftPick")),
                career_start=safe_int(data.get("careerStart")),
                career_end=safe_int(data.get("careerEnd")),
                hall_of_fame=data.get("hallOfFame", False),
                pro_bowls=safe_int(data.get("proBowls")),
                all_pros=safe_int(data.get("allPros")),
            )
        except Exception:
            return None

    def _parse_player_stats(
        self, data: Dict[str, Any], player_id: str
    ) -> Optional[PFRPlayerStats]:
        """Parse player statistics from API response."""
        try:
            return PFRPlayerStats(
                player_id=player_id,
                game_id=clean_text(data.get("gameId")),
                season=safe_int(data.get("season")),
                week=safe_int(data.get("week")),
                stats=data.get("stats", {}),
                # Passing
                pass_completions=safe_int(data.get("passCompletions")),
                pass_attempts=safe_int(data.get("passAttempts")),
                pass_yards=safe_int(data.get("passYards")),
                pass_touchdowns=safe_int(data.get("passTouchdowns")),
                interceptions=safe_int(data.get("interceptions")),
                passer_rating=safe_float(data.get("passerRating")),
                qbr=safe_float(data.get("qbr")),
                sacks_taken=safe_int(data.get("sacksTaken")),
                sack_yards_lost=safe_int(data.get("sackYardsLost")),
                # Rushing
                rush_attempts=safe_int(data.get("rushAttempts")),
                rush_yards=safe_int(data.get("rushYards")),
                rush_touchdowns=safe_int(data.get("rushTouchdowns")),
                rush_long=safe_int(data.get("rushLong")),
                rush_yards_per_attempt=safe_float(data.get("rushYardsPerAttempt")),
                # Receiving
                receptions=safe_int(data.get("receptions")),
                receiving_yards=safe_int(data.get("receivingYards")),
                receiving_touchdowns=safe_int(data.get("receivingTouchdowns")),
                targets=safe_int(data.get("targets")),
                receiving_long=safe_int(data.get("receivingLong")),
                yards_per_reception=safe_float(data.get("yardsPerReception")),
                catch_percentage=safe_float(data.get("catchPercentage")),
                # Defense
                tackles_solo=safe_int(data.get("tacklesSolo")),
                tackles_assisted=safe_int(data.get("tacklesAssisted")),
                tackles_total=safe_int(data.get("tacklesTotal")),
                tackles_for_loss=safe_int(data.get("tacklesForLoss")),
                sacks=safe_float(data.get("sacks")),
                quarterback_hits=safe_int(data.get("quarterbackHits")),
                interceptions_defense=safe_int(data.get("interceptionsDefense")),
                passes_defended=safe_int(data.get("passesDefended")),
                fumbles_forced=safe_int(data.get("fumblesForced")),
                fumbles_recovered=safe_int(data.get("fumblesRecovered")),
                defensive_touchdowns=safe_int(data.get("defensiveTouchdowns")),
                # Special teams
                field_goals_made=safe_int(data.get("fieldGoalsMade")),
                field_goals_attempted=safe_int(data.get("fieldGoalsAttempted")),
                field_goal_percentage=safe_float(data.get("fieldGoalPercentage")),
                extra_points_made=safe_int(data.get("extraPointsMade")),
                extra_points_attempted=safe_int(data.get("extraPointsAttempted")),
                punts=safe_int(data.get("punts")),
                punt_yards=safe_int(data.get("puntYards")),
                punt_average=safe_float(data.get("puntAverage")),
                punt_long=safe_int(data.get("puntLong")),
                # Advanced
                approximate_value=safe_float(data.get("approximateValue")),
                games_started=safe_int(data.get("gamesStarted")),
                snap_count=safe_int(data.get("snapCount")),
                snap_percentage=safe_float(data.get("snapPercentage")),
            )
        except Exception:
            return None

    def _parse_team_stats(self, data: Dict[str, Any]) -> Optional[PFRTeamStats]:
        """Parse team statistics from API response."""
        try:
            return PFRTeamStats(
                team_id=str(data.get("teamId", "")),
                season=safe_int(data.get("season")) or 0,
                games_played=safe_int(data.get("gamesPlayed")),
                wins=safe_int(data.get("wins")),
                losses=safe_int(data.get("losses")),
                ties=safe_int(data.get("ties")),
                win_percentage=safe_float(data.get("winPercentage")),
                points_for=safe_int(data.get("pointsFor")),
                total_yards=safe_int(data.get("totalYards")),
                passing_yards=safe_int(data.get("passingYards")),
                rushing_yards=safe_int(data.get("rushingYards")),
                first_downs=safe_int(data.get("firstDowns")),
                turnovers=safe_int(data.get("turnovers")),
                points_against=safe_int(data.get("pointsAgainst")),
                total_yards_allowed=safe_int(data.get("totalYardsAllowed")),
                passing_yards_allowed=safe_int(data.get("passingYardsAllowed")),
                rushing_yards_allowed=safe_int(data.get("rushingYardsAllowed")),
                takeaways=safe_int(data.get("takeaways")),
                sacks=safe_int(data.get("sacks")),
                field_goal_percentage=safe_float(data.get("fieldGoalPercentage")),
                punt_average=safe_float(data.get("puntAverage")),
                return_touchdowns=safe_int(data.get("returnTouchdowns")),
                strength_of_schedule=safe_float(data.get("strengthOfSchedule")),
                point_differential=safe_int(data.get("pointDifferential")),
                pythagorean_wins=safe_float(data.get("pythagoreanWins")),
            )
        except Exception:
            return None

    def _parse_game(self, data: Dict[str, Any]) -> Optional[PFRGame]:
        """Parse game data from API response."""
        try:
            return PFRGame(
                id=str(data.get("id", "")),
                home_team=clean_text(data.get("homeTeam")) or "",
                away_team=clean_text(data.get("awayTeam")) or "",
                home_score=safe_int(data.get("homeScore")),
                away_score=safe_int(data.get("awayScore")),
                status=clean_text(data.get("status")) or "unknown",
                start_time=parse_date(data.get("startTime")),
                week=safe_int(data.get("week")),
                season=safe_int(data.get("season")),
                season_type=clean_text(data.get("seasonType")),
                attendance=safe_int(data.get("attendance")),
                weather_conditions=clean_text(data.get("weatherConditions")),
                temperature=safe_int(data.get("temperature")),
                wind_speed=safe_int(data.get("windSpeed")),
                dome=data.get("dome"),
                playoff_game=data.get("playoffGame", False),
                overtime=data.get("overtime", False),
                home_team_record=clean_text(data.get("homeTeamRecord")),
                away_team_record=clean_text(data.get("awayTeamRecord")),
                spread=safe_float(data.get("spread")),
                over_under=safe_float(data.get("overUnder")),
            )
        except Exception:
            return None

    def _parse_draft_pick(self, data: Dict[str, Any]) -> Optional[PFRDraftPick]:
        """Parse draft pick data from API response."""
        try:
            return PFRDraftPick(
                year=safe_int(data.get("year")) or 0,
                round=safe_int(data.get("round")) or 0,
                pick=safe_int(data.get("pick")) or 0,
                overall_pick=safe_int(data.get("overallPick")) or 0,
                team=clean_text(data.get("team")) or "",
                player_name=clean_text(data.get("playerName")) or "",
                position=clean_text(data.get("position")) or "",
                college=clean_text(data.get("college")),
                approximate_value=safe_float(data.get("approximateValue")),
                years_played=safe_int(data.get("yearsPlayed")),
            )
        except Exception:
            return None

    def _parse_season_stats(self, data: Dict[str, Any]) -> Optional[PFRSeasonStats]:
        """Parse season statistics from API response."""
        try:
            stats_data = data.get("stats", {})
            stats = self._parse_player_stats(stats_data, data.get("playerId", ""))
            if not stats:
                return None

            return PFRSeasonStats(
                player_id=str(data.get("playerId", "")),
                season=safe_int(data.get("season")) or 0,
                team=clean_text(data.get("team")) or "",
                age=safe_int(data.get("age")),
                position=clean_text(data.get("position")) or "",
                games_played=safe_int(data.get("gamesPlayed")) or 0,
                games_started=safe_int(data.get("gamesStarted")),
                stats=stats,
                awards=data.get("awards", []),
            )
        except Exception:
            return None

    def _parse_career_stats(self, data: Dict[str, Any]) -> Optional[PFRCareerStats]:
        """Parse career statistics from API response."""
        try:
            seasons_data = data.get("seasons", [])
            seasons = []
            for season_data in seasons_data:
                season = self._parse_season_stats(season_data)
                if season:
                    seasons.append(season)

            totals_data = data.get("careerTotals", {})
            totals = self._parse_player_stats(totals_data, data.get("playerId", ""))

            averages_data = data.get("careerAverages", {})
            averages = self._parse_player_stats(averages_data, data.get("playerId", ""))

            if not totals or not averages:
                return None

            return PFRCareerStats(
                player_id=str(data.get("playerId", "")),
                seasons=seasons,
                career_totals=totals,
                career_averages=averages,
                hall_of_fame=data.get("hallOfFame", False),
                retired=data.get("retired", False),
                retirement_year=safe_int(data.get("retirementYear")),
            )
        except Exception:
            return None
