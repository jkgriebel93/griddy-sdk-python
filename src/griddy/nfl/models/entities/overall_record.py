from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class OverallRecordPoints(BaseModel):
    against: Optional[int] = None

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None


OverallRecordType = Literal[
    "W",
    "L",
    "T",
    "STREAK_TYPE_WINNING",
    "STREAK_TYPE_LOSING",
    "STREAK_TYPE_TYING",
]
r"""Type of current streak"""


class Streak(BaseModel):
    length: Optional[int] = None
    r"""Length of current streak"""

    type: Optional[OverallRecordType] = None
    r"""Type of current streak"""


class OverallRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[OverallRecordPoints] = None

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None

    games: Optional[int] = None
    r"""Total games played"""

    streak: Optional[Streak] = None
