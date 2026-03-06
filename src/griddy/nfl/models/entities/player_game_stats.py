from __future__ import annotations

from typing import Optional

from ...types import BaseModel
from .defensive_stats import DefensiveStats
from .kicking_stats import KickingStats
from .passing_stats import PassingStats
from .player import Player
from .receiving_stats import ReceivingStats
from .rushing_stats import RushingStats


class PlayerGameStats(BaseModel):
    """Player statistics for a single game."""

    defensive: Optional[DefensiveStats] = None

    kicking: Optional[KickingStats] = None

    passing: Optional[PassingStats] = None

    player: Optional[Player] = None

    receiving: Optional[ReceivingStats] = None

    rushing: Optional[RushingStats] = None
