from __future__ import annotations

from typing import Literal, Optional

from ...types import BaseModel
from .player import Player

Role = Literal[
    "PASSER",
    "RUSHER",
    "RECEIVER",
    "TACKLER",
    "KICKER",
    "RETURNER",
    "BLOCKER",
]


class PlayParticipantStats(BaseModel):
    r"""Play-specific statistics"""


class PlayParticipant(BaseModel):
    player: Optional[Player] = None

    role: Optional[Role] = None

    stats: Optional[PlayParticipantStats] = None
    r"""Play-specific statistics"""
