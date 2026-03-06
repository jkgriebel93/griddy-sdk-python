"""Pydantic models for a PFR game boxscore page.

Covers ``/boxscores/{game_id}.htm`` pages on Pro Football Reference,
including scorebox, linescore, scoring plays, expected points, player
stats (offense, defense, returns, kicking), starters, snap counts,
and drive summaries.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field

from ..base import PFRBaseModel

# --- Scorebox ---


class ScoreboxTeam(PFRBaseModel):
    """Team info within the scorebox header (name, score, record, coach)."""

    name: str
    href: str
    score: int
    record: str
    coach: str
    coach_href: str


class ScoreboxMeta(PFRBaseModel):
    """Game metadata from the scorebox (date, stadium, attendance, duration)."""

    date: Optional[str] = None
    start_time: Optional[str] = Field(default=None, alias="Start Time")
    stadium: Optional[str] = Field(default=None, alias="Stadium")
    attendance: Optional[str] = Field(default=None, alias="Attendance")
    time_of_game: Optional[str] = Field(default=None, alias="Time of Game")


class Scorebox(PFRBaseModel):
    """Combined scorebox with away team, home team, and game metadata."""

    away: ScoreboxTeam
    home: ScoreboxTeam
    meta: ScoreboxMeta


# --- Linescore ---


class LinescoreEntry(PFRBaseModel):
    """A single team's quarter-by-quarter scoring line."""

    team: str
    team_href: str
    quarters: Dict[str, int]


# --- Scoring ---


class ScoringPlay(PFRBaseModel):
    """A single scoring play with quarter, time, and description."""

    quarter: Optional[int] = None
    time: str
    team: str
    description: str
    description_href: str
    vis_team_score: int
    home_team_score: int


# --- Expected Points ---


class ExpectedPoints(PFRBaseModel):
    """Expected points added breakdown for a team in a game."""

    team_name: str
    pbp_exp_points_tot: float
    pbp_exp_points_off_tot: float
    pbp_exp_points_off_pass: float
    pbp_exp_points_off_rush: float
    pbp_exp_points_off_to: float
    pbp_exp_points_def_tot: float
    pbp_exp_points_def_pass: float
    pbp_exp_points_def_rush: float
    pbp_exp_points_def_to: float
    pbp_exp_points_st: float
    pbp_exp_points_k: float
    pbp_exp_points_kr: float
    pbp_exp_points_p: float
    pbp_exp_points_pr: float
    pbp_exp_points_fgxp: float


# --- Player Offense ---


class PlayerOffense(PFRBaseModel):
    """Individual player offensive stats from a game boxscore."""

    player: str
    player_href: str
    player_id: str
    team: str
    pass_cmp: int
    pass_att: int
    pass_yds: int
    pass_td: int
    pass_int: int
    pass_sacked: int
    pass_sacked_yds: int
    pass_long: Optional[int] = None
    pass_rating: Optional[float] = None
    rush_att: int
    rush_yds: int
    rush_td: int
    rush_long: Optional[int] = None
    targets: int
    rec: int
    rec_yds: int
    rec_td: int
    rec_long: Optional[int] = None
    fumbles: int
    fumbles_lost: int


# --- Player Defense ---


class PlayerDefense(PFRBaseModel):
    """Individual player defensive stats from a game boxscore."""

    player: str
    player_href: str
    player_id: str
    team: str
    def_int: int
    def_int_yds: int
    def_int_td: int
    def_int_long: int
    pass_defended: int
    sacks: float
    tackles_combined: int
    tackles_solo: int
    tackles_assists: int
    tackles_loss: int
    qb_hits: int
    fumbles_rec: int
    fumbles_rec_yds: int
    fumbles_rec_td: int
    fumbles_forced: int


# --- Returns ---


class PlayerReturn(PFRBaseModel):
    """Individual player kick and punt return stats from a game boxscore."""

    player: str
    player_href: str
    player_id: str
    team: str
    kick_ret: int
    kick_ret_yds: int
    kick_ret_yds_per_ret: Optional[float] = None
    kick_ret_td: int
    kick_ret_long: int
    punt_ret: int
    punt_ret_yds: int
    punt_ret_yds_per_ret: Optional[float] = None
    punt_ret_td: int
    punt_ret_long: int


# --- Kicking ---


class PlayerKicking(PFRBaseModel):
    """Individual player kicking and punting stats from a game boxscore."""

    player: str
    player_href: str
    player_id: str
    team: str
    xpm: Optional[int] = None
    xpa: Optional[int] = None
    fgm: Optional[int] = None
    fga: Optional[int] = None
    punt: int
    punt_yds: int
    punt_yds_per_punt: Optional[float] = None
    punt_long: Optional[int] = None


# --- Starters ---


class Starter(PFRBaseModel):
    """A starting player entry with position."""

    player: str
    player_href: str
    player_id: str
    pos: str


# --- Snap Counts ---


class SnapCount(PFRBaseModel):
    """Snap count totals and percentages for a player by phase of play."""

    player: str
    player_href: str
    player_id: str
    pos: str
    offense: int
    off_pct: str
    defense: int
    def_pct: str
    special_teams: int
    st_pct: str


# --- Drives ---


class Drive(PFRBaseModel):
    """A single drive summary with start time, plays, yards, and result."""

    drive_num: int
    quarter: int
    time_start: str
    start_at: Optional[str] = None
    play_count_tip: int
    time_total: str
    net_yds: int
    end_event: str


# --- Top-level Game Details ---


class GameDetails(PFRBaseModel):
    """Top-level model for a full PFR game boxscore page."""

    scorebox: Scorebox
    linescore: List[LinescoreEntry]
    scoring: List[ScoringPlay]
    game_info: Dict[str, str]
    officials: Dict[str, str]
    expected_points: List[ExpectedPoints]
    team_stats: Dict[str, Dict[str, str]]
    player_offense: List[PlayerOffense]
    player_defense: List[PlayerDefense]
    returns: List[PlayerReturn]
    kicking: List[PlayerKicking]
    home_starters: List[Starter]
    vis_starters: List[Starter]
    home_snap_counts: List[SnapCount]
    vis_snap_counts: List[SnapCount]
    home_drives: List[Drive]
    vis_drives: List[Drive]
