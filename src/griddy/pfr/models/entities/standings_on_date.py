"""Models for the PFR 'Standings on Any Date' page.

Represents NFL standings as of a specific date or week, grouped by
conference and division.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel


class StandingsTeamEntry(PFRBaseModel):
    """A single team's standing on the queried date."""

    conference: Optional[str] = None
    division: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    playoff_marker: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    win_loss_perc: Optional[float] = None
    points_for: Optional[int] = None
    points_against: Optional[int] = None
    points_diff: Optional[int] = None
    margin_of_victory: Optional[float] = None


class StandingsOnDate(PFRBaseModel):
    """Parsed result of the PFR standings-on-date page."""

    title: str
    teams: List[StandingsTeamEntry]
