
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PassingStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    completion_pct: NotRequired[float]
    completions: NotRequired[int]
    interceptions: NotRequired[int]
    rating: NotRequired[float]
    sack_yards: NotRequired[int]
    sacks: NotRequired[int]
    touchdowns: NotRequired[int]
    yards: NotRequired[int]


class PassingStats(BaseModel):
    attempts: Optional[int] = None

    completion_pct: Annotated[
        Optional[float], pydantic.Field(alias="completionPct")
    ] = None

    completions: Optional[int] = None

    interceptions: Optional[int] = None

    rating: Optional[float] = None

    sack_yards: Annotated[Optional[int], pydantic.Field(alias="sackYards")] = None

    sacks: Optional[int] = None

    touchdowns: Optional[int] = None

    yards: Optional[int] = None
