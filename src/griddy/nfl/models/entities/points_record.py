from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class PointsRecordPoints(BaseModel):
    against: Optional[int] = None

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None


class PointsRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[PointsRecordPoints] = None

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None
