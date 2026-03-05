"""Models for the PFR 'Quarterback Wins vs. Each Franchise' page."""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class QBWinEntry(PFRBaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    teams_beat: int
    teams_not_beat: List[str]


class QBWins(PFRBaseModel):
    title: str
    entries: List[QBWinEntry]
