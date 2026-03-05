"""NGS Content entity models for charts, highlights, and chart players."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel

from .ngs_play import NgsPlay
from .player import Player


class NgsChart(BaseModel):
    """A player chart (route, pass, or carry)."""

    image_name: Annotated[Optional[str], pydantic.Field(alias="imageName")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    player_name_slug: Annotated[
        Optional[str], pydantic.Field(alias="playerNameSlug")
    ] = None
    position: Optional[str] = None
    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    week: Optional[int] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    timestamp: Optional[int] = None
    type: Optional[str] = None
    headshot: Optional[str] = None
    small_img: Annotated[Optional[str], pydantic.Field(alias="smallImg")] = None
    medium_img: Annotated[Optional[str], pydantic.Field(alias="mediumImg")] = None
    large_img: Annotated[Optional[str], pydantic.Field(alias="largeImg")] = None
    extra_large_img: Annotated[Optional[str], pydantic.Field(alias="extraLargeImg")] = (
        None
    )
    # Route chart specific
    receiving_yards: Annotated[
        Optional[int], pydantic.Field(alias="receivingYards")
    ] = None
    receptions: Optional[int] = None
    # Carry chart specific
    carries: Optional[int] = None
    rushing_yards: Annotated[Optional[int], pydantic.Field(alias="rushingYards")] = None
    # Pass chart specific
    attempts: Optional[int] = None
    completions: Optional[int] = None
    completion_percentage: Annotated[
        Optional[float], pydantic.Field(alias="completionPercentage")
    ] = None
    passing_yards: Annotated[Optional[int], pydantic.Field(alias="passingYards")] = None
    interceptions: Optional[int] = None
    passer_rating: Annotated[Optional[float], pydantic.Field(alias="passerRating")] = (
        None
    )
    # Common
    touchdowns: Optional[int] = None


class NgsChartPlayer(BaseModel):
    """A player available in the chart system."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None


class NgsHighlight(BaseModel):
    """A play highlight."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    play_id: Annotated[Optional[int], pydantic.Field(alias="playId")] = None
    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    week: Optional[int] = None
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    play: Optional[NgsPlay] = None
    players: Optional[List[Player]] = None
