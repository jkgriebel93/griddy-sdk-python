"""Pydantic models for PFR Super Bowl pages.

Covers three page types:
- ``/super-bowl/`` — Super Bowl history (table ``#super_bowls``)
- ``/super-bowl/leaders.htm`` — Super Bowl leaders (leaderboard tables)
- ``/super-bowl/standings.htm`` — franchise standings (table ``#standings``)
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# ---------------------------------------------------------------------------
# Super Bowl Game (one row in /super-bowl/)
# ---------------------------------------------------------------------------


class SuperBowlGame(PFRBaseModel):
    game_date: Optional[str] = None
    superbowl: Optional[str] = None
    superbowl_number: Optional[int] = None
    boxscore_href: Optional[str] = None
    winner: Optional[str] = None
    winner_href: Optional[str] = None
    winner_points: Optional[int] = None
    loser: Optional[str] = None
    loser_href: Optional[str] = None
    loser_points: Optional[int] = None
    mvp: Optional[str] = None
    mvp_href: Optional[str] = None
    stadium: Optional[str] = None
    stadium_href: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None


# ---------------------------------------------------------------------------
# Super Bowl History (top-level for /super-bowl/)
# ---------------------------------------------------------------------------


class SuperBowlHistory(PFRBaseModel):
    games: List[SuperBowlGame] = []


# ---------------------------------------------------------------------------
# Super Bowl Leader Entry (one row in a leader table)
# ---------------------------------------------------------------------------


class SuperBowlLeaderEntry(PFRBaseModel):
    rank: Optional[int] = None
    player: Optional[str] = None
    player_href: Optional[str] = None
    description: Optional[str] = None
    value: Optional[str] = None


# ---------------------------------------------------------------------------
# Super Bowl Leader Table (one leaderboard table)
# ---------------------------------------------------------------------------


class SuperBowlLeaderTable(PFRBaseModel):
    category: Optional[str] = None
    entries: List[SuperBowlLeaderEntry] = []


# ---------------------------------------------------------------------------
# Super Bowl Leaders (top-level for /super-bowl/leaders.htm)
# ---------------------------------------------------------------------------


class SuperBowlLeaders(PFRBaseModel):
    tables: List[SuperBowlLeaderTable] = []


# ---------------------------------------------------------------------------
# Super Bowl QB (one QB in standings sb_qbs column)
# ---------------------------------------------------------------------------


class SuperBowlQB(PFRBaseModel):
    player: Optional[str] = None
    player_href: Optional[str] = None
    record: Optional[str] = None


# ---------------------------------------------------------------------------
# Super Bowl Standing (one row in /super-bowl/standings.htm)
# ---------------------------------------------------------------------------


class SuperBowlStanding(PFRBaseModel):
    rank: Optional[int] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    games: Optional[int] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    win_loss_pct: Optional[str] = None
    points: Optional[int] = None
    points_opp: Optional[int] = None
    points_diff: Optional[str] = None
    qbs: List[SuperBowlQB] = []


# ---------------------------------------------------------------------------
# Super Bowl Standings (top-level for /super-bowl/standings.htm)
# ---------------------------------------------------------------------------


class SuperBowlStandings(PFRBaseModel):
    teams: List[SuperBowlStanding] = []
