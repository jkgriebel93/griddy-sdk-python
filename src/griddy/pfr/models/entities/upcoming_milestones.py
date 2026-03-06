"""Pydantic models for PFR Upcoming Milestones pages.

Covers ``/friv/milestones.htm`` pages on Pro Football Reference, listing
players close to reaching statistical milestones and current career leaders.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class UpcomingMilestoneEntry(PFRBaseModel):
    """A player approaching an upcoming statistical milestone."""

    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None


class UpcomingLeaderboardEntry(PFRBaseModel):
    """A career leader entry with a link to the full leaderboard."""

    category: str
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    value: Optional[int] = None
    needed: Optional[str] = None
    leader_href: Optional[str] = None


class UpcomingMilestones(PFRBaseModel):
    """Top-level result for a PFR upcoming milestones page."""

    title: str
    description: str
    milestones: List[UpcomingMilestoneEntry]
    leaderboards: List[UpcomingLeaderboardEntry]
