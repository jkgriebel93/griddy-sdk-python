"""Pro Football Focus API client."""

from typing import List, Optional, Dict, Any
from datetime import datetime

from ..core.base_client import BaseClient
from ..core.utils import parse_date, safe_int, safe_float, clean_text
from .models import (
    PFFPlayer,
    PFFPlayerGrades,
    PFFPlayerMetrics,
    PFFTeamGrades,
    PFFSeasonSummary,
    PFFDraftProspect,
    PFFMockDraft,
    PFFInjuryReport,
    PFFPassingGrades,
    PFFRushingGrades,
    PFFReceivingGrades,
    PFFDefensiveGrades,
    PFFSpecialTeamsGrades,
)


class PFFClient(BaseClient):
    """Client for accessing Pro Football Focus data."""

    def __init__(self, api_key: Optional[str] = None, **kwargs):
        """
        Initialize PFF client.

        Args:
            api_key: PFF API key for authenticated requests
            **kwargs: Additional arguments passed to BaseClient
        """
        headers = {"Accept": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        # Note: PFF has premium/subscription-based API access
        super().__init__(
            base_url="https://api.pff.com/v1",  # Placeholder URL
            headers=headers,
            rate_limit_delay=1.0,  # Respectful rate limiting
            **kwargs,
        )

    def get_player_grades(
        self, player_id: str, season: int, week: Optional[int] = None
    ) -> Optional[PFFPlayerGrades]:
        """
        Get PFF grades for a specific player.

        Args:
            player_id: Player identifier
            season: Season year
            week: Week number (if None, returns season grades)

        Returns:
            Player grades or None if not found
        """
        params = {"season": season}
        if week is not None:
            params["week"] = week

        try:
            response = self.get(f"players/{player_id}/grades", params=params)
            grades_data = response.get("grades")
            return self._parse_player_grades(grades_data) if grades_data else None
        except Exception:
            return None

    def get_player_metrics(
        self, player_id: str, season: int, week: Optional[int] = None
    ) -> Optional[PFFPlayerMetrics]:
        """
        Get advanced PFF metrics for a player.

        Args:
            player_id: Player identifier
            season: Season year
            week: Week number (if None, returns season metrics)

        Returns:
            Player metrics or None if not found
        """
        params = {"season": season}
        if week is not None:
            params["week"] = week

        try:
            response = self.get(f"players/{player_id}/metrics", params=params)
            metrics_data = response.get("metrics")
            return (
                self._parse_player_metrics(metrics_data, player_id, season, week)
                if metrics_data
                else None
            )
        except Exception:
            return None

    def get_team_grades(
        self, team_id: str, season: int, week: Optional[int] = None
    ) -> Optional[PFFTeamGrades]:
        """
        Get PFF team grades.

        Args:
            team_id: Team identifier
            season: Season year
            week: Week number (if None, returns season grades)

        Returns:
            Team grades or None if not found
        """
        params = {"season": season}
        if week is not None:
            params["week"] = week

        try:
            response = self.get(f"teams/{team_id}/grades", params=params)
            grades_data = response.get("grades")
            return (
                self._parse_team_grades(grades_data, team_id, season, week)
                if grades_data
                else None
            )
        except Exception:
            return None

    def get_position_rankings(
        self, position: str, season: int, week: Optional[int] = None, limit: int = 50
    ) -> List[PFFPlayerGrades]:
        """
        Get PFF rankings for a specific position.

        Args:
            position: Position abbreviation (QB, RB, WR, etc.)
            season: Season year
            week: Week number (if None, returns season rankings)
            limit: Maximum number of players to return

        Returns:
            List of player grades ranked by overall grade
        """
        params = {"position": position, "season": season, "limit": limit}
        if week is not None:
            params["week"] = week

        try:
            response = self.get("rankings", params=params)
            rankings_data = response.get("rankings", [])

            rankings = []
            for ranking_data in rankings_data:
                grades = self._parse_player_grades(ranking_data)
                if grades:
                    rankings.append(grades)

            return rankings
        except Exception:
            return []

    def get_season_summary(
        self, player_id: str, season: int
    ) -> Optional[PFFSeasonSummary]:
        """
        Get season summary with PFF grades and awards.

        Args:
            player_id: Player identifier
            season: Season year

        Returns:
            Season summary or None if not found
        """
        try:
            response = self.get(f"players/{player_id}/seasons/{season}")
            summary_data = response.get("summary")
            return (
                self._parse_season_summary(summary_data, player_id, season)
                if summary_data
                else None
            )
        except Exception:
            return None

    def get_all_pro_teams(self, season: int) -> Dict[str, List[PFFPlayer]]:
        """
        Get PFF All-Pro teams.

        Args:
            season: Season year

        Returns:
            Dictionary with first and second team All-Pro players
        """
        try:
            response = self.get(f"awards/all-pro/{season}")
            teams_data = response.get("teams", {})

            result = {}
            for team_level, players_data in teams_data.items():
                players = []
                for player_data in players_data:
                    player = self._parse_player(player_data)
                    if player:
                        players.append(player)
                result[team_level] = players

            return result
        except Exception:
            return {}

    def get_team_of_the_week(self, season: int, week: int) -> List[PFFPlayer]:
        """
        Get PFF Team of the Week.

        Args:
            season: Season year
            week: Week number

        Returns:
            List of Team of the Week players
        """
        try:
            response = self.get(f"awards/team-of-the-week/{season}/{week}")
            players_data = response.get("players", [])

            players = []
            for player_data in players_data:
                player = self._parse_player(player_data)
                if player:
                    players.append(player)

            return players
        except Exception:
            return []

    def get_draft_board(
        self, year: int, position: Optional[str] = None, limit: int = 100
    ) -> List[PFFDraftProspect]:
        """
        Get PFF draft board rankings.

        Args:
            year: Draft year
            position: Position filter
            limit: Maximum number of prospects

        Returns:
            List of draft prospects ranked by PFF grade
        """
        params = {"limit": limit}
        if position:
            params["position"] = position

        try:
            response = self.get(f"draft/{year}/board", params=params)
            prospects_data = response.get("prospects", [])

            prospects = []
            for prospect_data in prospects_data:
                prospect = self._parse_draft_prospect(prospect_data)
                if prospect:
                    prospects.append(prospect)

            return prospects
        except Exception:
            return []

    def get_mock_draft(
        self, year: int, round: Optional[int] = None
    ) -> List[PFFMockDraft]:
        """
        Get PFF mock draft.

        Args:
            year: Draft year
            round: Specific round (if None, returns all rounds)

        Returns:
            List of mock draft picks
        """
        params = {}
        if round is not None:
            params["round"] = round

        try:
            response = self.get(f"draft/{year}/mock", params=params)
            picks_data = response.get("picks", [])

            picks = []
            for pick_data in picks_data:
                pick = self._parse_mock_draft_pick(pick_data, year)
                if pick:
                    picks.append(pick)

            return picks
        except Exception:
            return []

    def get_injury_report(
        self, team: Optional[str] = None, player_id: Optional[str] = None
    ) -> List[PFFInjuryReport]:
        """
        Get PFF injury analysis.

        Args:
            team: Team abbreviation filter
            player_id: Specific player filter

        Returns:
            List of injury reports
        """
        params = {}
        if team:
            params["team"] = team
        if player_id:
            params["player"] = player_id

        try:
            response = self.get("injuries", params=params)
            injuries_data = response.get("injuries", [])

            injuries = []
            for injury_data in injuries_data:
                injury = self._parse_injury_report(injury_data)
                if injury:
                    injuries.append(injury)

            return injuries
        except Exception:
            return []

    def get_pressure_leaders(
        self, season: int, position: str = "EDGE", limit: int = 20
    ) -> List[PFFPlayerGrades]:
        """
        Get pass rush pressure leaders.

        Args:
            season: Season year
            position: Position group (EDGE, DI, LB)
            limit: Number of leaders to return

        Returns:
            List of pressure leaders with grades
        """
        params = {
            "category": "pressure",
            "position": position,
            "season": season,
            "limit": limit,
        }

        try:
            response = self.get("leaders", params=params)
            leaders_data = response.get("leaders", [])

            leaders = []
            for leader_data in leaders_data:
                grades = self._parse_player_grades(leader_data)
                if grades:
                    leaders.append(grades)

            return leaders
        except Exception:
            return []

    def get_coverage_leaders(
        self, season: int, position: str = "CB", limit: int = 20
    ) -> List[PFFPlayerGrades]:
        """
        Get coverage leaders.

        Args:
            season: Season year
            position: Position group (CB, S, LB)
            limit: Number of leaders to return

        Returns:
            List of coverage leaders with grades
        """
        params = {
            "category": "coverage",
            "position": position,
            "season": season,
            "limit": limit,
        }

        try:
            response = self.get("leaders", params=params)
            leaders_data = response.get("leaders", [])

            leaders = []
            for leader_data in leaders_data:
                grades = self._parse_player_grades(leader_data)
                if grades:
                    leaders.append(grades)

            return leaders
        except Exception:
            return []

    def _parse_player_grades(self, data: Dict[str, Any]) -> Optional[PFFPlayerGrades]:
        """Parse player grades from API response."""
        try:
            # Parse position-specific grades
            passing = None
            if data.get("passing"):
                passing = PFFPassingGrades(
                    overall_grade=safe_float(data["passing"].get("overallGrade")),
                    accuracy_grade=safe_float(data["passing"].get("accuracyGrade")),
                    deep_ball_grade=safe_float(data["passing"].get("deepBallGrade")),
                    pocket_grade=safe_float(data["passing"].get("pocketGrade")),
                    play_action_grade=safe_float(
                        data["passing"].get("playActionGrade")
                    ),
                    completion_percentage_above_expectation=safe_float(
                        data["passing"].get("cpoe")
                    ),
                    yards_per_attempt=safe_float(
                        data["passing"].get("yardsPerAttempt")
                    ),
                    air_yards_per_attempt=safe_float(
                        data["passing"].get("airYardsPerAttempt")
                    ),
                    pressure_to_sack_rate=safe_float(
                        data["passing"].get("pressureToSackRate")
                    ),
                    turnover_worthy_plays=safe_int(
                        data["passing"].get("turnoverWorthyPlays")
                    ),
                    big_time_throws=safe_int(data["passing"].get("bigTimeThrows")),
                    pressured_dropbacks=safe_int(
                        data["passing"].get("pressuredDropbacks")
                    ),
                    time_to_throw=safe_float(data["passing"].get("timeToThrow")),
                )

            rushing = None
            if data.get("rushing"):
                rushing = PFFRushingGrades(
                    overall_grade=safe_float(data["rushing"].get("overallGrade")),
                    vision_grade=safe_float(data["rushing"].get("visionGrade")),
                    power_grade=safe_float(data["rushing"].get("powerGrade")),
                    elusiveness_grade=safe_float(
                        data["rushing"].get("elusivenessGrade")
                    ),
                    yards_after_contact=safe_float(
                        data["rushing"].get("yardsAfterContact")
                    ),
                    forced_missed_tackles=safe_int(
                        data["rushing"].get("forcedMissedTackles")
                    ),
                    breakaway_runs=safe_int(data["rushing"].get("breakawayRuns")),
                    stuffed_runs=safe_int(data["rushing"].get("stuffedRuns")),
                    red_zone_attempts=safe_int(data["rushing"].get("redZoneAttempts")),
                    goal_line_attempts=safe_int(
                        data["rushing"].get("goalLineAttempts")
                    ),
                )

            receiving = None
            if data.get("receiving"):
                receiving = PFFReceivingGrades(
                    overall_grade=safe_float(data["receiving"].get("overallGrade")),
                    route_running_grade=safe_float(
                        data["receiving"].get("routeRunningGrade")
                    ),
                    hands_grade=safe_float(data["receiving"].get("handsGrade")),
                    contested_catch_grade=safe_float(
                        data["receiving"].get("contestedCatchGrade")
                    ),
                    separation_grade=safe_float(
                        data["receiving"].get("separationGrade")
                    ),
                    yards_after_catch=safe_float(
                        data["receiving"].get("yardsAfterCatch")
                    ),
                    drop_rate=safe_float(data["receiving"].get("dropRate")),
                    contested_catch_rate=safe_float(
                        data["receiving"].get("contestedCatchRate")
                    ),
                    target_share=safe_float(data["receiving"].get("targetShare")),
                    air_yards_share=safe_float(data["receiving"].get("airYardsShare")),
                    red_zone_targets=safe_int(data["receiving"].get("redZoneTargets")),
                )

            defense = None
            if data.get("defense"):
                defense = PFFDefensiveGrades(
                    overall_grade=safe_float(data["defense"].get("overallGrade")),
                    pass_rush_grade=safe_float(data["defense"].get("passRushGrade")),
                    run_defense_grade=safe_float(
                        data["defense"].get("runDefenseGrade")
                    ),
                    coverage_grade=safe_float(data["defense"].get("coverageGrade")),
                    tackling_grade=safe_float(data["defense"].get("tacklingGrade")),
                    pass_rush_win_rate=safe_float(
                        data["defense"].get("passRushWinRate")
                    ),
                    pressure_rate=safe_float(data["defense"].get("pressureRate")),
                    run_stop_rate=safe_float(data["defense"].get("runStopRate")),
                    missed_tackle_rate=safe_float(
                        data["defense"].get("missedTackleRate")
                    ),
                    yards_per_coverage_snap=safe_float(
                        data["defense"].get("yardsPerCoverageSnap")
                    ),
                    passer_rating_allowed=safe_float(
                        data["defense"].get("passerRatingAllowed")
                    ),
                    forced_fumbles=safe_int(data["defense"].get("forcedFumbles")),
                    batted_passes=safe_int(data["defense"].get("battedPasses")),
                )

            special_teams = None
            if data.get("specialTeams"):
                special_teams = PFFSpecialTeamsGrades(
                    overall_grade=safe_float(data["specialTeams"].get("overallGrade")),
                    kicking_grade=safe_float(data["specialTeams"].get("kickingGrade")),
                    punting_grade=safe_float(data["specialTeams"].get("puntingGrade")),
                    return_grade=safe_float(data["specialTeams"].get("returnGrade")),
                    coverage_grade=safe_float(
                        data["specialTeams"].get("coverageGrade")
                    ),
                    field_goal_percentage=safe_float(
                        data["specialTeams"].get("fieldGoalPercentage")
                    ),
                    extra_point_percentage=safe_float(
                        data["specialTeams"].get("extraPointPercentage")
                    ),
                    punt_net_average=safe_float(
                        data["specialTeams"].get("puntNetAverage")
                    ),
                    touchback_percentage=safe_float(
                        data["specialTeams"].get("touchbackPercentage")
                    ),
                    return_average=safe_float(
                        data["specialTeams"].get("returnAverage")
                    ),
                    long_return=safe_int(data["specialTeams"].get("longReturn")),
                )

            return PFFPlayerGrades(
                player_id=str(data.get("playerId", "")),
                pff_id=str(data.get("pffId", "")),
                season=safe_int(data.get("season")) or 0,
                week=safe_int(data.get("week")),
                team=clean_text(data.get("team")) or "",
                position=clean_text(data.get("position")) or "",
                overall_grade=safe_float(data.get("overallGrade")) or 0.0,
                overall_rank=safe_int(data.get("overallRank")),
                snaps_played=safe_int(data.get("snapsPlayed")) or 0,
                snap_percentage=safe_float(data.get("snapPercentage")),
                passing=passing,
                rushing=rushing,
                receiving=receiving,
                defense=defense,
                special_teams=special_teams,
            )
        except Exception:
            return None

    def _parse_player_metrics(
        self, data: Dict[str, Any], player_id: str, season: int, week: Optional[int]
    ) -> Optional[PFFPlayerMetrics]:
        """Parse player metrics from API response."""
        try:
            return PFFPlayerMetrics(
                player_id=player_id,
                season=season,
                week=week,
                third_down_grade=safe_float(data.get("thirdDownGrade")),
                red_zone_grade=safe_float(data.get("redZoneGrade")),
                two_minute_grade=safe_float(data.get("twoMinuteGrade")),
                play_action_grade=safe_float(data.get("playActionGrade")),
                under_pressure_grade=safe_float(data.get("underPressureGrade")),
                win_rate=safe_float(data.get("winRate")),
                efficiency_rating=safe_float(data.get("efficiencyRating")),
                consistency_score=safe_float(data.get("consistencyScore")),
                clutch_rating=safe_float(data.get("clutchRating")),
                injury_risk_score=safe_float(data.get("injuryRiskScore")),
                fatigue_index=safe_float(data.get("fatigueIndex")),
                durability_score=safe_float(data.get("durabilityScore")),
            )
        except Exception:
            return None

    def _parse_team_grades(
        self, data: Dict[str, Any], team_id: str, season: int, week: Optional[int]
    ) -> Optional[PFFTeamGrades]:
        """Parse team grades from API response."""
        try:
            return PFFTeamGrades(
                team_id=team_id,
                season=season,
                week=week,
                overall_offense_grade=safe_float(data.get("overallOffenseGrade"))
                or 0.0,
                overall_defense_grade=safe_float(data.get("overallDefenseGrade"))
                or 0.0,
                overall_special_teams_grade=safe_float(
                    data.get("overallSpecialTeamsGrade")
                )
                or 0.0,
                passing_offense_grade=safe_float(data.get("passingOffenseGrade")),
                rushing_offense_grade=safe_float(data.get("rushingOffenseGrade")),
                offensive_line_grade=safe_float(data.get("offensiveLineGrade")),
                pass_defense_grade=safe_float(data.get("passDefenseGrade")),
                run_defense_grade=safe_float(data.get("runDefenseGrade")),
                pass_rush_grade=safe_float(data.get("passRushGrade")),
                coverage_grade=safe_float(data.get("coverageGrade")),
                pressure_rate=safe_float(data.get("pressureRate")),
                pressure_allowed_rate=safe_float(data.get("pressureAllowedRate")),
                explosive_play_rate=safe_float(data.get("explosivePlayRate")),
                red_zone_efficiency=safe_float(data.get("redZoneEfficiency")),
                third_down_conversion_rate=safe_float(
                    data.get("thirdDownConversionRate")
                ),
                turnover_margin=safe_int(data.get("turnoverMargin")),
            )
        except Exception:
            return None

    def _parse_player(self, data: Dict[str, Any]) -> Optional[PFFPlayer]:
        """Parse player data from API response."""
        try:
            return PFFPlayer(
                id=str(data.get("id", "")),
                pff_id=str(data.get("pffId", "")),
                name=clean_text(data.get("name")) or "",
                team_id=clean_text(data.get("teamId")),
                position=clean_text(data.get("position")),
                jersey_number=safe_int(data.get("jerseyNumber")),
                height=clean_text(data.get("height")),
                weight=safe_int(data.get("weight")),
                age=safe_int(data.get("age")),
                college=clean_text(data.get("college")),
                years_pro=safe_int(data.get("yearsPro")),
                draft_year=safe_int(data.get("draftYear")),
                draft_round=safe_int(data.get("draftRound")),
                draft_pick=safe_int(data.get("draftPick")),
                photo_url=clean_text(data.get("photoUrl")),
                contract_value=safe_float(data.get("contractValue")),
                status=clean_text(data.get("status")),
            )
        except Exception:
            return None

    def _parse_season_summary(
        self, data: Dict[str, Any], player_id: str, season: int
    ) -> Optional[PFFSeasonSummary]:
        """Parse season summary from API response."""
        try:
            return PFFSeasonSummary(
                player_id=player_id,
                season=season,
                team=clean_text(data.get("team")) or "",
                position=clean_text(data.get("position")) or "",
                games_played=safe_int(data.get("gamesPlayed")) or 0,
                snaps_played=safe_int(data.get("snapsPlayed")) or 0,
                overall_grade=safe_float(data.get("overallGrade")) or 0.0,
                position_rank=safe_int(data.get("positionRank")),
                pff_all_pro=clean_text(data.get("pffAllPro")),
                team_of_the_week_awards=safe_int(data.get("teamOfTheWeekAwards")),
                player_of_the_week_awards=safe_int(data.get("playerOfTheWeekAwards")),
                highest_graded_game=safe_float(data.get("highestGradedGame")),
                lowest_graded_game=safe_float(data.get("lowestGradedGame")),
                consistency_rating=safe_float(data.get("consistencyRating")),
                passing_grade=safe_float(data.get("passingGrade")),
                rushing_grade=safe_float(data.get("rushingGrade")),
                receiving_grade=safe_float(data.get("receivingGrade")),
                pass_blocking_grade=safe_float(data.get("passBlockingGrade")),
                run_blocking_grade=safe_float(data.get("runBlockingGrade")),
                coverage_grade=safe_float(data.get("coverageGrade")),
                pass_rush_grade=safe_float(data.get("passRushGrade")),
                run_defense_grade=safe_float(data.get("runDefenseGrade")),
                tackling_grade=safe_float(data.get("tacklingGrade")),
            )
        except Exception:
            return None

    def _parse_draft_prospect(self, data: Dict[str, Any]) -> Optional[PFFDraftProspect]:
        """Parse draft prospect from API response."""
        try:
            return PFFDraftProspect(
                prospect_id=str(data.get("id", "")),
                name=clean_text(data.get("name")) or "",
                position=clean_text(data.get("position")) or "",
                college=clean_text(data.get("college")) or "",
                height=clean_text(data.get("height")),
                weight=safe_int(data.get("weight")),
                age=safe_int(data.get("age")),
                pff_grade=safe_float(data.get("pffGrade")) or 0.0,
                draft_ranking=safe_int(data.get("draftRanking")),
                position_ranking=safe_int(data.get("positionRanking")),
                round_projection=safe_int(data.get("roundProjection")),
                strengths=data.get("strengths", []),
                weaknesses=data.get("weaknesses", []),
                comparison=clean_text(data.get("comparison")),
                college_grade=safe_float(data.get("collegeGrade")),
                college_production=data.get("collegeProduction"),
                forty_yard_dash=safe_float(data.get("fortyYardDash")),
                bench_press=safe_int(data.get("benchPress")),
                vertical_jump=safe_float(data.get("verticalJump")),
                broad_jump=safe_float(data.get("broadJump")),
                three_cone=safe_float(data.get("threeCone")),
                twenty_yard_shuttle=safe_float(data.get("twentyYardShuffle")),
            )
        except Exception:
            return None

    def _parse_mock_draft_pick(
        self, data: Dict[str, Any], year: int
    ) -> Optional[PFFMockDraft]:
        """Parse mock draft pick from API response."""
        try:
            prospect_data = data.get("prospect", {})
            prospect = (
                self._parse_draft_prospect(prospect_data) if prospect_data else None
            )

            if not prospect:
                return None

            return PFFMockDraft(
                year=year,
                round=safe_int(data.get("round")) or 0,
                pick=safe_int(data.get("pick")) or 0,
                overall_pick=safe_int(data.get("overallPick")) or 0,
                team=clean_text(data.get("team")) or "",
                prospect=prospect,
                analysis=clean_text(data.get("analysis")),
                trade_details=data.get("tradeDetails"),
                need_addressed=clean_text(data.get("needAddressed")),
                grade=clean_text(data.get("grade")),
            )
        except Exception:
            return None

    def _parse_injury_report(self, data: Dict[str, Any]) -> Optional[PFFInjuryReport]:
        """Parse injury report from API response."""
        try:
            return PFFInjuryReport(
                player_id=str(data.get("playerId", "")),
                injury_type=clean_text(data.get("injuryType")) or "",
                severity=clean_text(data.get("severity")) or "",
                expected_recovery_time=clean_text(data.get("expectedRecoveryTime")),
                games_missed_projection=safe_int(data.get("gamesMissedProjection")),
                performance_impact=clean_text(data.get("performanceImpact")),
                positional_impact=data.get("positionalImpact"),
                team_impact=clean_text(data.get("teamImpact")),
                similar_injuries=data.get("similarInjuries", []),
                recovery_timeline=data.get("recoveryTimeline"),
                risk_factors=data.get("riskFactors", []),
            )
        except Exception:
            return None
