"""Models for the PFR 'Quarterback Wins vs. Each Franchise' page."""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class QBWinEntryTypedDict(TypedDict):
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    teams_beat: int
    teams_not_beat: List[str]


class QBWinEntry(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    teams_beat: int
    teams_not_beat: List[str]


class QBWinsTypedDict(TypedDict):
    title: str
    entries: List[QBWinEntryTypedDict]


class QBWins(BaseModel):
    title: str
    entries: List[QBWinEntry]
