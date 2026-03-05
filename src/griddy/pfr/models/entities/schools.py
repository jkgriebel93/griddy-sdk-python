"""Pydantic models for PFR Schools & Colleges pages.

Covers two page types:
- ``/schools/`` — All Player Colleges (table ``#college_stats_table``)
- ``/schools/high_schools.cgi`` — High Schools (table ``#high_schools``)
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# ---------------------------------------------------------------------------
# College (one row in /schools/)
# ---------------------------------------------------------------------------


class College(PFRBaseModel):
    rank: Optional[int] = None
    college_name: Optional[str] = None
    college_href: Optional[str] = None
    state: Optional[str] = None
    players: Optional[int] = None
    players_active: Optional[int] = None
    hofers: Optional[int] = None
    pro_bowls: Optional[int] = None
    games: Optional[int] = None
    touchdowns: Optional[int] = None
    best_career_av_player: Optional[str] = None
    best_career_av_player_href: Optional[str] = None
    best_career_av: Optional[int] = None
    most_td_player: Optional[str] = None
    most_td_player_href: Optional[str] = None
    most_td: Optional[int] = None
    most_games_player: Optional[str] = None
    most_games_player_href: Optional[str] = None
    most_games: Optional[int] = None


# ---------------------------------------------------------------------------
# CollegeList (top-level for /schools/)
# ---------------------------------------------------------------------------


class CollegeList(PFRBaseModel):
    colleges: List[College] = []


# ---------------------------------------------------------------------------
# HighSchool (one row in /schools/high_schools.cgi)
# ---------------------------------------------------------------------------


class HighSchool(PFRBaseModel):
    name: Optional[str] = None
    name_href: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    num_players: Optional[int] = None
    num_active: Optional[int] = None


# ---------------------------------------------------------------------------
# HighSchoolList (top-level for /schools/high_schools.cgi)
# ---------------------------------------------------------------------------


class HighSchoolList(PFRBaseModel):
    schools: List[HighSchool] = []
