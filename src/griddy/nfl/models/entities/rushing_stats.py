from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class RushingStatsTypedDict(TypedDict):
    carries: NotRequired[int]
    fumbles: NotRequired[int]
    long_rush: NotRequired[int]
    touchdowns: NotRequired[int]
    yards: NotRequired[int]
    yards_per_carry: NotRequired[float]


class RushingStats(BaseModel):
    carries: Optional[int] = None

    fumbles: Optional[int] = None

    long_rush: Annotated[Optional[int], pydantic.Field(alias="longRush")] = None

    touchdowns: Optional[int] = None

    yards: Optional[int] = None

    yards_per_carry: Annotated[
        Optional[float], pydantic.Field(alias="yardsPerCarry")
    ] = None
