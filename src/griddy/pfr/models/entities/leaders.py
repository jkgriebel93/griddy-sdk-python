"""Pydantic models for PFR career/single-season/single-game leader pages.

Covers ``/leaders/{stat}_{scope}.htm`` pages on Pro Football Reference,
e.g. ``/leaders/pass_yds_career.htm`` or ``/leaders/rush_td_single_season.htm``.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from ...types import BaseModel

# --- Individual leader entry (one row in the leaders table) ---


class LeaderEntry(BaseModel):
    rank: Optional[int] = None
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    is_active: Optional[bool] = None
    is_hof: Optional[bool] = None
    stat_value: Optional[str] = None
    year: Optional[str] = None
    year_href: Optional[str] = None
    years: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None


# --- Top-level leaderboard page ---


class Leaderboard(BaseModel):
    stat: Optional[str] = None
    scope: Optional[str] = None
    title: Optional[str] = None
    entries: List[LeaderEntry] = []
