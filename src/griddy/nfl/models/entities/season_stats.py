from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import BaseModel
from .defensive_stats import DefensiveStats
from .kicking_stats import KickingStats
from .passing_stats import PassingStats
from .receiving_stats import ReceivingStats
from .rushing_stats import RushingStats


class SeasonStats(BaseModel):
    defensive: Optional[DefensiveStats] = None

    games: Optional[int] = None

    kicking: Optional[KickingStats] = None

    passing: Optional[PassingStats] = None

    receiving: Optional[ReceivingStats] = None

    rushing: Optional[RushingStats] = None

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    starts: Optional[int] = None
