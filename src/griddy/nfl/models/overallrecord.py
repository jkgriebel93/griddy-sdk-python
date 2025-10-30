
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OverallRecordPointsTypedDict(TypedDict):
    against: NotRequired[int]
    for_: NotRequired[int]


class OverallRecordPoints(BaseModel):
    against: Optional[int] = None

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None


OverallRecordType = Literal[
    "W",
    "L",
    "T",
    "STREAK_TYPE_WINNING",
    "STREAK_TYPE_LOSING",
]
r"""Type of current streak"""


class StreakTypedDict(TypedDict):
    length: NotRequired[int]
    r"""Length of current streak"""
    type: NotRequired[OverallRecordType]
    r"""Type of current streak"""


class Streak(BaseModel):
    length: Optional[int] = None
    r"""Length of current streak"""

    type: Optional[OverallRecordType] = None
    r"""Type of current streak"""


class OverallRecordTypedDict(TypedDict):
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins: NotRequired[int]
    points: NotRequired[OverallRecordPointsTypedDict]
    win_pct: NotRequired[float]
    games: NotRequired[int]
    r"""Total games played"""
    streak: NotRequired[StreakTypedDict]


class OverallRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[OverallRecordPoints] = None

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None

    games: Optional[int] = None
    r"""Total games played"""

    streak: Optional[Streak] = None
