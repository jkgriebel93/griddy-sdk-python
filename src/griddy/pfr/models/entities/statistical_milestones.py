from __future__ import annotations

from typing import Any, List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class MilestoneEntryTypedDict(TypedDict):
    milestone: str
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    value: NotRequired[Optional[int]]
    needed: NotRequired[Optional[str]]


class MilestoneEntry(BaseModel):
    milestone: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class CareerLeaderTypedDict(TypedDict):
    rank: NotRequired[Optional[int]]
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    value: NotRequired[Optional[int]]
    needed: NotRequired[Optional[str]]
    is_active: bool


class CareerLeader(BaseModel):
    rank: Optional[int] = None
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    is_active: bool = False


class StatisticalMilestonesTypedDict(TypedDict):
    title: str
    stat: str
    milestones: List[MilestoneEntryTypedDict]
    career_leaders: List[CareerLeaderTypedDict]


class StatisticalMilestones(BaseModel):
    title: str
    stat: str
    milestones: List[MilestoneEntry]
    career_leaders: List[CareerLeader]
