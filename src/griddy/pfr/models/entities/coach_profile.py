"""Pydantic models for PFR coach profile pages.

Covers the ``/coaches/{CoachId}.htm`` pages on Pro Football Reference,
including coaching results, coaching ranks, coaching history, coaching
tree (worked-for / employed), and challenge results.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# --- Coach Bio (from #meta div) ---


class CoachBio(PFRBaseModel):
    """Biographical info from the coach profile meta panel."""

    name: str
    full_name: Optional[str] = None
    nicknames: List[str] = []
    photo_url: Optional[str] = None
    birth_date: Optional[str] = None
    birth_city: Optional[str] = None
    birth_state: Optional[str] = None
    college: Optional[str] = None
    college_href: Optional[str] = None
    college_coaching_href: Optional[str] = None
    high_schools: List[str] = []
    as_exec: Optional[str] = None
    as_exec_href: Optional[str] = None
    relatives: Optional[str] = None
    relatives_href: Optional[str] = None


# --- Coaching Result (from coaching_results table body) ---


class CoachingResult(PFRBaseModel):
    """A single season row from the coaching_results table."""

    year_id: str
    year_href: Optional[str] = None
    age: Optional[int] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    league_id: Optional[str] = None
    g: Optional[int] = None
    g_href: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    win_loss_perc: Optional[str] = None
    srs_total: Optional[float] = None
    srs_offense: Optional[float] = None
    srs_defense: Optional[float] = None
    g_playoffs: Optional[int] = None
    wins_playoffs: Optional[int] = None
    losses_playoffs: Optional[int] = None
    win_loss_playoffs_perc: Optional[str] = None
    rank_team: Optional[int] = None
    chall_num: Optional[int] = None
    chall_won: Optional[int] = None
    coach_remarks: Optional[str] = None


# --- Coaching Result Total (from coaching_results table footer) ---


class CoachingResultTotal(PFRBaseModel):
    """A summary total row from the coaching_results table footer."""

    label: str
    team: Optional[str] = None
    g: Optional[int] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    win_loss_perc: Optional[str] = None
    g_playoffs: Optional[int] = None
    wins_playoffs: Optional[int] = None
    losses_playoffs: Optional[int] = None
    win_loss_playoffs_perc: Optional[str] = None
    rank_avg: Optional[float] = None
    chall_num: Optional[int] = None
    chall_won: Optional[int] = None


# --- Coaching Rank (from coaching_ranks table) ---


class CoachingRank(PFRBaseModel):
    """A single season row from the coaching_ranks table."""

    year_id: str
    team: Optional[str] = None
    coordinator_type: Optional[str] = None
    teams_in_league: Optional[int] = None
    rank_win_percentage: Optional[int] = None
    rank_takeaway_giveaway: Optional[int] = None
    rank_points_diff: Optional[int] = None
    rank_yds_diff: Optional[int] = None
    rank_off_yds: Optional[int] = None
    rank_off_pts: Optional[int] = None
    rank_off_turnovers: Optional[int] = None
    rank_off_rush_att: Optional[int] = None
    rank_off_rush_yds: Optional[int] = None
    rank_off_rush_td: Optional[int] = None
    rank_off_rush_yds_per_att: Optional[int] = None
    rank_off_fumbles_lost: Optional[int] = None
    rank_off_pass_att: Optional[int] = None
    rank_off_pass_yds: Optional[int] = None
    rank_off_pass_td: Optional[int] = None
    rank_off_pass_int: Optional[int] = None
    rank_off_pass_net_yds_per_att: Optional[int] = None
    rank_def_yds: Optional[int] = None
    rank_def_pts: Optional[int] = None
    rank_def_turnovers: Optional[int] = None
    rank_def_rush_att: Optional[int] = None
    rank_def_rush_yds: Optional[int] = None
    rank_def_rush_td: Optional[int] = None
    rank_def_rush_yds_per_att: Optional[int] = None
    rank_def_fumbles_rec: Optional[int] = None
    rank_def_pass_att: Optional[int] = None
    rank_def_pass_yds: Optional[int] = None
    rank_def_pass_td: Optional[int] = None
    rank_def_pass_int: Optional[int] = None
    rank_def_pass_net_yds_per_att: Optional[int] = None


# --- Coaching History Entry (from coaching_history table) ---


class CoachingHistoryEntry(PFRBaseModel):
    """A single row from the coaching_history table."""

    year_id: str
    coach_age: Optional[int] = None
    coach_level: Optional[str] = None
    coach_employer: Optional[str] = None
    coach_employer_href: Optional[str] = None
    coach_role: Optional[str] = None


# --- Coaching Tree Entry (for worked_for and employed tables) ---


class CoachingTreeEntry(PFRBaseModel):
    """A coaching tree entry (worked-for or employed relationship)."""

    coach_name: str
    coach_href: Optional[str] = None
    roles: Optional[str] = None


# --- Challenge Result (from challenge_results table) ---


class ChallengeResult(PFRBaseModel):
    """A single challenge result from the challenge_results table."""

    game_date: Optional[str] = None
    game_date_href: Optional[str] = None
    down: Optional[int] = None
    yds_to_go: Optional[int] = None
    location: Optional[str] = None
    challenge_ruling: Optional[str] = None
    detail: Optional[str] = None


# --- Coach Profile (top-level model) ---


class CoachProfile(PFRBaseModel):
    """Top-level model for a PFR coach profile page."""

    bio: CoachBio
    coaching_results: List[CoachingResult]
    coaching_results_totals: List[CoachingResultTotal]
    coaching_ranks: List[CoachingRank]
    coaching_history: List[CoachingHistoryEntry]
    challenge_results: List[ChallengeResult]
    worked_for: List[CoachingTreeEntry]
    employed: List[CoachingTreeEntry]
