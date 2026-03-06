"""Pydantic models for PFR season overview and stat category pages.

Covers the ``/years/{year}/`` main page (standings, team stats) and
``/years/{year}/{category}.htm`` stat category pages on Pro Football Reference.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..base import PFRBaseModel

# --- Conference Standing (AFC / NFC standings tables) ---


class ConferenceStanding(PFRBaseModel):
    """A single team row from the AFC or NFC standings table."""

    division: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    win_loss_perc: Optional[str] = None
    points: Optional[int] = None
    points_opp: Optional[int] = None
    points_diff: Optional[int] = None
    mov: Optional[str] = None
    sos_total: Optional[str] = None
    srs_total: Optional[str] = None
    srs_offense: Optional[str] = None
    srs_defense: Optional[str] = None


# --- Playoff Game (playoff_results table) ---


class PlayoffGame(PFRBaseModel):
    """A single playoff game from the playoff_results table."""

    week_num: Optional[str] = None
    game_day_of_week: Optional[str] = None
    game_date: Optional[str] = None
    winner: Optional[str] = None
    winner_href: Optional[str] = None
    game_location: Optional[str] = None
    loser: Optional[str] = None
    loser_href: Optional[str] = None
    boxscore_word: Optional[str] = None
    boxscore_href: Optional[str] = None
    pts_win: Optional[int] = None
    pts_lose: Optional[int] = None


# --- Playoff Standing (afc/nfc_playoff_standings tables) ---


class PlayoffStanding(PFRBaseModel):
    """A team's playoff qualification entry with seed reasoning."""

    team: Optional[str] = None
    team_href: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    why: Optional[str] = None
    reason: Optional[str] = None


# --- Season Overview (top-level for /years/{year}/) ---


class SeasonOverview(PFRBaseModel):
    """Top-level model for a PFR season overview page."""

    afc_standings: List[ConferenceStanding] = []
    nfc_standings: List[ConferenceStanding] = []
    playoff_results: List[PlayoffGame] = []
    afc_playoff_standings: List[PlayoffStanding] = []
    nfc_playoff_standings: List[PlayoffStanding] = []
    team_stats: List[Dict[str, Any]] = []
    passing: List[Dict[str, Any]] = []
    rushing: List[Dict[str, Any]] = []
    returns: List[Dict[str, Any]] = []
    kicking: List[Dict[str, Any]] = []
    punting: List[Dict[str, Any]] = []
    team_scoring: List[Dict[str, Any]] = []
    team_conversions: List[Dict[str, Any]] = []
    drives: List[Dict[str, Any]] = []


# --- Season Stats (top-level for /years/{year}/{category}.htm) ---


class SeasonStats(PFRBaseModel):
    """Top-level result for a PFR season stat category page."""

    regular_season: List[Dict[str, Any]] = []
    postseason: List[Dict[str, Any]] = []


# --- Week Game (individual game from /years/{year}/week_{number}.htm) ---


class WeekGame(PFRBaseModel):
    """A single game from a weekly schedule page."""

    game_date: Optional[str] = None
    away_team: Optional[str] = None
    away_team_href: Optional[str] = None
    away_score: Optional[int] = None
    home_team: Optional[str] = None
    home_team_href: Optional[str] = None
    home_score: Optional[int] = None
    winner: Optional[str] = None
    boxscore_href: Optional[str] = None
    top_passer: Optional[str] = None
    top_passer_href: Optional[str] = None
    top_passer_yds: Optional[str] = None
    top_rusher: Optional[str] = None
    top_rusher_href: Optional[str] = None
    top_rusher_yds: Optional[str] = None
    top_receiver: Optional[str] = None
    top_receiver_href: Optional[str] = None
    top_receiver_yds: Optional[str] = None


# --- Week Summary (top-level for /years/{year}/week_{number}.htm) ---


class WeekSummary(PFRBaseModel):
    """Top-level result for a PFR weekly schedule page."""

    games: List[WeekGame] = []
    players_of_the_week: List[Dict[str, Any]] = []
    top_passers: List[Dict[str, Any]] = []
    top_receivers: List[Dict[str, Any]] = []
    top_rushers: List[Dict[str, Any]] = []
    top_defenders: List[Dict[str, Any]] = []
