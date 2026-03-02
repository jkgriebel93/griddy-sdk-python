"""Models for the PFR 'Last Undefeated Team' page.

Represents the last undefeated team(s) in every season, along with their
season outcomes.  Sourced from ``/friv/last-undefeated.htm``.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class LastUndefeatedEntryTypedDict(TypedDict):
    """TypedDict for a single last-undefeated-team row."""

    year: NotRequired[Optional[int]]
    year_href: NotRequired[Optional[str]]
    league_id: NotRequired[Optional[str]]
    team: NotRequired[Optional[str]]
    team_href: NotRequired[Optional[str]]
    record: NotRequired[Optional[str]]
    first_loss: NotRequired[Optional[str]]
    first_loss_href: NotRequired[Optional[str]]
    final_record: NotRequired[Optional[str]]
    playoff_result: NotRequired[Optional[str]]
    playoff_result_href: NotRequired[Optional[str]]


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


class LastUndefeatedTypedDict(TypedDict):
    """TypedDict for the full last-undefeated page."""

    title: str
    entries: List[LastUndefeatedEntryTypedDict]


class LastUndefeated(BaseModel):
    """Parsed result of the PFR last-undefeated-team page."""

    title: str
    entries: List[LastUndefeatedEntry]
