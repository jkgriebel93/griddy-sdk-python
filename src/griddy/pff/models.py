"""Pro Football Focus specific data models with advanced analytics."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import Field

from ..core.models import BaseModel, Player


class PFFPlayer(Player):
    """PFF player model with additional analytics data."""

    pff_id: Optional[str] = Field(None, description="PFF player ID")
    height: Optional[str] = Field(None, description="Player height")
    weight: Optional[int] = Field(None, description="Player weight in pounds")
    age: Optional[int] = Field(None, description="Player age")
    college: Optional[str] = Field(None, description="College attended")
    years_pro: Optional[int] = Field(None, description="Years as professional")
    draft_year: Optional[int] = Field(None, description="Draft year")
    draft_round: Optional[int] = Field(None, description="Draft round")
    draft_pick: Optional[int] = Field(None, description="Draft pick number")
    photo_url: Optional[str] = Field(None, description="Player photo URL")
    contract_value: Optional[float] = Field(None, description="Contract value")
    status: Optional[str] = Field(None, description="Player status")


class PFFPassingGrades(BaseModel):
    """PFF passing grades and metrics."""

    overall_grade: Optional[float] = Field(None, description="Overall passing grade")
    accuracy_grade: Optional[float] = Field(None, description="Passing accuracy grade")
    deep_ball_grade: Optional[float] = Field(
        None, description="Deep ball accuracy grade"
    )
    pocket_grade: Optional[float] = Field(None, description="Pocket presence grade")
    play_action_grade: Optional[float] = Field(None, description="Play action grade")

    # Advanced metrics
    completion_percentage_above_expectation: Optional[float] = Field(
        None, description="CPOE"
    )
    yards_per_attempt: Optional[float] = Field(None, description="Yards per attempt")
    air_yards_per_attempt: Optional[float] = Field(
        None, description="Air yards per attempt"
    )
    pressure_to_sack_rate: Optional[float] = Field(
        None, description="Pressure to sack rate"
    )
    turnover_worthy_plays: Optional[int] = Field(
        None, description="Turnover worthy plays"
    )
    big_time_throws: Optional[int] = Field(None, description="Big time throws")
    pressured_dropbacks: Optional[int] = Field(None, description="Pressured dropbacks")
    time_to_throw: Optional[float] = Field(None, description="Average time to throw")


class PFFRushingGrades(BaseModel):
    """PFF rushing grades and metrics."""

    overall_grade: Optional[float] = Field(None, description="Overall rushing grade")
    vision_grade: Optional[float] = Field(None, description="Vision grade")
    power_grade: Optional[float] = Field(None, description="Power grade")
    elusiveness_grade: Optional[float] = Field(None, description="Elusiveness grade")

    # Advanced metrics
    yards_after_contact: Optional[float] = Field(
        None, description="Yards after contact per attempt"
    )
    forced_missed_tackles: Optional[int] = Field(
        None, description="Forced missed tackles"
    )
    breakaway_runs: Optional[int] = Field(
        None, description="Breakaway runs (15+ yards)"
    )
    stuffed_runs: Optional[int] = Field(None, description="Runs stuffed at/behind LOS")
    red_zone_attempts: Optional[int] = Field(None, description="Red zone attempts")
    goal_line_attempts: Optional[int] = Field(None, description="Goal line attempts")


class PFFReceivingGrades(BaseModel):
    """PFF receiving grades and metrics."""

    overall_grade: Optional[float] = Field(None, description="Overall receiving grade")
    route_running_grade: Optional[float] = Field(
        None, description="Route running grade"
    )
    hands_grade: Optional[float] = Field(None, description="Hands/catching grade")
    contested_catch_grade: Optional[float] = Field(
        None, description="Contested catch grade"
    )

    # Advanced metrics
    separation_grade: Optional[float] = Field(None, description="Average separation")
    yards_after_catch: Optional[float] = Field(
        None, description="Yards after catch per reception"
    )
    drop_rate: Optional[float] = Field(None, description="Drop rate percentage")
    contested_catch_rate: Optional[float] = Field(
        None, description="Contested catch rate"
    )
    target_share: Optional[float] = Field(
        None, description="Team target share percentage"
    )
    air_yards_share: Optional[float] = Field(None, description="Team air yards share")
    red_zone_targets: Optional[int] = Field(None, description="Red zone targets")


class PFFDefensiveGrades(BaseModel):
    """PFF defensive grades and metrics."""

    overall_grade: Optional[float] = Field(None, description="Overall defensive grade")
    pass_rush_grade: Optional[float] = Field(None, description="Pass rush grade")
    run_defense_grade: Optional[float] = Field(None, description="Run defense grade")
    coverage_grade: Optional[float] = Field(None, description="Coverage grade")
    tackling_grade: Optional[float] = Field(None, description="Tackling grade")

    # Advanced metrics
    pass_rush_win_rate: Optional[float] = Field(None, description="Pass rush win rate")
    pressure_rate: Optional[float] = Field(None, description="Pressure rate")
    run_stop_rate: Optional[float] = Field(None, description="Run stop rate")
    missed_tackle_rate: Optional[float] = Field(None, description="Missed tackle rate")
    yards_per_coverage_snap: Optional[float] = Field(
        None, description="Yards allowed per coverage snap"
    )
    passer_rating_allowed: Optional[float] = Field(
        None, description="Passer rating allowed in coverage"
    )
    forced_fumbles: Optional[int] = Field(None, description="Forced fumbles")
    batted_passes: Optional[int] = Field(None, description="Batted passes")


class PFFSpecialTeamsGrades(BaseModel):
    """PFF special teams grades and metrics."""

    overall_grade: Optional[float] = Field(
        None, description="Overall special teams grade"
    )
    kicking_grade: Optional[float] = Field(None, description="Kicking grade")
    punting_grade: Optional[float] = Field(None, description="Punting grade")
    return_grade: Optional[float] = Field(None, description="Return grade")
    coverage_grade: Optional[float] = Field(None, description="Coverage grade")

    # Advanced metrics
    field_goal_percentage: Optional[float] = Field(
        None, description="Field goal percentage"
    )
    extra_point_percentage: Optional[float] = Field(
        None, description="Extra point percentage"
    )
    punt_net_average: Optional[float] = Field(None, description="Punt net average")
    touchback_percentage: Optional[float] = Field(
        None, description="Touchback percentage"
    )
    return_average: Optional[float] = Field(None, description="Return average")
    long_return: Optional[int] = Field(None, description="Long return")


class PFFPlayerGrades(BaseModel):
    """Comprehensive PFF player grades for a specific period."""

    player_id: str = Field(..., description="Player identifier")
    pff_id: Optional[str] = Field(None, description="PFF player ID")
    season: int = Field(..., description="Season year")
    week: Optional[int] = Field(None, description="Week number (None for season)")
    team: str = Field(..., description="Team abbreviation")
    position: str = Field(..., description="Player position")

    # Overall grades
    overall_grade: float = Field(..., description="Overall PFF grade")
    overall_rank: Optional[int] = Field(None, description="Overall position rank")
    snaps_played: int = Field(..., description="Total snaps played")
    snap_percentage: Optional[float] = Field(None, description="Snap percentage")

    # Position-specific grades
    passing: Optional[PFFPassingGrades] = Field(None, description="Passing grades")
    rushing: Optional[PFFRushingGrades] = Field(None, description="Rushing grades")
    receiving: Optional[PFFReceivingGrades] = Field(
        None, description="Receiving grades"
    )
    defense: Optional[PFFDefensiveGrades] = Field(None, description="Defensive grades")
    special_teams: Optional[PFFSpecialTeamsGrades] = Field(
        None, description="Special teams grades"
    )


class PFFPlayerMetrics(BaseModel):
    """Advanced PFF metrics and analytics."""

    player_id: str = Field(..., description="Player identifier")
    season: int = Field(..., description="Season year")
    week: Optional[int] = Field(None, description="Week number")

    # Situational performance
    third_down_grade: Optional[float] = Field(
        None, description="Third down performance grade"
    )
    red_zone_grade: Optional[float] = Field(
        None, description="Red zone performance grade"
    )
    two_minute_grade: Optional[float] = Field(
        None, description="Two-minute drill grade"
    )
    play_action_grade: Optional[float] = Field(None, description="Play action grade")
    under_pressure_grade: Optional[float] = Field(
        None, description="Performance under pressure"
    )

    # Advanced analytics
    win_rate: Optional[float] = Field(None, description="Position-specific win rate")
    efficiency_rating: Optional[float] = Field(None, description="Efficiency rating")
    consistency_score: Optional[float] = Field(None, description="Consistency score")
    clutch_rating: Optional[float] = Field(
        None, description="Clutch performance rating"
    )

    # Injury and fatigue metrics
    injury_risk_score: Optional[float] = Field(
        None, description="Injury risk assessment"
    )
    fatigue_index: Optional[float] = Field(None, description="Fatigue index")
    durability_score: Optional[float] = Field(None, description="Durability score")


class PFFTeamGrades(BaseModel):
    """PFF team grades and analytics."""

    team_id: str = Field(..., description="Team identifier")
    season: int = Field(..., description="Season year")
    week: Optional[int] = Field(None, description="Week number")

    # Overall team grades
    overall_offense_grade: float = Field(..., description="Overall offensive grade")
    overall_defense_grade: float = Field(..., description="Overall defensive grade")
    overall_special_teams_grade: float = Field(
        ..., description="Overall special teams grade"
    )

    # Offensive grades by unit
    passing_offense_grade: Optional[float] = Field(
        None, description="Passing offense grade"
    )
    rushing_offense_grade: Optional[float] = Field(
        None, description="Rushing offense grade"
    )
    offensive_line_grade: Optional[float] = Field(
        None, description="Offensive line grade"
    )

    # Defensive grades by unit
    pass_defense_grade: Optional[float] = Field(None, description="Pass defense grade")
    run_defense_grade: Optional[float] = Field(None, description="Run defense grade")
    pass_rush_grade: Optional[float] = Field(None, description="Pass rush grade")
    coverage_grade: Optional[float] = Field(None, description="Coverage grade")

    # Advanced team metrics
    pressure_rate: Optional[float] = Field(None, description="Team pressure rate")
    pressure_allowed_rate: Optional[float] = Field(
        None, description="Pressure allowed rate"
    )
    explosive_play_rate: Optional[float] = Field(
        None, description="Explosive play rate"
    )
    red_zone_efficiency: Optional[float] = Field(
        None, description="Red zone efficiency"
    )
    third_down_conversion_rate: Optional[float] = Field(
        None, description="Third down conversion rate"
    )
    turnover_margin: Optional[int] = Field(None, description="Turnover margin")


class PFFSeasonSummary(BaseModel):
    """Season summary with PFF grades and awards."""

    player_id: str = Field(..., description="Player identifier")
    season: int = Field(..., description="Season year")
    team: str = Field(..., description="Primary team")
    position: str = Field(..., description="Position")

    # Season totals
    games_played: int = Field(..., description="Games played")
    snaps_played: int = Field(..., description="Total snaps")
    overall_grade: float = Field(..., description="Season overall grade")
    position_rank: Optional[int] = Field(None, description="Position rank")

    # PFF recognitions
    pff_all_pro: Optional[str] = Field(
        None, description="PFF All-Pro team (1st, 2nd, etc.)"
    )
    team_of_the_week_awards: Optional[int] = Field(
        None, description="Team of the Week awards"
    )
    player_of_the_week_awards: Optional[int] = Field(
        None, description="Player of the Week awards"
    )
    highest_graded_game: Optional[float] = Field(
        None, description="Highest single-game grade"
    )
    lowest_graded_game: Optional[float] = Field(
        None, description="Lowest single-game grade"
    )
    consistency_rating: Optional[float] = Field(
        None, description="Season consistency rating"
    )

    # Position-specific season grades
    passing_grade: Optional[float] = Field(None, description="Season passing grade")
    rushing_grade: Optional[float] = Field(None, description="Season rushing grade")
    receiving_grade: Optional[float] = Field(None, description="Season receiving grade")
    pass_blocking_grade: Optional[float] = Field(
        None, description="Season pass blocking grade"
    )
    run_blocking_grade: Optional[float] = Field(
        None, description="Season run blocking grade"
    )
    coverage_grade: Optional[float] = Field(None, description="Season coverage grade")
    pass_rush_grade: Optional[float] = Field(None, description="Season pass rush grade")
    run_defense_grade: Optional[float] = Field(
        None, description="Season run defense grade"
    )
    tackling_grade: Optional[float] = Field(None, description="Season tackling grade")


class PFFDraftProspect(BaseModel):
    """PFF draft prospect evaluation."""

    prospect_id: str = Field(..., description="Prospect identifier")
    name: str = Field(..., description="Player name")
    position: str = Field(..., description="Position")
    college: str = Field(..., description="College")
    height: Optional[str] = Field(None, description="Height")
    weight: Optional[int] = Field(None, description="Weight")
    age: Optional[int] = Field(None, description="Age on draft day")

    # PFF draft evaluation
    pff_grade: float = Field(..., description="PFF draft grade")
    draft_ranking: Optional[int] = Field(None, description="PFF draft ranking")
    position_ranking: Optional[int] = Field(None, description="Position ranking")
    round_projection: Optional[int] = Field(None, description="Projected draft round")

    # Strengths and weaknesses
    strengths: List[str] = Field(default_factory=list, description="Player strengths")
    weaknesses: List[str] = Field(
        default_factory=list, description="Areas for improvement"
    )
    comparison: Optional[str] = Field(None, description="NFL player comparison")

    # College performance
    college_grade: Optional[float] = Field(
        None, description="Final college season grade"
    )
    college_production: Optional[Dict[str, Any]] = Field(
        None, description="College production metrics"
    )

    # Combine and workout metrics
    forty_yard_dash: Optional[float] = Field(None, description="40-yard dash time")
    bench_press: Optional[int] = Field(None, description="Bench press reps")
    vertical_jump: Optional[float] = Field(None, description="Vertical jump inches")
    broad_jump: Optional[float] = Field(None, description="Broad jump inches")
    three_cone: Optional[float] = Field(None, description="3-cone drill time")
    twenty_yard_shuttle: Optional[float] = Field(
        None, description="20-yard shuttle time"
    )


class PFFMockDraft(BaseModel):
    """PFF mock draft results."""

    year: int = Field(..., description="Draft year")
    round: int = Field(..., description="Draft round")
    pick: int = Field(..., description="Pick number")
    overall_pick: int = Field(..., description="Overall pick number")
    team: str = Field(..., description="Selecting team")
    prospect: PFFDraftProspect = Field(..., description="Selected prospect")
    analysis: Optional[str] = Field(None, description="Pick analysis")
    trade_details: Optional[Dict[str, Any]] = Field(
        None, description="Trade details if applicable"
    )
    need_addressed: Optional[str] = Field(None, description="Team need addressed")
    grade: Optional[str] = Field(None, description="Pick grade (A+, A, B+, etc.)")


class PFFInjuryReport(BaseModel):
    """PFF injury analysis and projections."""

    player_id: str = Field(..., description="Player identifier")
    injury_type: str = Field(..., description="Type of injury")
    severity: str = Field(..., description="Injury severity (Minor, Moderate, Severe)")
    expected_recovery_time: Optional[str] = Field(
        None, description="Expected recovery timeframe"
    )
    games_missed_projection: Optional[int] = Field(
        None, description="Projected games missed"
    )

    # Impact analysis
    performance_impact: Optional[str] = Field(
        None, description="Expected performance impact"
    )
    positional_impact: Optional[Dict[str, float]] = Field(
        None, description="Impact by position group"
    )
    team_impact: Optional[str] = Field(None, description="Impact on team performance")

    # Historical context
    similar_injuries: Optional[List[Dict[str, Any]]] = Field(
        None, description="Similar injury cases"
    )
    recovery_timeline: Optional[Dict[str, str]] = Field(
        None, description="Recovery milestones"
    )
    risk_factors: Optional[List[str]] = Field(
        None, description="Risk factors for re-injury"
    )
