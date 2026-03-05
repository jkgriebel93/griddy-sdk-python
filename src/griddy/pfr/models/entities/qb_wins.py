"""Models for the PFR 'Quarterback Wins vs. Each Franchise' page."""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class QBWinEntry(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    teams_beat: int
    teams_not_beat: List[str]


class QBWins(BaseModel):
    title: str
    entries: List[QBWinEntry]
