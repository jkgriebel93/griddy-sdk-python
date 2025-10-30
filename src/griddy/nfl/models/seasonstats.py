from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .defensivestats import DefensiveStats, DefensiveStatsTypedDict
from .kickingstats import KickingStats, KickingStatsTypedDict
from .passingstats import PassingStats, PassingStatsTypedDict
from .receivingstats import ReceivingStats, ReceivingStatsTypedDict
from .rushingstats import RushingStats, RushingStatsTypedDict
from .seasontypeenum import SeasonTypeEnum


class SeasonStatsTypedDict(TypedDict):
    defensive: NotRequired[DefensiveStatsTypedDict]
    games: NotRequired[int]
    kicking: NotRequired[KickingStatsTypedDict]
    passing: NotRequired[PassingStatsTypedDict]
    receiving: NotRequired[ReceivingStatsTypedDict]
    rushing: NotRequired[RushingStatsTypedDict]
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    starts: NotRequired[int]


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
