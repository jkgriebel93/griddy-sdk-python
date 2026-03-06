"""Pydantic models for PFR Statistical Milestones pages.

Covers ``/friv/{stat}-milestones.htm`` pages on Pro Football Reference,
listing upcoming statistical milestones and career leaders for a stat.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class MilestoneEntry(PFRBaseModel):
    """A player approaching a statistical milestone with current value and amount needed."""

    milestone: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class CareerLeader(PFRBaseModel):
    """An all-time career leader for a particular statistic."""

    rank: Optional[int] = None
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    is_active: bool = False


class StatisticalMilestones(PFRBaseModel):
    """Top-level result for a PFR statistical milestones page."""

    title: str
    stat: str
    milestones: List[MilestoneEntry]
    career_leaders: List[CareerLeader]
