"""NFL-specific data models."""

from datetime import datetime
from pydantic import Field

from ..core.models import BaseModel, Game, Team, Player, PlayerStats


class NFLGame(Game):
    """NFL-specific game model."""

    quarter: int | None = Field(None, description="Current quarter")
    time_remaining: str | None = Field(None, description="Time remaining in quarter")
    possession: str | None = Field(None, description="Team with possession")
    down: int | None = Field(None, description="Current down")
    distance: int | None = Field(None, description="Yards to go")
    yard_line: str | None = Field(None, description="Field position")
    redzone: bool | None = Field(None, description="Team in red zone")
    weather: str | None = Field(None, description="Weather conditions")
    temperature: int | None = Field(None, description="Temperature in Fahrenheit")
    wind: str | None = Field(None, description="Wind conditions")


class NFLTeam(Team):
    """NFL-specific team model."""

    logo_url: Optional[str] = Field(None, description="Team logo URL")
    primary_color: Optional[str] = Field(None, description="Primary team color")
    secondary_color: Optional[str] = Field(None, description="Secondary team color")
    wins: Optional[int] = Field(None, description="Season wins")
    losses: Optional[int] = Field(None, description="Season losses")
    ties: Optional[int] = Field(None, description="Season ties")
    playoff_seed: Optional[int] = Field(None, description="Playoff seed")


class NFLPlayer(Player):
    """NFL-specific player model."""

    height: Optional[str] = Field(None, description="Player height")
    weight: Optional[int] = Field(None, description="Player weight in pounds")
    age: Optional[int] = Field(None, description="Player age")
    experience: Optional[int] = Field(None, description="Years of experience")
    college: Optional[str] = Field(None, description="College attended")
    rookie_year: Optional[int] = Field(None, description="Rookie season year")
    status: Optional[str] = Field(None, description="Player status (active, injured, etc.)")
    photo_url: Optional[str] = Field(None, description="Player photo URL")


class NFLPlayerStats(PlayerStats):
    """NFL-specific player statistics."""

    passing_yards: Optional[int] = Field(None, description="Passing yards")
    passing_touchdowns: Optional[int] = Field(None, description="Passing touchdowns")
    interceptions: Optional[int] = Field(None, description="Interceptions thrown")
    completions: Optional[int] = Field(None, description="Pass completions")
    attempts: Optional[int] = Field(None, description="Pass attempts")
    rushing_yards: Optional[int] = Field(None, description="Rushing yards")
    rushing_touchdowns: Optional[int] = Field(None, description="Rushing touchdowns")
    rushing_attempts: Optional[int] = Field(None, description="Rushing attempts")
    receiving_yards: Optional[int] = Field(None, description="Receiving yards")
    receiving_touchdowns: Optional[int] = Field(None, description="Receiving touchdowns")
    receptions: Optional[int] = Field(None, description="Receptions")
    targets: Optional[int] = Field(None, description="Targets")
    tackles: Optional[int] = Field(None, description="Tackles")
    sacks: Optional[float] = Field(None, description="Sacks")
    interceptions_defense: Optional[int] = Field(None, description="Interceptions (defense)")
    fumbles_forced: Optional[int] = Field(None, description="Fumbles forced")
    fumbles_recovered: Optional[int] = Field(None, description="Fumbles recovered")


class NFLSchedule(BaseModel):
    """NFL schedule information."""

    week: int = Field(..., description="Week number")
    season: int = Field(..., description="Season year")
    season_type: str = Field(..., description="Season type (regular, playoffs, etc.)")
    games: List[NFLGame] = Field(default_factory=list, description="Games in this week")


class NFLStandings(BaseModel):
    """NFL standings information."""

    conference: str = Field(..., description="Conference name")
    division: str = Field(..., description="Division name")
    teams: List[NFLTeam] = Field(default_factory=list, description="Teams in standings order")


class NFLNews(BaseModel):
    """NFL news article."""

    id: str = Field(..., description="Article ID")
    title: str = Field(..., description="Article title")
    summary: Optional[str] = Field(None, description="Article summary")
    content: Optional[str] = Field(None, description="Full article content")
    author: Optional[str] = Field(None, description="Article author")
    published_date: Optional[datetime] = Field(None, description="Publication date")
    url: Optional[str] = Field(None, description="Article URL")
    image_url: Optional[str] = Field(None, description="Article image URL")
    tags: List[str] = Field(default_factory=list, description="Article tags")
    related_players: List[str] = Field(default_factory=list, description="Related player IDs")
    related_teams: List[str] = Field(default_factory=list, description="Related team IDs")