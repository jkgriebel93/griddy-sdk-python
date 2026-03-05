from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


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
