"""NGS Stats entity models for passing, receiving, and rushing statistics."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel

from .player import Player, PlayerTypedDict


class NgsPassingStatTypedDict(TypedDict):
    """NGS passing statistics for a player."""

    player_name: NotRequired[str]
    position: NotRequired[str]
    team_id: NotRequired[str]
    season: NotRequired[int]
    season_type: NotRequired[str]
    games_played: NotRequired[int]
    attempts: NotRequired[int]
    completions: NotRequired[int]
    completion_percentage: NotRequired[float]
    pass_yards: NotRequired[int]
    pass_touchdowns: NotRequired[int]
    interceptions: NotRequired[int]
    passer_rating: NotRequired[float]
    avg_time_to_throw: NotRequired[float]
    avg_air_distance: NotRequired[float]
    avg_completed_air_yards: NotRequired[float]
    avg_intended_air_yards: NotRequired[float]
    avg_air_yards_differential: NotRequired[float]
    avg_air_yards_to_sticks: NotRequired[float]
    max_air_distance: NotRequired[float]
    max_completed_air_distance: NotRequired[float]
    aggressiveness: NotRequired[float]
    expected_completion_percentage: NotRequired[float]
    completion_percentage_above_expectation: NotRequired[float]
    player: NotRequired[PlayerTypedDict]


class NgsPassingStat(BaseModel):
    """NGS passing statistics for a player."""

    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    games_played: Annotated[Optional[int], pydantic.Field(alias="gamesPlayed")] = None
    attempts: Optional[int] = None
    completions: Optional[int] = None
    completion_percentage: Annotated[
        Optional[float], pydantic.Field(alias="completionPercentage")
    ] = None
    pass_yards: Annotated[Optional[int], pydantic.Field(alias="passYards")] = None
    pass_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="passTouchdowns")
    ] = None
    interceptions: Optional[int] = None
    passer_rating: Annotated[Optional[float], pydantic.Field(alias="passerRating")] = (
        None
    )
    avg_time_to_throw: Annotated[
        Optional[float], pydantic.Field(alias="avgTimeToThrow")
    ] = None
    avg_air_distance: Annotated[
        Optional[float], pydantic.Field(alias="avgAirDistance")
    ] = None
    avg_completed_air_yards: Annotated[
        Optional[float], pydantic.Field(alias="avgCompletedAirYards")
    ] = None
    avg_intended_air_yards: Annotated[
        Optional[float], pydantic.Field(alias="avgIntendedAirYards")
    ] = None
    avg_air_yards_differential: Annotated[
        Optional[float], pydantic.Field(alias="avgAirYardsDifferential")
    ] = None
    avg_air_yards_to_sticks: Annotated[
        Optional[float], pydantic.Field(alias="avgAirYardsToSticks")
    ] = None
    max_air_distance: Annotated[
        Optional[float], pydantic.Field(alias="maxAirDistance")
    ] = None
    max_completed_air_distance: Annotated[
        Optional[float], pydantic.Field(alias="maxCompletedAirDistance")
    ] = None
    aggressiveness: Optional[float] = None
    expected_completion_percentage: Annotated[
        Optional[float], pydantic.Field(alias="expectedCompletionPercentage")
    ] = None
    completion_percentage_above_expectation: Annotated[
        Optional[float], pydantic.Field(alias="completionPercentageAboveExpectation")
    ] = None
    player: Optional[Player] = None


class NgsReceivingStatTypedDict(TypedDict):
    """NGS receiving statistics for a player."""

    player_name: NotRequired[str]
    position: NotRequired[str]
    team_id: NotRequired[str]
    targets: NotRequired[int]
    receptions: NotRequired[int]
    yards: NotRequired[int]
    rec_touchdowns: NotRequired[int]
    catch_percentage: NotRequired[float]
    avg_cushion: NotRequired[float]
    avg_separation: NotRequired[float]
    avg_intended_air_yards: NotRequired[float]
    avg_yac: NotRequired[float]
    avg_expected_yac: NotRequired[float]
    avg_yac_above_expectation: NotRequired[float]
    percent_share_of_intended_air_yards: NotRequired[float]
    player: NotRequired[PlayerTypedDict]


class NgsReceivingStat(BaseModel):
    """NGS receiving statistics for a player."""

    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    position: Optional[str] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    targets: Optional[int] = None
    receptions: Optional[int] = None
    yards: Optional[int] = None
    rec_touchdowns: Annotated[Optional[int], pydantic.Field(alias="recTouchdowns")] = (
        None
    )
    catch_percentage: Annotated[
        Optional[float], pydantic.Field(alias="catchPercentage")
    ] = None
    avg_cushion: Annotated[Optional[float], pydantic.Field(alias="avgCushion")] = None
    avg_separation: Annotated[
        Optional[float], pydantic.Field(alias="avgSeparation")
    ] = None
    avg_intended_air_yards: Annotated[
        Optional[float], pydantic.Field(alias="avgIntendedAirYards")
    ] = None
    avg_yac: Annotated[Optional[float], pydantic.Field(alias="avgYAC")] = None
    avg_expected_yac: Annotated[
        Optional[float], pydantic.Field(alias="avgExpectedYAC")
    ] = None
    avg_yac_above_expectation: Annotated[
        Optional[float], pydantic.Field(alias="avgYACAboveExpectation")
    ] = None
    percent_share_of_intended_air_yards: Annotated[
        Optional[float], pydantic.Field(alias="percentShareOfIntendedAirYards")
    ] = None
    player: Optional[Player] = None


class NgsRushingStatTypedDict(TypedDict):
    """NGS rushing statistics for a player."""

    team_id: NotRequired[str]
    rush_attempts: NotRequired[int]
    rush_yards: NotRequired[int]
    rush_touchdowns: NotRequired[int]
    avg_rush_yards: NotRequired[float]
    avg_time_to_los: NotRequired[float]
    expected_rush_yards: NotRequired[float]
    rush_yards_over_expected: NotRequired[float]
    rush_yards_over_expected_per_att: NotRequired[float]
    rush_pct_over_expected: NotRequired[float]
    efficiency: NotRequired[float]
    percent_attempts_gte_eight_defenders: NotRequired[float]
    player: NotRequired[PlayerTypedDict]


class NgsRushingStat(BaseModel):
    """NGS rushing statistics for a player."""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    rush_attempts: Annotated[Optional[int], pydantic.Field(alias="rushAttempts")] = None
    rush_yards: Annotated[Optional[int], pydantic.Field(alias="rushYards")] = None
    rush_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="rushTouchdowns")
    ] = None
    avg_rush_yards: Annotated[Optional[float], pydantic.Field(alias="avgRushYards")] = (
        None
    )
    avg_time_to_los: Annotated[
        Optional[float], pydantic.Field(alias="avgTimeToLos")
    ] = None
    expected_rush_yards: Annotated[
        Optional[float], pydantic.Field(alias="expectedRushYards")
    ] = None
    rush_yards_over_expected: Annotated[
        Optional[float], pydantic.Field(alias="rushYardsOverExpected")
    ] = None
    rush_yards_over_expected_per_att: Annotated[
        Optional[float], pydantic.Field(alias="rushYardsOverExpectedPerAtt")
    ] = None
    rush_pct_over_expected: Annotated[
        Optional[float], pydantic.Field(alias="rushPctOverExpected")
    ] = None
    efficiency: Optional[float] = None
    percent_attempts_gte_eight_defenders: Annotated[
        Optional[float], pydantic.Field(alias="percentAttemptsGteEightDefenders")
    ] = None
    player: Optional[Player] = None
