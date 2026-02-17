from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class PointsRecordPointsTypedDict(TypedDict):
    against: NotRequired[int]
    for_: NotRequired[int]


class PointsRecordPoints(BaseModel):
    against: Optional[int] = None

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None


class PointsRecordTypedDict(TypedDict):
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins: NotRequired[int]
    points: NotRequired[PointsRecordPointsTypedDict]
    win_pct: NotRequired[float]


class PointsRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[PointsRecordPoints] = None

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None
