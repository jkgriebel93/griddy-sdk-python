"""Models for the PFR 'Last Undefeated Team' page.

Represents the last undefeated team(s) in every season, along with their
season outcomes.  Sourced from ``/friv/last-undefeated.htm``.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class LastUndefeatedEntry(BaseModel):
    """A single last-undefeated-team row."""

    year: Optional[int] = None
    year_href: Optional[str] = None
    league_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    record: Optional[str] = None
    first_loss: Optional[str] = None
    first_loss_href: Optional[str] = None
    final_record: Optional[str] = None
    playoff_result: Optional[str] = None
    playoff_result_href: Optional[str] = None


class LastUndefeated(BaseModel):
    """Parsed result of the PFR last-undefeated-team page."""

    title: str
    entries: List[LastUndefeatedEntry]
