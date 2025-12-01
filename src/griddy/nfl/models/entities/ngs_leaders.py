"""NGS Leaders entity models for leaderboard entries."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel

from .ngs_play import NgsPlay, NgsPlayTypedDict
from .player import Player, PlayerTypedDict


class NgsSpeedLeaderTypedDict(TypedDict):
    """Leader info for speed leaderboards."""

    nfl_id: NotRequired[int]
    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    yards: NotRequired[int]
    in_play_dist: NotRequired[float]
    max_speed: NotRequired[float]
    headshot: NotRequired[str]


class NgsSpeedLeader(BaseModel):
    """Leader info for speed leaderboards."""

    nfl_id: Annotated[Optional[int], pydantic.Field(alias="nflId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    yards: Optional[int] = None
    in_play_dist: Annotated[Optional[float], pydantic.Field(alias="inPlayDist")] = None
    max_speed: Annotated[Optional[float], pydantic.Field(alias="maxSpeed")] = None
    headshot: Optional[str] = None


class NgsSpeedLeaderEntryTypedDict(TypedDict):
    """Entry in speed leaderboards."""

    leader: NotRequired[NgsSpeedLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsSpeedLeaderEntry(BaseModel):
    """Entry in speed leaderboards."""

    leader: Optional[NgsSpeedLeader] = None
    play: Optional[NgsPlay] = None


class NgsSackLeaderTypedDict(TypedDict):
    """Leader info for sack leaderboards."""

    nfl_id: NotRequired[int]
    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    time: NotRequired[float]
    season_avg: NotRequired[float]
    team_avg: NotRequired[float]
    headshot: NotRequired[str]


class NgsSackLeader(BaseModel):
    """Leader info for sack leaderboards."""

    nfl_id: Annotated[Optional[int], pydantic.Field(alias="nflId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    time: Optional[float] = None
    season_avg: Annotated[Optional[float], pydantic.Field(alias="seasonAvg")] = None
    team_avg: Annotated[Optional[float], pydantic.Field(alias="teamAvg")] = None
    headshot: Optional[str] = None


class NgsSackLeaderEntryTypedDict(TypedDict):
    """Entry in sack leaderboards."""

    leader: NotRequired[NgsSackLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsSackLeaderEntry(BaseModel):
    """Entry in sack leaderboards."""

    leader: Optional[NgsSackLeader] = None
    play: Optional[NgsPlay] = None


class NgsCompletionLeaderTypedDict(TypedDict):
    """Leader info for completion probability leaderboards."""

    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    pass_yards: NotRequired[int]
    air_yards: NotRequired[float]
    completion_probability: NotRequired[float]
    headshot: NotRequired[str]
    receiver: NotRequired[PlayerTypedDict]


class NgsCompletionLeader(BaseModel):
    """Leader info for completion probability leaderboards."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    pass_yards: Annotated[Optional[int], pydantic.Field(alias="passYards")] = None
    air_yards: Annotated[Optional[float], pydantic.Field(alias="airYards")] = None
    completion_probability: Annotated[
        Optional[float], pydantic.Field(alias="completionProbability")
    ] = None
    headshot: Optional[str] = None
    receiver: Optional[Player] = None


class NgsCompletionLeaderEntryTypedDict(TypedDict):
    """Entry in completion probability leaderboards."""

    leader: NotRequired[NgsCompletionLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsCompletionLeaderEntry(BaseModel):
    """Entry in completion probability leaderboards."""

    leader: Optional[NgsCompletionLeader] = None
    play: Optional[NgsPlay] = None


class NgsYACLeaderTypedDict(TypedDict):
    """Leader info for YAC (yards after catch) leaderboards."""

    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    rec_yards: NotRequired[int]
    air_yards: NotRequired[float]
    yards_after_catch: NotRequired[float]
    expected_yards_after_catch: NotRequired[float]
    yards_after_catch_over_expectation: NotRequired[float]
    is_touchdown: NotRequired[bool]
    headshot: NotRequired[str]


class NgsYACLeader(BaseModel):
    """Leader info for YAC (yards after catch) leaderboards."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    rec_yards: Annotated[Optional[int], pydantic.Field(alias="recYards")] = None
    air_yards: Annotated[Optional[float], pydantic.Field(alias="airYards")] = None
    yards_after_catch: Annotated[
        Optional[float], pydantic.Field(alias="yardsAfterCatch")
    ] = None
    expected_yards_after_catch: Annotated[
        Optional[float], pydantic.Field(alias="expectedYardsAfterCatch")
    ] = None
    yards_after_catch_over_expectation: Annotated[
        Optional[float], pydantic.Field(alias="yardsAfterCatchOverExpectation")
    ] = None
    is_touchdown: Annotated[Optional[bool], pydantic.Field(alias="isTouchdown")] = None
    headshot: Optional[str] = None


class NgsYACLeaderEntryTypedDict(TypedDict):
    """Entry in YAC leaderboards."""

    leader: NotRequired[NgsYACLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsYACLeaderEntry(BaseModel):
    """Entry in YAC leaderboards."""

    leader: Optional[NgsYACLeader] = None
    play: Optional[NgsPlay] = None


class NgsDistanceLeaderTypedDict(TypedDict):
    """Leader info for distance leaderboards."""

    nfl_id: NotRequired[int]
    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    yards: NotRequired[int]
    in_play_dist: NotRequired[float]
    headshot: NotRequired[str]


class NgsDistanceLeader(BaseModel):
    """Leader info for distance leaderboards."""

    nfl_id: Annotated[Optional[int], pydantic.Field(alias="nflId")] = None
    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    yards: Optional[int] = None
    in_play_dist: Annotated[Optional[float], pydantic.Field(alias="inPlayDist")] = None
    headshot: Optional[str] = None


class NgsDistanceLeaderEntryTypedDict(TypedDict):
    """Entry in distance leaderboards."""

    leader: NotRequired[NgsDistanceLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsDistanceLeaderEntry(BaseModel):
    """Entry in distance leaderboards."""

    leader: Optional[NgsDistanceLeader] = None
    play: Optional[NgsPlay] = None


class NgsTackleLeaderTypedDict(TypedDict):
    """Leader info for tackle distance leaderboards."""

    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    in_play_dist: NotRequired[float]
    distance_covered: NotRequired[float]
    headshot: NotRequired[str]


class NgsTackleLeader(BaseModel):
    """Leader info for tackle distance leaderboards."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    in_play_dist: Annotated[Optional[float], pydantic.Field(alias="inPlayDist")] = None
    distance_covered: Annotated[
        Optional[float], pydantic.Field(alias="distanceCovered")
    ] = None
    headshot: Optional[str] = None


class NgsTackleLeaderEntryTypedDict(TypedDict):
    """Entry in tackle distance leaderboards."""

    leader: NotRequired[NgsTackleLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsTackleLeaderEntry(BaseModel):
    """Entry in tackle distance leaderboards."""

    leader: Optional[NgsTackleLeader] = None
    play: Optional[NgsPlay] = None


class NgsERYLeaderTypedDict(TypedDict):
    """Leader info for expected rush yards (ERY) leaderboards."""

    esb_id: NotRequired[str]
    gsis_id: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    player_name: NotRequired[str]
    short_name: NotRequired[str]
    jersey_number: NotRequired[int]
    position: NotRequired[str]
    position_group: NotRequired[str]
    team_abbr: NotRequired[str]
    team_id: NotRequired[str]
    week: NotRequired[int]
    rush_yards: NotRequired[int]
    expected_rush_yards: NotRequired[float]
    rush_yards_over_expected: NotRequired[float]
    is_touchdown: NotRequired[bool]
    headshot: NotRequired[str]


class NgsERYLeader(BaseModel):
    """Leader info for expected rush yards (ERY) leaderboards."""

    esb_id: Annotated[Optional[str], pydantic.Field(alias="esbId")] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    first_name: Annotated[Optional[str], pydantic.Field(alias="firstName")] = None
    last_name: Annotated[Optional[str], pydantic.Field(alias="lastName")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    position: Optional[str] = None
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    team_abbr: Annotated[Optional[str], pydantic.Field(alias="teamAbbr")] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    week: Optional[int] = None
    rush_yards: Annotated[Optional[int], pydantic.Field(alias="rushYards")] = None
    expected_rush_yards: Annotated[
        Optional[float], pydantic.Field(alias="expectedRushYards")
    ] = None
    rush_yards_over_expected: Annotated[
        Optional[float], pydantic.Field(alias="rushYardsOverExpected")
    ] = None
    is_touchdown: Annotated[Optional[bool], pydantic.Field(alias="isTouchdown")] = None
    headshot: Optional[str] = None


class NgsERYLeaderEntryTypedDict(TypedDict):
    """Entry in ERY leaderboards."""

    leader: NotRequired[NgsERYLeaderTypedDict]
    play: NotRequired[NgsPlayTypedDict]


class NgsERYLeaderEntry(BaseModel):
    """Entry in ERY leaderboards."""

    leader: Optional[NgsERYLeader] = None
    play: Optional[NgsPlay] = None
