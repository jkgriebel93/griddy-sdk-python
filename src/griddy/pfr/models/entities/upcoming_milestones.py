from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class UpcomingMilestoneEntryTypedDict(TypedDict):
    category: str
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    value: NotRequired[Optional[int]]
    needed: NotRequired[Optional[str]]


class UpcomingMilestoneEntry(BaseModel):
    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class UpcomingLeaderboardEntryTypedDict(TypedDict):
    category: str
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    value: NotRequired[Optional[int]]
    needed: NotRequired[Optional[str]]
    leader_href: NotRequired[Optional[str]]


class UpcomingLeaderboardEntry(BaseModel):
    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    leader_href: Optional[str] = None


class UpcomingMilestonesTypedDict(TypedDict):
    title: str
    description: str
    milestones: List[UpcomingMilestoneEntryTypedDict]
    leaderboards: List[UpcomingLeaderboardEntryTypedDict]


class UpcomingMilestones(BaseModel):
    title: str
    description: str
    milestones: List[UpcomingMilestoneEntry]
    leaderboards: List[UpcomingLeaderboardEntry]
