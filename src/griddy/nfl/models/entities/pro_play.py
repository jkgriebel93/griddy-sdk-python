from typing import Annotated, List, NotRequired, Optional, TypedDict

import pydantic

from griddy.core import BaseModel
from griddy.nfl.models import PlayStat, PlayStatTypedDict
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

# --- Nested TypedDicts ---


class UnofficialPlayTypedDict(TypedDict):
    date_time_stamp_utc: NotRequired[str]


class OffenseInfoTypedDict(TypedDict):
    offense_formation: NotRequired[str]
    personnel: NotRequired[str]


class DefenseInfoTypedDict(TypedDict):
    defenders_in_the_box: NotRequired[int]
    personnel: NotRequired[str]
    number_of_pass_rushers: NotRequired[int]
    man_zone_type: NotRequired[str]
    coverage_type: NotRequired[str]


class PassInfoTypedDict(TypedDict):
    air_yards: NotRequired[float]
    time_to_throw: NotRequired[float]
    was_pressure: NotRequired[bool]


class RecInfoTypedDict(TypedDict):
    route: NotRequired[str]


# --- Nested Pydantic Models ---


class UnofficialPlay(BaseModel):
    date_time_stamp_utc: Annotated[
        Optional[str], pydantic.Field(alias="dateTimeStampUTC")
    ] = None


class OffenseInfo(BaseModel):
    offense_formation: Annotated[
        Optional[str], pydantic.Field(alias="offenseFormation")
    ] = None
    personnel: Optional[str] = None


class DefenseInfo(BaseModel):
    defenders_in_the_box: Annotated[
        Optional[int], pydantic.Field(alias="defendersInTheBox")
    ] = None
    personnel: Optional[str] = None
    number_of_pass_rushers: Annotated[
        Optional[int], pydantic.Field(alias="numberOfPassRushers")
    ] = None
    man_zone_type: Annotated[Optional[str], pydantic.Field(alias="manZoneType")] = None
    coverage_type: Annotated[Optional[str], pydantic.Field(alias="coverageType")] = None


class PassInfo(BaseModel):
    air_yards: Annotated[Optional[float], pydantic.Field(alias="airYards")] = None
    time_to_throw: Annotated[Optional[float], pydantic.Field(alias="timeToThrow")] = (
        None
    )
    was_pressure: Annotated[Optional[bool], pydantic.Field(alias="wasPressure")] = None


class RecInfo(BaseModel):
    route: Optional[str] = None


# --- Main TypedDict ---


class ProPlayTypedDict(TypedDict):
    game_id: NotRequired[int]
    play_id: NotRequired[int]
    down: NotRequired[int]
    home_score: NotRequired[int]
    is_big_play: NotRequired[bool]
    is_stp_play: NotRequired[bool]
    is_scoring: NotRequired[bool]
    play_description: NotRequired[str]
    # TODO: This should probably be an enum
    play_state: NotRequired[str]
    play_stats: NotRequired[List[PlayStatTypedDict]]
    play_type: NotRequired[str]
    possession_team: NotRequired[str]
    possession_team_id: NotRequired[str]
    quarter: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    sequence: NotRequired[float]
    unofficial_play: NotRequired[Optional[UnofficialPlayTypedDict]]
    visitor_score: NotRequired[int]
    week: NotRequired[int]
    yard_line_number: NotRequired[Optional[int]]
    yard_line_side: NotRequired[Optional[str]]
    yards_to_go: NotRequired[int]
    nfl_ids: NotRequired[List[int]]
    is_marker_play: NotRequired[bool]
    end_game_clock: NotRequired[Optional[str]]
    start_game_clock: NotRequired[Optional[str]]
    is_red_zone_play: NotRequired[bool]
    offense: NotRequired[OffenseInfoTypedDict]
    defense: NotRequired[DefenseInfoTypedDict]
    pass_info: NotRequired[PassInfoTypedDict]
    rec_info: NotRequired[RecInfoTypedDict]


# --- Main Pydantic Model ---


class ProPlay(BaseModel):
    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    play_id: Annotated[Optional[int], pydantic.Field(alias="playId")] = None
    down: Optional[int] = None
    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None
    is_big_play: Annotated[Optional[bool], pydantic.Field(alias="isBigPlay")] = None
    is_stp_play: Annotated[Optional[bool], pydantic.Field(alias="isSTPlay")] = None
    is_scoring: Annotated[Optional[bool], pydantic.Field(alias="isScoring")] = None
    play_description: Annotated[
        Optional[str], pydantic.Field(alias="playDescription")
    ] = None
    # TODO: This should probably be an enum
    play_state: Annotated[Optional[str], pydantic.Field(alias="playState")] = None
    play_stats: Annotated[
        Optional[List[PlayStat]], pydantic.Field(alias="playStats")
    ] = None
    play_type: Annotated[Optional[str], pydantic.Field(alias="playType")] = None
    possession_team: Annotated[
        Optional[str], pydantic.Field(alias="possessionTeam")
    ] = None
    possession_team_id: Annotated[
        Optional[str], pydantic.Field(alias="possessionTeamId")
    ] = None
    quarter: Optional[int] = None
    season: Optional[int] = None
    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    sequence: Optional[float] = None
    visitor_score: Annotated[Optional[int], pydantic.Field(alias="visitorScore")] = None
    week: Optional[int] = None
    yards_to_go: Annotated[Optional[int], pydantic.Field(alias="yardsToGo")] = None
    nfl_ids: Annotated[Optional[List[int]], pydantic.Field(alias="nflIds")] = None
    is_marker_play: Annotated[Optional[bool], pydantic.Field(alias="isMarkerPlay")] = (
        None
    )
    unofficial_play: Annotated[
        Optional[UnofficialPlay], pydantic.Field(alias="unofficialPlay")
    ] = None
    yard_line_number: Annotated[
        Optional[int], pydantic.Field(alias="yardlineNumber")
    ] = None
    yard_line_side: Annotated[Optional[str], pydantic.Field(alias="yardlineSide")] = (
        None
    )
    end_game_clock: Annotated[Optional[str], pydantic.Field(alias="endGameClock")] = (
        None
    )
    start_game_clock: Annotated[
        Optional[str], pydantic.Field(alias="startGameClock")
    ] = None
    is_red_zone_play: Annotated[
        Optional[bool], pydantic.Field(alias="isRedzonePlay")
    ] = None
    offense: Optional[OffenseInfo] = None
    defense: Optional[DefenseInfo] = None
    pass_info: Annotated[Optional[PassInfo], pydantic.Field(alias="passInfo")] = None
    rec_info: Annotated[Optional[RecInfo], pydantic.Field(alias="recInfo")] = None
