"""Pydantic models for a PFR team franchise page.

Covers ``/teams/{team}/`` pages on Pro Football Reference, including
franchise metadata, all-time leaders, and year-by-year season records.
"""

from __future__ import annotations

from typing import List, Optional

from ..base import PFRBaseModel

# --- Franchise Metadata ---


class FranchiseLeader(PFRBaseModel):
    """An all-time franchise leader in a stat category."""

    name: Optional[str] = None
    href: Optional[str] = None
    stats: Optional[str] = None


class FranchiseMeta(PFRBaseModel):
    """Franchise-level metadata including records and all-time leaders."""

    team_names: Optional[str] = None
    seasons: Optional[str] = None
    record: Optional[str] = None
    playoff_record: Optional[str] = None
    super_bowls_won: Optional[str] = None
    championships_won: Optional[str] = None
    all_time_passing_leader: Optional[FranchiseLeader] = None
    all_time_rushing_leader: Optional[FranchiseLeader] = None
    all_time_receiving_leader: Optional[FranchiseLeader] = None
    all_time_scoring_leader: Optional[FranchiseLeader] = None
    all_time_av_leader: Optional[FranchiseLeader] = None
    winningest_coach: Optional[FranchiseLeader] = None


# --- Franchise Season Record (one row of team_index table) ---


class FranchiseSeasonRecord(PFRBaseModel):
    """A single season row from the franchise team_index table."""

    year_id: str
    year_href: Optional[str] = None
    league_id: Optional[str] = None
    league_href: Optional[str] = None
    team: str
    team_href: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    ties: Optional[int] = None
    div_finish: Optional[str] = None
    playoff_result: Optional[str] = None
    playoff_result_href: Optional[str] = None
    points: Optional[int] = None
    points_opp: Optional[int] = None
    points_diff: Optional[int] = None
    coaches: Optional[str] = None
    coaches_href: Optional[str] = None
    av: Optional[str] = None
    av_title: Optional[str] = None
    av_href: Optional[str] = None
    passer: Optional[str] = None
    passer_title: Optional[str] = None
    passer_href: Optional[str] = None
    rusher: Optional[str] = None
    rusher_title: Optional[str] = None
    rusher_href: Optional[str] = None
    receiver: Optional[str] = None
    receiver_title: Optional[str] = None
    receiver_href: Optional[str] = None
    rank_off_pts: Optional[int] = None
    rank_off_yds: Optional[int] = None
    rank_def_pts: Optional[int] = None
    rank_def_yds: Optional[int] = None
    rank_takeaway_giveaway: Optional[int] = None
    rank_points_diff: Optional[int] = None
    rank_yds_diff: Optional[int] = None
    teams_in_league: Optional[int] = None
    mov: Optional[float] = None
    sos_total: Optional[float] = None
    srs_total: Optional[float] = None
    srs_offense: Optional[float] = None
    srs_defense: Optional[float] = None


# --- Top-level Team Franchise ---


class Franchise(PFRBaseModel):
    """Top-level model for a PFR team franchise page."""

    meta: FranchiseMeta
    team_index: List[FranchiseSeasonRecord]
