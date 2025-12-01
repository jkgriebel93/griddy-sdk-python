"""NGS Play and PlayStat entity models."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class NgsPlayStatTypedDict(TypedDict):
    """Statistics for a single play."""

    play_id: NotRequired[int]
    club_code: NotRequired[str]
    player_name: NotRequired[str]
    stat_id: NotRequired[int]
    yards: NotRequired[int]
    gsis_id: NotRequired[str]


class NgsPlayStat(BaseModel):
    """Statistics for a single play."""

    play_id: Annotated[Optional[int], pydantic.Field(alias="playId")] = None
    club_code: Annotated[Optional[str], pydantic.Field(alias="clubCode")] = None
    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    stat_id: Annotated[Optional[int], pydantic.Field(alias="statId")] = None
    yards: Optional[int] = None
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None


class NgsPlayTypedDict(TypedDict):
    """Detailed play information from NGS endpoints."""

    game_id: NotRequired[int]
    play_id: NotRequired[int]
    sequence: NotRequired[int]
    game_key: NotRequired[int]
    play_type: NotRequired[str]
    play_type_code: NotRequired[int]
    play_description: NotRequired[str]
    play_state: NotRequired[str]
    quarter: NotRequired[int]
    down: NotRequired[int]
    yards_to_go: NotRequired[int]
    actual_yards_to_go: NotRequired[float]
    yardline: NotRequired[str]
    yardline_number: NotRequired[int]
    yardline_side: NotRequired[str]
    absolute_yardline_number: NotRequired[int]
    actual_yardline_for_first_down: NotRequired[float]
    game_clock: NotRequired[str]
    start_game_clock: NotRequired[str]
    end_game_clock: NotRequired[str]
    time_of_day_utc: NotRequired[datetime]
    home_score: NotRequired[int]
    visitor_score: NotRequired[int]
    pre_snap_home_score: NotRequired[int]
    pre_snap_visitor_score: NotRequired[int]
    possession_team_id: NotRequired[str]
    is_penalty: NotRequired[bool]
    is_big_play: NotRequired[bool]
    is_scoring: NotRequired[bool]
    is_st_play: NotRequired[bool]
    is_goal_to_go: NotRequired[bool]
    is_end_quarter: NotRequired[bool]
    is_change_of_possession: NotRequired[bool]
    play_direction: NotRequired[str]
    play_stats: NotRequired[List[NgsPlayStatTypedDict]]


class NgsPlay(BaseModel):
    """Detailed play information from NGS endpoints."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    play_id: Annotated[Optional[int], pydantic.Field(alias="playId")] = None
    sequence: Optional[int] = None
    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    play_type: Annotated[Optional[str], pydantic.Field(alias="playType")] = None
    play_type_code: Annotated[Optional[int], pydantic.Field(alias="playTypeCode")] = (
        None
    )
    play_description: Annotated[
        Optional[str], pydantic.Field(alias="playDescription")
    ] = None
    play_state: Annotated[Optional[str], pydantic.Field(alias="playState")] = None
    quarter: Optional[int] = None
    down: Optional[int] = None
    yards_to_go: Annotated[Optional[int], pydantic.Field(alias="yardsToGo")] = None
    actual_yards_to_go: Annotated[
        Optional[float], pydantic.Field(alias="actualYardsToGo")
    ] = None
    yardline: Optional[str] = None
    yardline_number: Annotated[
        Optional[int], pydantic.Field(alias="yardlineNumber")
    ] = None
    yardline_side: Annotated[Optional[str], pydantic.Field(alias="yardlineSide")] = None
    absolute_yardline_number: Annotated[
        Optional[int], pydantic.Field(alias="absoluteYardlineNumber")
    ] = None
    actual_yardline_for_first_down: Annotated[
        Optional[float], pydantic.Field(alias="actualYardlineForFirstDown")
    ] = None
    game_clock: Annotated[Optional[str], pydantic.Field(alias="gameClock")] = None
    start_game_clock: Annotated[
        Optional[str], pydantic.Field(alias="startGameClock")
    ] = None
    end_game_clock: Annotated[Optional[str], pydantic.Field(alias="endGameClock")] = (
        None
    )
    time_of_day_utc: Annotated[
        Optional[datetime], pydantic.Field(alias="timeOfDayUTC")
    ] = None
    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None
    visitor_score: Annotated[Optional[int], pydantic.Field(alias="visitorScore")] = None
    pre_snap_home_score: Annotated[
        Optional[int], pydantic.Field(alias="preSnapHomeScore")
    ] = None
    pre_snap_visitor_score: Annotated[
        Optional[int], pydantic.Field(alias="preSnapVisitorScore")
    ] = None
    possession_team_id: Annotated[
        Optional[str], pydantic.Field(alias="possessionTeamId")
    ] = None
    is_penalty: Annotated[Optional[bool], pydantic.Field(alias="isPenalty")] = None
    is_big_play: Annotated[Optional[bool], pydantic.Field(alias="isBigPlay")] = None
    is_scoring: Annotated[Optional[bool], pydantic.Field(alias="isScoring")] = None
    is_st_play: Annotated[Optional[bool], pydantic.Field(alias="isSTPlay")] = None
    is_goal_to_go: Annotated[Optional[bool], pydantic.Field(alias="isGoalToGo")] = None
    is_end_quarter: Annotated[Optional[bool], pydantic.Field(alias="isEndQuarter")] = (
        None
    )
    is_change_of_possession: Annotated[
        Optional[bool], pydantic.Field(alias="isChangeOfPossession")
    ] = None
    play_direction: Annotated[Optional[str], pydantic.Field(alias="playDirection")] = (
        None
    )
    play_stats: Annotated[
        Optional[List[NgsPlayStat]], pydantic.Field(alias="playStats")
    ] = None
