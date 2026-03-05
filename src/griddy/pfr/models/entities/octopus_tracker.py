"""Models for the PFR 'Octopus Tracker' page.

Represents game-level instances (since 1994) of a player scoring both
the touchdown and the two-point conversion on a single possession.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel


class OctopusEntry(BaseModel):
    """A single game instance of an octopus (TD + 2pt conversion)."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    week_num: Optional[int] = None
    game_day_of_week: Optional[str] = None
    game_date: Optional[str] = None
    boxscore_href: Optional[str] = None
    game_outcome: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    opp: Optional[str] = None
    opp_href: Optional[str] = None
    margin: Optional[int] = None
    score_type: Optional[str] = None
    xpa_type: Optional[str] = None


class OctopusTracker(BaseModel):
    """Parsed result of the PFR octopus tracker page."""

    title: str
    entries: List[OctopusEntry]
