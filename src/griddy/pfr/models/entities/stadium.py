"""Pydantic models for PFR stadium pages.

Covers the ``/stadiums/{StadiumId}.htm`` pages on Pro Football Reference,
including stadium bio, career leaders, best games, and notable game summaries.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# --- Stadium Team (from #meta teams list) ---


class StadiumTeam(PFRBaseModel):
    name: str
    team_href: Optional[str] = None
    years: Optional[str] = None
    regular_season_record: Optional[str] = None
    regular_season_href: Optional[str] = None
    playoff_record: Optional[str] = None
    playoff_href: Optional[str] = None


# --- Stadium Bio (from #meta div) ---


class StadiumBio(PFRBaseModel):
    name: str
    address: Optional[str] = None
    years_active: Optional[str] = None
    total_games: Optional[int] = None
    surfaces: Optional[str] = None
    teams: List[StadiumTeam] = []


# --- Stadium Leader (from leaders table) ---


class StadiumLeader(PFRBaseModel):
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    g: Optional[int] = None
    stats: Optional[str] = None


# --- Stadium Best Game (from games and playoff_games tables) ---


class StadiumBestGame(PFRBaseModel):
    player: Optional[str] = None
    player_id: Optional[str] = None
    player_href: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    stats: Optional[str] = None
    boxscore_word: Optional[str] = None
    boxscore_href: Optional[str] = None


# --- Stadium Game Leader (stat leader in a game summary) ---


class StadiumGameLeader(PFRBaseModel):
    stat_name: Optional[str] = None
    player: Optional[str] = None
    player_href: Optional[str] = None
    value: Optional[str] = None


# --- Stadium Game Summary (notable game from game_summaries section) ---


class StadiumGameSummary(PFRBaseModel):
    label: Optional[str] = None
    date: Optional[str] = None
    team_1: Optional[str] = None
    team_1_href: Optional[str] = None
    team_1_score: Optional[int] = None
    team_2: Optional[str] = None
    team_2_href: Optional[str] = None
    team_2_score: Optional[int] = None
    boxscore_href: Optional[str] = None
    leaders: List[StadiumGameLeader] = []


# --- Stadium Profile (top-level model) ---


class StadiumProfile(PFRBaseModel):
    bio: StadiumBio
    leaders: List[StadiumLeader]
    best_games: List[StadiumBestGame]
    best_playoff_games: List[StadiumBestGame]
    game_summaries: List[StadiumGameSummary]
