from __future__ import annotations

from typing import Literal, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .player import Player, PlayerTypedDict

Role = Literal[
    "PASSER",
    "RUSHER",
    "RECEIVER",
    "TACKLER",
    "KICKER",
    "RETURNER",
    "BLOCKER",
]


class PlayParticipantStatsTypedDict(TypedDict):
    r"""Play-specific statistics"""


class PlayParticipantStats(BaseModel):
    r"""Play-specific statistics"""


class PlayParticipantTypedDict(TypedDict):
    player: NotRequired[PlayerTypedDict]
    role: NotRequired[Role]
    stats: NotRequired[PlayParticipantStatsTypedDict]
    r"""Play-specific statistics"""


class PlayParticipant(BaseModel):
    player: Optional[Player] = None

    role: Optional[Role] = None

    stats: Optional[PlayParticipantStats] = None
    r"""Play-specific statistics"""
