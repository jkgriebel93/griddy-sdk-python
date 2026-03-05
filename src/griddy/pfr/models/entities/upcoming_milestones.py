from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class UpcomingMilestoneEntry(PFRBaseModel):
    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class UpcomingLeaderboardEntry(PFRBaseModel):
    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    leader_href: Optional[str] = None


class UpcomingMilestones(PFRBaseModel):
    title: str
    description: str
    milestones: List[UpcomingMilestoneEntry]
    leaderboards: List[UpcomingLeaderboardEntry]
