from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class StandingsRecordPoints(BaseModel):
    against: Optional[int] = None
    r"""Points allowed"""

    for_: Annotated[Optional[int], pydantic.Field(alias="for")] = None
    r"""Points scored"""


class StandingsRecord(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None

    points: Optional[StandingsRecordPoints] = None

    rank: Optional[int] = None
    r"""Ranking within group"""

    win_pct: Annotated[Optional[float], pydantic.Field(alias="winPct")] = None
    r"""Win percentage"""
