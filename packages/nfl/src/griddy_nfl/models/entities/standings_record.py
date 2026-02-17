from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class StandingsRecordPointsTypedDict(TypedDict):
    against: NotRequired[int]
    r"""Points allowed"""
    for_: NotRequired[int]
    r"""Points scored"""


class StandingsRecordPoints(BaseModel):
    against: Optional[int] = None
    r"""Points allowed"""

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None
    r"""Points scored"""


class StandingsRecordTypedDict(TypedDict):
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins: NotRequired[int]
    points: NotRequired[StandingsRecordPointsTypedDict]
    rank: NotRequired[int]
    r"""Ranking within group"""
    win_pct: NotRequired[float]
    r"""Win percentage"""


class StandingsRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[StandingsRecordPoints] = None

    rank: Optional[int] = None
    r"""Ranking within group"""

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None
    r"""Win percentage"""
