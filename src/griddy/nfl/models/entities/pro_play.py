from typing import Annotated, List, NotRequired, Optional, TypedDict

import pydantic

from griddy.core import BaseModel
from griddy.nfl.models import PlayStat, PlayStatTypedDict
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

# --- Nested TypedDicts ---


class UnofficialPlayTypedDict(TypedDict):
    date_time_stamp_utc: str


class OffenseInfoTypedDict(TypedDict):
    offense_formation: NotRequired[str]
    personnel: str


class DefenseInfoTypedDict(TypedDict):
    defenders_in_the_box: NotRequired[int]
    personnel: str
    number_of_pass_rushers: NotRequired[int]
    man_zone_type: NotRequired[str]
    coverage_type: NotRequired[str]


class PassInfoTypedDict(TypedDict):
    air_yards: NotRequired[float]
    time_to_throw: NotRequired[float]
    was_pressure: NotRequired[bool]


class RecInfoTypedDict(TypedDict):
    route: str


# --- Nested Pydantic Models ---


class UnofficialPlay(BaseModel):
    date_time_stamp_utc: Annotated[str, pydantic.Field(alias="dateTimeStampUTC")]


class OffenseInfo(BaseModel):
    offense_formation: Annotated[
        Optional[str], pydantic.Field(alias="offenseFormation")
    ] = None
    personnel: str


class DefenseInfo(BaseModel):
    defenders_in_the_box: Annotated[
        Optional[int], pydantic.Field(alias="defendersInTheBox")
    ] = None
    personnel: str
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
    route: str


# --- Main TypedDict ---


class ProPlayTypedDict(TypedDict):
    game_id: int
    play_id: int
    down: int
    home_score: int
    is_big_play: bool
    is_stp_play: bool
    is_scoring: bool
    play_description: str
    # TODO: This should probably be an enum
    play_state: str
    play_stats: List[PlayStatTypedDict]
    play_type: str
    possession_team: str
    possession_team_id: str
    quarter: int
    season: int
    season_type: SeasonTypeEnum
    sequence: float
    unofficial_play: Optional[UnofficialPlayTypedDict]
    visitor_score: int
    week: int
    yard_line_number: Optional[int]
    yard_line_side: Optional[str]
    yards_to_go: int
    nfl_ids: List[int]
    is_marker_play: bool
    end_game_clock: NotRequired[Optional[str]]
    start_game_clock: NotRequired[Optional[str]]
    is_red_zone_play: NotRequired[bool]
    offense: NotRequired[OffenseInfoTypedDict]
    defense: NotRequired[DefenseInfoTypedDict]
    pass_info: NotRequired[PassInfoTypedDict]
    rec_info: NotRequired[RecInfoTypedDict]


# --- Main Pydantic Model ---


class ProPlay(BaseModel):
    # Required fields (always present in API response)
    game_id: Annotated[int, pydantic.Field(alias="gameId")]
    play_id: Annotated[int, pydantic.Field(alias="playId")]
    down: int
    home_score: Annotated[int, pydantic.Field(alias="homeScore")]
    is_big_play: Annotated[bool, pydantic.Field(alias="isBigPlay")]
    is_stp_play: Annotated[bool, pydantic.Field(alias="isSTPlay")]
    is_scoring: Annotated[bool, pydantic.Field(alias="isScoring")]
    play_description: Annotated[str, pydantic.Field(alias="playDescription")]
    # TODO: This should probably be an enum
    play_state: Annotated[str, pydantic.Field(alias="playState")]
    play_stats: Annotated[List[PlayStat], pydantic.Field(alias="playStats")]
    play_type: Annotated[str, pydantic.Field(alias="playType")]
    possession_team: Annotated[str, pydantic.Field(alias="possessionTeam")]
    possession_team_id: Annotated[str, pydantic.Field(alias="possessionTeamId")]
    quarter: int
    season: int
    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    sequence: float
    visitor_score: Annotated[int, pydantic.Field(alias="visitorScore")]
    week: int
    yards_to_go: Annotated[int, pydantic.Field(alias="yardsToGo")]
    nfl_ids: Annotated[List[int], pydantic.Field(alias="nflIds")]
    is_marker_play: Annotated[bool, pydantic.Field(alias="isMarkerPlay")]

    # Required but nullable (always present, value may be null)
    unofficial_play: Annotated[
        Optional[UnofficialPlay], pydantic.Field(alias="unofficialPlay")
    ]
    yard_line_number: Annotated[Optional[int], pydantic.Field(alias="yardlineNumber")]
    yard_line_side: Annotated[Optional[str], pydantic.Field(alias="yardlineSide")]

    # Conditional fields (may be absent from API response)
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
