from __future__ import annotations

from typing import Any, List, Optional

from ...types import BaseModel


class MilestoneEntry(BaseModel):
    milestone: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class CareerLeader(BaseModel):
    rank: Optional[int] = None
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    is_active: bool = False


class StatisticalMilestones(BaseModel):
    title: str
    stat: str
    milestones: List[MilestoneEntry]
    career_leaders: List[CareerLeader]
