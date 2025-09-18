"""Base models and common data structures for Griddy SDK."""

from typing import Any

from datetime import datetime
from pydantic import BaseModel as PydanticBaseModel, Field


class BaseModel(PydanticBaseModel):
    """Base model for all Griddy data structures."""

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True
        extra = "forbid"


class Game(BaseModel):
    """Represents a sports game."""

    id: str = Field(..., description="Unique identifier for the game")
    home_team: str = Field(..., description="Home team name or abbreviation")
    away_team: str = Field(..., description="Away team name or abbreviation")
    home_score: int | None = Field(None, description="Home team score")
    away_score: int | None = Field(None, description="Away team score")
    status: str = Field(..., description="Game status (scheduled, live, final, etc.)")
    start_time: datetime | None = Field(None, description="Game start time")
    week: int | None = Field(None, description="Week number")
    season: int | None = Field(None, description="Season year")
    season_type: str | None = Field(None, description="Season type (regular, playoffs, etc.)")


class Team(BaseModel):
    """Represents a sports team."""

    id: str = Field(..., description="Unique identifier for the team")
    name: str = Field(..., description="Team full name")
    abbreviation: str = Field(..., description="Team abbreviation")
    city: str | None = Field(None, description="Team city")
    conference: str | None = Field(None, description="Team conference")
    division: str | None = Field(None, description="Team division")


class Player(BaseModel):
    """Represents a sports player."""

    id: str = Field(..., description="Unique identifier for the player")
    name: str = Field(..., description="Player full name")
    team_id: str | None = Field(None, description="Current team identifier")
    position: str | None = Field(None, description="Player position")
    jersey_number: int | None = Field(None, description="Jersey number")


class PlayerStats(BaseModel):
    """Represents player statistics."""

    player_id: str = Field(..., description="Player identifier")
    game_id: str | None = Field(None, description="Game identifier")
    season: int | None = Field(None, description="Season year")
    week: int | None = Field(None, description="Week number")
    stats: dict[str, Any] = Field(default_factory=dict, description="Statistics data")


class APIResponse(BaseModel):
    """Standard API response wrapper."""

    success: bool = Field(..., description="Whether the request was successful")
    data: Any | None = Field(None, description="Response data")
    message: str | None = Field(None, description="Response message")
    error: str | None = Field(None, description="Error message if applicable")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata")