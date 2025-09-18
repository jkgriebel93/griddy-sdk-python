"""ESPN-specific data models."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import Field

from ..core.models import BaseModel, Game, Team, Player, PlayerStats


class ESPNGame(Game):
    """ESPN-specific game model with live data features."""

    espn_id: Optional[str] = Field(None, description="ESPN game ID")
    broadcast_network: Optional[str] = Field(None, description="TV broadcast network")
    venue_name: Optional[str] = Field(None, description="Stadium/venue name")
    venue_city: Optional[str] = Field(None, description="Venue city")
    venue_state: Optional[str] = Field(None, description="Venue state")
    attendance: Optional[int] = Field(None, description="Game attendance")
    temperature: Optional[int] = Field(None, description="Temperature in Fahrenheit")
    weather_description: Optional[str] = Field(None, description="Weather description")
    wind: Optional[str] = Field(None, description="Wind conditions")
    is_neutral_site: Optional[bool] = Field(None, description="Neutral site game")
    conference_game: Optional[bool] = Field(None, description="Conference game")
    playoff_game: Optional[bool] = Field(None, description="Playoff game")
    odds: Optional[Dict[str, Any]] = Field(None, description="Betting odds")
    predictions: Optional[Dict[str, Any]] = Field(None, description="ESPN predictions")


class ESPNTeam(Team):
    """ESPN-specific team model."""

    espn_id: Optional[str] = Field(None, description="ESPN team ID")
    display_name: Optional[str] = Field(None, description="Team display name")
    short_display_name: Optional[str] = Field(None, description="Short display name")
    color: Optional[str] = Field(None, description="Primary team color")
    alternate_color: Optional[str] = Field(None, description="Alternate team color")
    logo: Optional[str] = Field(None, description="Team logo URL")
    record: Optional[str] = Field(None, description="Team record (W-L-T)")
    standing: Optional[int] = Field(None, description="Division standing")
    playoff_seed: Optional[int] = Field(None, description="Playoff seed")
    is_active: Optional[bool] = Field(None, description="Team active status")


class ESPNPlayer(Player):
    """ESPN-specific player model."""

    espn_id: Optional[str] = Field(None, description="ESPN player ID")
    display_name: Optional[str] = Field(None, description="Player display name")
    short_name: Optional[str] = Field(None, description="Player short name")
    weight: Optional[int] = Field(None, description="Player weight")
    height: Optional[str] = Field(None, description="Player height")
    age: Optional[int] = Field(None, description="Player age")
    experience: Optional[str] = Field(None, description="Years of experience")
    birth_place: Optional[str] = Field(None, description="Birth place")
    college: Optional[str] = Field(None, description="College")
    salary: Optional[float] = Field(None, description="Player salary")
    headshot: Optional[str] = Field(None, description="Player headshot URL")
    jersey: Optional[str] = Field(None, description="Jersey number")
    active: Optional[bool] = Field(None, description="Active roster status")
    injured: Optional[bool] = Field(None, description="Injury status")
    injury_status: Optional[str] = Field(None, description="Injury details")


class ESPNPlayerStats(PlayerStats):
    """ESPN-specific player statistics."""

    # Passing stats
    passing_completions: Optional[int] = Field(None, description="Pass completions")
    passing_attempts: Optional[int] = Field(None, description="Pass attempts")
    passing_yards: Optional[int] = Field(None, description="Passing yards")
    passing_touchdowns: Optional[int] = Field(None, description="Passing touchdowns")
    passing_interceptions: Optional[int] = Field(None, description="Interceptions")
    passing_rating: Optional[float] = Field(None, description="Passer rating")
    passing_long: Optional[int] = Field(None, description="Longest pass")
    sacks: Optional[int] = Field(None, description="Sacks taken")

    # Rushing stats
    rushing_attempts: Optional[int] = Field(None, description="Rushing attempts")
    rushing_yards: Optional[int] = Field(None, description="Rushing yards")
    rushing_touchdowns: Optional[int] = Field(None, description="Rushing touchdowns")
    rushing_long: Optional[int] = Field(None, description="Longest rush")
    rushing_average: Optional[float] = Field(None, description="Yards per carry")

    # Receiving stats
    receiving_receptions: Optional[int] = Field(None, description="Receptions")
    receiving_yards: Optional[int] = Field(None, description="Receiving yards")
    receiving_touchdowns: Optional[int] = Field(
        None, description="Receiving touchdowns"
    )
    receiving_targets: Optional[int] = Field(None, description="Targets")
    receiving_long: Optional[int] = Field(None, description="Longest reception")
    receiving_average: Optional[float] = Field(None, description="Yards per reception")

    # Defensive stats
    total_tackles: Optional[int] = Field(None, description="Total tackles")
    solo_tackles: Optional[int] = Field(None, description="Solo tackles")
    sacks_defense: Optional[float] = Field(None, description="Sacks (defense)")
    tackles_for_loss: Optional[int] = Field(None, description="Tackles for loss")
    quarterback_hits: Optional[int] = Field(None, description="QB hits")
    interceptions_defense: Optional[int] = Field(None, description="Interceptions")
    passes_defended: Optional[int] = Field(None, description="Passes defended")
    fumbles_forced: Optional[int] = Field(None, description="Fumbles forced")
    fumbles_recovered: Optional[int] = Field(None, description="Fumbles recovered")
    safeties: Optional[int] = Field(None, description="Safeties")
    touchdowns_defense: Optional[int] = Field(None, description="Defensive touchdowns")

    # Kicking stats
    field_goals_made: Optional[int] = Field(None, description="Field goals made")
    field_goals_attempted: Optional[int] = Field(
        None, description="Field goals attempted"
    )
    field_goal_percentage: Optional[float] = Field(None, description="FG percentage")
    extra_points_made: Optional[int] = Field(None, description="Extra points made")
    extra_points_attempted: Optional[int] = Field(
        None, description="Extra points attempted"
    )
    long_field_goal: Optional[int] = Field(None, description="Longest field goal")

    # Punting stats
    punts: Optional[int] = Field(None, description="Number of punts")
    punt_yards: Optional[int] = Field(None, description="Punt yards")
    punt_average: Optional[float] = Field(None, description="Punt average")
    punt_long: Optional[int] = Field(None, description="Longest punt")
    punts_inside_20: Optional[int] = Field(None, description="Punts inside 20")

    # Return stats
    kick_return_attempts: Optional[int] = Field(
        None, description="Kick return attempts"
    )
    kick_return_yards: Optional[int] = Field(None, description="Kick return yards")
    kick_return_touchdowns: Optional[int] = Field(None, description="Kick return TDs")
    kick_return_long: Optional[int] = Field(None, description="Longest kick return")
    punt_return_attempts: Optional[int] = Field(
        None, description="Punt return attempts"
    )
    punt_return_yards: Optional[int] = Field(None, description="Punt return yards")
    punt_return_touchdowns: Optional[int] = Field(None, description="Punt return TDs")
    punt_return_long: Optional[int] = Field(None, description="Longest punt return")


class ESPNScoreboard(BaseModel):
    """ESPN scoreboard with multiple games."""

    date: datetime = Field(..., description="Scoreboard date")
    league: str = Field(..., description="League (NFL)")
    season: int = Field(..., description="Season year")
    season_type: str = Field(..., description="Season type")
    week: Optional[int] = Field(None, description="Week number")
    games: List[ESPNGame] = Field(default_factory=list, description="List of games")


class ESPNStandings(BaseModel):
    """ESPN standings information."""

    season: int = Field(..., description="Season year")
    season_type: str = Field(..., description="Season type")
    groups: List[Dict[str, Any]] = Field(
        default_factory=list, description="Standings groups"
    )


class ESPNNews(BaseModel):
    """ESPN news article."""

    id: str = Field(..., description="Article ID")
    headline: str = Field(..., description="Article headline")
    description: Optional[str] = Field(None, description="Article description")
    story: Optional[str] = Field(None, description="Full article text")
    published: Optional[datetime] = Field(None, description="Publication date")
    last_modified: Optional[datetime] = Field(None, description="Last modified date")
    premium: Optional[bool] = Field(None, description="Premium content")
    links: Optional[Dict[str, str]] = Field(None, description="Related links")
    categories: List[str] = Field(
        default_factory=list, description="Article categories"
    )
    keywords: List[str] = Field(default_factory=list, description="Article keywords")
    byline: Optional[str] = Field(None, description="Article byline")
    images: List[Dict[str, Any]] = Field(
        default_factory=list, description="Article images"
    )
    video: Optional[Dict[str, Any]] = Field(None, description="Associated video")


class ESPNAthlete(BaseModel):
    """ESPN athlete profile."""

    id: str = Field(..., description="Athlete ID")
    guid: Optional[str] = Field(None, description="Athlete GUID")
    uid: Optional[str] = Field(None, description="Athlete UID")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    full_name: str = Field(..., description="Full name")
    display_name: str = Field(..., description="Display name")
    short_name: str = Field(..., description="Short name")
    weight: Optional[float] = Field(None, description="Weight")
    display_weight: Optional[str] = Field(None, description="Display weight")
    height: Optional[float] = Field(None, description="Height")
    display_height: Optional[str] = Field(None, description="Display height")
    age: Optional[int] = Field(None, description="Age")
    date_of_birth: Optional[datetime] = Field(None, description="Date of birth")
    birth_place: Optional[Dict[str, str]] = Field(None, description="Birth place")
    college: Optional[Dict[str, Any]] = Field(None, description="College info")
    slug: Optional[str] = Field(None, description="URL slug")
    headshot: Optional[Dict[str, str]] = Field(None, description="Headshot URLs")
    jersey: Optional[str] = Field(None, description="Jersey number")
    position: Optional[Dict[str, Any]] = Field(None, description="Position info")
    team: Optional[Dict[str, Any]] = Field(None, description="Team info")
    status: Optional[Dict[str, Any]] = Field(None, description="Status info")
    statistics: List[Dict[str, Any]] = Field(
        default_factory=list, description="Career statistics"
    )


class ESPNEvent(BaseModel):
    """ESPN event (game) detailed information."""

    id: str = Field(..., description="Event ID")
    uid: Optional[str] = Field(None, description="Event UID")
    date: datetime = Field(..., description="Event date")
    name: str = Field(..., description="Event name")
    short_name: str = Field(..., description="Event short name")
    season: Dict[str, Any] = Field(..., description="Season info")
    week: Optional[Dict[str, Any]] = Field(None, description="Week info")
    competitions: List[Dict[str, Any]] = Field(
        default_factory=list, description="Competition details"
    )
    links: List[Dict[str, Any]] = Field(
        default_factory=list, description="Related links"
    )
    weather: Optional[Dict[str, Any]] = Field(None, description="Weather conditions")
    status: Dict[str, Any] = Field(..., description="Event status")
    broadcasts: List[Dict[str, Any]] = Field(
        default_factory=list, description="Broadcast info"
    )
    odds: List[Dict[str, Any]] = Field(default_factory=list, description="Betting odds")
