"""Pro Football Reference specific data models."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import Field

from ..core.models import BaseModel, Game, Player, PlayerStats


class PFRPlayer(Player):
    """Pro Football Reference player model with additional historical data."""

    birth_date: Optional[datetime] = Field(None, description="Player birth date")
    height_inches: Optional[int] = Field(None, description="Player height in inches")
    weight: Optional[int] = Field(None, description="Player weight in pounds")
    college: Optional[str] = Field(None, description="College attended")
    draft_year: Optional[int] = Field(None, description="NFL draft year")
    draft_round: Optional[int] = Field(None, description="Draft round")
    draft_pick: Optional[int] = Field(None, description="Draft pick number")
    career_start: Optional[int] = Field(None, description="First NFL season")
    career_end: Optional[int] = Field(None, description="Last NFL season")
    hall_of_fame: Optional[bool] = Field(None, description="Hall of Fame inductee")
    pro_bowls: Optional[int] = Field(None, description="Number of Pro Bowl selections")
    all_pros: Optional[int] = Field(None, description="Number of All-Pro selections")


class PFRPlayerStats(PlayerStats):
    """Pro Football Reference player statistics with comprehensive data."""

    # Passing stats
    pass_completions: Optional[int] = Field(None, description="Pass completions")
    pass_attempts: Optional[int] = Field(None, description="Pass attempts")
    pass_yards: Optional[int] = Field(None, description="Passing yards")
    pass_touchdowns: Optional[int] = Field(None, description="Passing touchdowns")
    interceptions: Optional[int] = Field(None, description="Interceptions thrown")
    passer_rating: Optional[float] = Field(None, description="Passer rating")
    qbr: Optional[float] = Field(None, description="QB rating")
    sacks_taken: Optional[int] = Field(None, description="Sacks taken")
    sack_yards_lost: Optional[int] = Field(None, description="Yards lost to sacks")

    # Rushing stats
    rush_attempts: Optional[int] = Field(None, description="Rushing attempts")
    rush_yards: Optional[int] = Field(None, description="Rushing yards")
    rush_touchdowns: Optional[int] = Field(None, description="Rushing touchdowns")
    rush_long: Optional[int] = Field(None, description="Longest rush")
    rush_yards_per_attempt: Optional[float] = Field(None, description="Yards per rushing attempt")

    # Receiving stats
    receptions: Optional[int] = Field(None, description="Receptions")
    receiving_yards: Optional[int] = Field(None, description="Receiving yards")
    receiving_touchdowns: Optional[int] = Field(None, description="Receiving touchdowns")
    targets: Optional[int] = Field(None, description="Targets")
    receiving_long: Optional[int] = Field(None, description="Longest reception")
    yards_per_reception: Optional[float] = Field(None, description="Yards per reception")
    catch_percentage: Optional[float] = Field(None, description="Catch percentage")

    # Defensive stats
    tackles_solo: Optional[int] = Field(None, description="Solo tackles")
    tackles_assisted: Optional[int] = Field(None, description="Assisted tackles")
    tackles_total: Optional[int] = Field(None, description="Total tackles")
    tackles_for_loss: Optional[int] = Field(None, description="Tackles for loss")
    sacks: Optional[float] = Field(None, description="Sacks")
    quarterback_hits: Optional[int] = Field(None, description="QB hits")
    interceptions_defense: Optional[int] = Field(None, description="Interceptions (defense)")
    passes_defended: Optional[int] = Field(None, description="Passes defended")
    fumbles_forced: Optional[int] = Field(None, description="Fumbles forced")
    fumbles_recovered: Optional[int] = Field(None, description="Fumbles recovered")
    defensive_touchdowns: Optional[int] = Field(None, description="Defensive touchdowns")

    # Special teams stats
    field_goals_made: Optional[int] = Field(None, description="Field goals made")
    field_goals_attempted: Optional[int] = Field(None, description="Field goals attempted")
    field_goal_percentage: Optional[float] = Field(None, description="Field goal percentage")
    extra_points_made: Optional[int] = Field(None, description="Extra points made")
    extra_points_attempted: Optional[int] = Field(None, description="Extra points attempted")
    punts: Optional[int] = Field(None, description="Punts")
    punt_yards: Optional[int] = Field(None, description="Punt yards")
    punt_average: Optional[float] = Field(None, description="Punt average")
    punt_long: Optional[int] = Field(None, description="Longest punt")

    # Advanced stats
    approximate_value: Optional[float] = Field(None, description="Approximate Value (AV)")
    games_started: Optional[int] = Field(None, description="Games started")
    snap_count: Optional[int] = Field(None, description="Snap count")
    snap_percentage: Optional[float] = Field(None, description="Snap percentage")


class PFRTeamStats(BaseModel):
    """Pro Football Reference team statistics."""

    team_id: str = Field(..., description="Team identifier")
    season: int = Field(..., description="Season year")
    games_played: Optional[int] = Field(None, description="Games played")
    wins: Optional[int] = Field(None, description="Wins")
    losses: Optional[int] = Field(None, description="Losses")
    ties: Optional[int] = Field(None, description="Ties")
    win_percentage: Optional[float] = Field(None, description="Win percentage")

    # Offensive stats
    points_for: Optional[int] = Field(None, description="Points scored")
    total_yards: Optional[int] = Field(None, description="Total offensive yards")
    passing_yards: Optional[int] = Field(None, description="Passing yards")
    rushing_yards: Optional[int] = Field(None, description="Rushing yards")
    first_downs: Optional[int] = Field(None, description="First downs")
    turnovers: Optional[int] = Field(None, description="Turnovers committed")

    # Defensive stats
    points_against: Optional[int] = Field(None, description="Points allowed")
    total_yards_allowed: Optional[int] = Field(None, description="Total yards allowed")
    passing_yards_allowed: Optional[int] = Field(None, description="Passing yards allowed")
    rushing_yards_allowed: Optional[int] = Field(None, description="Rushing yards allowed")
    takeaways: Optional[int] = Field(None, description="Takeaways forced")
    sacks: Optional[int] = Field(None, description="Sacks")

    # Special teams
    field_goal_percentage: Optional[float] = Field(None, description="Field goal percentage")
    punt_average: Optional[float] = Field(None, description="Punt average")
    return_touchdowns: Optional[int] = Field(None, description="Return touchdowns")

    # Advanced metrics
    strength_of_schedule: Optional[float] = Field(None, description="Strength of schedule")
    point_differential: Optional[int] = Field(None, description="Point differential")
    pythagorean_wins: Optional[float] = Field(None, description="Pythagorean win expectation")


class PFRGame(Game):
    """Pro Football Reference game model with additional historical data."""

    attendance: Optional[int] = Field(None, description="Game attendance")
    weather_conditions: Optional[str] = Field(None, description="Weather conditions")
    temperature: Optional[int] = Field(None, description="Temperature")
    wind_speed: Optional[int] = Field(None, description="Wind speed")
    dome: Optional[bool] = Field(None, description="Played in dome")
    playoff_game: Optional[bool] = Field(None, description="Playoff game")
    overtime: Optional[bool] = Field(None, description="Overtime game")
    home_team_record: Optional[str] = Field(None, description="Home team record before game")
    away_team_record: Optional[str] = Field(None, description="Away team record before game")
    spread: Optional[float] = Field(None, description="Point spread")
    over_under: Optional[float] = Field(None, description="Over/under total")


class PFRDraftPick(BaseModel):
    """Pro Football Reference draft pick information."""

    year: int = Field(..., description="Draft year")
    round: int = Field(..., description="Draft round")
    pick: int = Field(..., description="Pick number")
    overall_pick: int = Field(..., description="Overall pick number")
    team: str = Field(..., description="Drafting team")
    player_name: str = Field(..., description="Player name")
    position: str = Field(..., description="Player position")
    college: Optional[str] = Field(None, description="College")
    approximate_value: Optional[float] = Field(None, description="Career Approximate Value")
    years_played: Optional[int] = Field(None, description="Years in NFL")


class PFRSeasonStats(BaseModel):
    """Season-level statistics aggregation."""

    player_id: str = Field(..., description="Player identifier")
    season: int = Field(..., description="Season year")
    team: str = Field(..., description="Team abbreviation")
    age: Optional[int] = Field(None, description="Player age during season")
    position: str = Field(..., description="Position played")
    games_played: int = Field(..., description="Games played")
    games_started: Optional[int] = Field(None, description="Games started")
    stats: PFRPlayerStats = Field(..., description="Season statistics")
    awards: List[str] = Field(default_factory=list, description="Awards received")


class PFRCareerStats(BaseModel):
    """Career statistics summary."""

    player_id: str = Field(..., description="Player identifier")
    seasons: List[PFRSeasonStats] = Field(default_factory=list, description="Season-by-season stats")
    career_totals: PFRPlayerStats = Field(..., description="Career total statistics")
    career_averages: PFRPlayerStats = Field(..., description="Career average statistics")
    hall_of_fame: bool = Field(False, description="Hall of Fame inductee")
    retired: bool = Field(False, description="Retired status")
    retirement_year: Optional[int] = Field(None, description="Retirement year")