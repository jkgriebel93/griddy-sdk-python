"""Models for the PFR 'Overtime Ties' page.

Represents all tied games since sudden-death overtime was instituted in 1974.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class OvertimeTieEntry(PFRBaseModel):
    """A single overtime tie game."""

    year: int
    game_date: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    points: Optional[int] = None
    opp: Optional[str] = None
    opp_href: Optional[str] = None
    points_opp: Optional[int] = None
    boxscore_href: Optional[str] = None


class OvertimeTies(PFRBaseModel):
    """Parsed result of the PFR overtime ties page."""

    title: str
    entries: List[OvertimeTieEntry]
