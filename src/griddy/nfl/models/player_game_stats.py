from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .defensive_stats import DefensiveStats, DefensiveStatsTypedDict
from .kicking_stats import KickingStats, KickingStatsTypedDict
from .passing_stats import PassingStats, PassingStatsTypedDict
from .player import Player, PlayerTypedDict
from .receiving_stats import ReceivingStats, ReceivingStatsTypedDict
from .rushing_stats import RushingStats, RushingStatsTypedDict


class PlayerGameStatsTypedDict(TypedDict):
    defensive: NotRequired[DefensiveStatsTypedDict]
    kicking: NotRequired[KickingStatsTypedDict]
    passing: NotRequired[PassingStatsTypedDict]
    player: NotRequired[PlayerTypedDict]
    receiving: NotRequired[ReceivingStatsTypedDict]
    rushing: NotRequired[RushingStatsTypedDict]


class PlayerGameStats(BaseModel):
    defensive: Optional[DefensiveStats] = None

    kicking: Optional[KickingStats] = None

    passing: Optional[PassingStats] = None

    player: Optional[Player] = None

    receiving: Optional[ReceivingStats] = None

    rushing: Optional[RushingStats] = None
