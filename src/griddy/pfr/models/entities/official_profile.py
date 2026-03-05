"""Pydantic models for PFR game official profile pages.

Covers the ``/officials/{OfficialId}.htm`` pages on Pro Football Reference,
including season penalty totals and individual game logs.
"""

from __future__ import annotations

from typing import List, Optional

from ...types import BaseModel

# --- Official Bio (from #meta div) ---


class OfficialBio(BaseModel):
    name: str
    position: Optional[str] = None


# --- Official Season Stat (from official_stats table body) ---


class OfficialSeasonStat(BaseModel):
    year: str
    g: Optional[int] = None
    g_playoffs: Optional[int] = None
    pos: Optional[str] = None
    home: Optional[int] = None
    visitor: Optional[int] = None
    home_pct: Optional[float] = None
    home_wpct: Optional[float] = None
    pen_total: Optional[int] = None
    pen_yds: Optional[int] = None
    pen_per_g: Optional[float] = None
    pen_yds_per_g: Optional[float] = None
    lg_home_pct: Optional[float] = None
    lg_home_wpct: Optional[float] = None
    lg_pen_per_g: Optional[float] = None
    lg_pen_yds_per_g: Optional[float] = None
    rel_home_pct: Optional[float] = None
    rel_home_wpct: Optional[float] = None
    rel_pen_per_g: Optional[float] = None
    rel_pen_yds_per_g: Optional[float] = None


# --- Official Game (from games table body) ---


class OfficialGame(BaseModel):
    game_date: Optional[str] = None
    game_date_href: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    opp: Optional[str] = None
    opp_href: Optional[str] = None
    pos: Optional[str] = None
    points_opp: Optional[int] = None
    penalties_opp: Optional[int] = None
    penalties_yds_opp: Optional[int] = None
    points: Optional[int] = None
    penalties: Optional[int] = None
    penalties_yds: Optional[int] = None


# --- Official Profile (top-level model) ---


class OfficialProfile(BaseModel):
    bio: OfficialBio
    official_stats: List[OfficialSeasonStat]
    games: List[OfficialGame]
