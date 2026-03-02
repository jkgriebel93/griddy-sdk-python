"""Models for the PFR 'Standings on Any Date' page.

Represents NFL standings as of a specific date or week, grouped by
conference and division.
"""

from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class StandingsTeamEntryTypedDict(TypedDict):
    """TypedDict for a single team's standing."""

    conference: NotRequired[Optional[str]]
    division: NotRequired[Optional[str]]
    team: NotRequired[Optional[str]]
    team_href: NotRequired[Optional[str]]
    playoff_marker: NotRequired[Optional[str]]
    wins: NotRequired[Optional[int]]
    losses: NotRequired[Optional[int]]
    ties: NotRequired[Optional[int]]
    win_loss_perc: NotRequired[Optional[float]]
    points_for: NotRequired[Optional[int]]
    points_against: NotRequired[Optional[int]]
    points_diff: NotRequired[Optional[int]]
    margin_of_victory: NotRequired[Optional[float]]


class StandingsTeamEntry(BaseModel):
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


class StandingsOnDateTypedDict(TypedDict):
    """TypedDict for the full standings-on-date page."""

    title: str
    teams: List[StandingsTeamEntryTypedDict]


class StandingsOnDate(BaseModel):
    """Parsed result of the PFR standings-on-date page."""

    title: str
    teams: List[StandingsTeamEntry]
