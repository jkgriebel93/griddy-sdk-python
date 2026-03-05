"""Pydantic models for PFR Fantasy Rankings pages.

Covers:
- ``/years/{year}/fantasy.htm`` — Top Fantasy Players (table ``#fantasy``)
- ``/fantasy/{position}-fantasy-matchups.htm`` — Fantasy Matchups
  (table ``#fantasy_stats``)
- ``/years/{year}/fantasy-points-against-{position}.htm`` — Fantasy Points
  Allowed (table ``#fantasy_def``)
- ``/years/{year}/redzone-passing.htm`` — Red Zone Passing
  (table ``#fantasy_rz``)
- ``/years/{year}/redzone-receiving.htm`` — Red Zone Receiving
  (table ``#fantasy_rz``)
- ``/years/{year}/redzone-rushing.htm`` — Red Zone Rushing
  (table ``#fantasy_rz``)
"""

from __future__ import annotations

from typing import Any, List, Optional

from ..base import PFRBaseModel

# ---------------------------------------------------------------------------
# FantasyPlayer (one row in /years/{year}/fantasy.htm)
# ---------------------------------------------------------------------------


class FantasyPlayer(PFRBaseModel):
    rank: Optional[int] = None
    player: Optional[str] = None
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    fantasy_pos: Optional[str] = None
    age: Optional[int] = None
    # Games
    g: Optional[int] = None
    gs: Optional[int] = None
    # Passing
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_int: Optional[int] = None
    # Rushing
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_yds_per_att: Optional[float] = None
    rush_td: Optional[int] = None
    # Receiving
    targets: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_yds_per_rec: Optional[float] = None
    rec_td: Optional[int] = None
    # Fumbles
    fumbles: Optional[int] = None
    fumbles_lost: Optional[int] = None
    # Scoring
    all_td: Optional[int] = None
    two_pt_md: Optional[int] = None
    two_pt_pass: Optional[int] = None
    # Fantasy
    fantasy_points: Optional[float] = None
    fantasy_points_ppr: Optional[float] = None
    draftkings_points: Optional[float] = None
    fanduel_points: Optional[float] = None
    vbd: Optional[int] = None
    fantasy_rank_pos: Optional[int] = None
    fantasy_rank_overall: Optional[int] = None


# ---------------------------------------------------------------------------
# TopFantasyPlayers (top-level for /years/{year}/fantasy.htm)
# ---------------------------------------------------------------------------


class TopFantasyPlayers(PFRBaseModel):
    players: List[FantasyPlayer] = []


# ---------------------------------------------------------------------------
# FantasyMatchupPlayer (one row in /fantasy/{position}-fantasy-matchups.htm)
# ---------------------------------------------------------------------------


class FantasyMatchupPlayer(PFRBaseModel):
    player: Optional[str] = None
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    injury: Optional[str] = None
    # Games
    g: Optional[int] = None
    gs: Optional[int] = None
    snaps: Optional[str] = None
    # Passing (QB only)
    pass_cmp: Optional[float] = None
    pass_att: Optional[float] = None
    pass_yds: Optional[float] = None
    pass_td: Optional[float] = None
    pass_int: Optional[float] = None
    pass_sacked: Optional[float] = None
    # Rushing (QB / RB)
    rush_att: Optional[float] = None
    rush_yds: Optional[float] = None
    rush_td: Optional[float] = None
    # Receiving (WR / RB / TE)
    targets: Optional[float] = None
    rec: Optional[float] = None
    rec_yds: Optional[float] = None
    rec_td: Optional[float] = None
    # Fantasy per game
    fantasy_points_per_game: Optional[float] = None
    draftkings_points_per_game: Optional[float] = None
    fanduel_points_per_game: Optional[float] = None
    # Matchup
    at_or_vs: Optional[str] = None
    opp: Optional[str] = None
    opp_href: Optional[str] = None
    rank: Optional[int] = None
    # Opponent fantasy allowed per game
    opp_fantasy_points_per_game: Optional[float] = None
    opp_draftkings_points_per_game: Optional[float] = None
    opp_fanduel_points_per_game: Optional[float] = None
    # Projected ranks
    fantasy_points_proj_rank: Optional[int] = None
    draftkings_points_proj_rank: Optional[int] = None
    fanduel_points_proj_rank: Optional[int] = None


# ---------------------------------------------------------------------------
# FantasyMatchups (top-level for /fantasy/{position}-fantasy-matchups.htm)
# ---------------------------------------------------------------------------


class FantasyMatchups(PFRBaseModel):
    players: List[FantasyMatchupPlayer] = []


# ---------------------------------------------------------------------------
# FantasyPointsAllowedTeam
# (one row in /years/{year}/fantasy-points-against-{position}.htm)
# ---------------------------------------------------------------------------


class FantasyPointsAllowedTeam(PFRBaseModel):
    team: Optional[str] = None
    team_href: Optional[str] = None
    g: Optional[int] = None
    # Passing (QB only)
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_int: Optional[int] = None
    two_pt_pass: Optional[int] = None
    pass_sacked: Optional[int] = None
    # Rushing (QB / RB)
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_td: Optional[int] = None
    # Receiving (WR / RB / TE)
    targets: Optional[int] = None
    rec: Optional[int] = None
    rec_yds: Optional[int] = None
    rec_td: Optional[int] = None
    # Scoring (WR / RB / TE)
    two_pt_md: Optional[int] = None
    # Fumbles (WR / RB / TE)
    fumbles_lost: Optional[int] = None
    # Fantasy totals
    fantasy_points: Optional[float] = None
    draftkings_points: Optional[float] = None
    fanduel_points: Optional[float] = None
    # Fantasy per game
    fantasy_points_per_game: Optional[float] = None
    draftkings_points_per_game: Optional[float] = None
    fanduel_points_per_game: Optional[float] = None


# ---------------------------------------------------------------------------
# FantasyPointsAllowed
# (top-level for /years/{year}/fantasy-points-against-{position}.htm)
# ---------------------------------------------------------------------------


class FantasyPointsAllowed(PFRBaseModel):
    teams: List[FantasyPointsAllowedTeam] = []


# ---------------------------------------------------------------------------
# RedZonePassingPlayer (one row in /years/{year}/redzone-passing.htm)
# ---------------------------------------------------------------------------


class RedZonePassingPlayer(PFRBaseModel):
    player: Optional[str] = None
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    # Inside 20
    pass_cmp: Optional[int] = None
    pass_att: Optional[int] = None
    pass_cmp_perc: Optional[float] = None
    pass_yds: Optional[int] = None
    pass_td: Optional[int] = None
    pass_int: Optional[int] = None
    # Inside 10
    pass_cmp_in_10: Optional[int] = None
    pass_att_in_10: Optional[int] = None
    pass_cmp_perc_in_10: Optional[float] = None
    pass_yds_in_10: Optional[int] = None
    pass_td_in_10: Optional[int] = None
    pass_int_in_10: Optional[int] = None
    # Link
    link_href: Optional[str] = None


# ---------------------------------------------------------------------------
# RedZonePassing (top-level for /years/{year}/redzone-passing.htm)
# ---------------------------------------------------------------------------


class RedZonePassing(PFRBaseModel):
    players: List[RedZonePassingPlayer] = []


# ---------------------------------------------------------------------------
# RedZoneReceivingPlayer (one row in /years/{year}/redzone-receiving.htm)
# ---------------------------------------------------------------------------


class RedZoneReceivingPlayer(PFRBaseModel):
    player: Optional[str] = None
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    # Inside 20
    targets: Optional[int] = None
    rec: Optional[int] = None
    catch_pct: Optional[float] = None
    rec_yds: Optional[int] = None
    rec_td: Optional[int] = None
    targets_pct: Optional[float] = None
    # Inside 10
    targets_in_10: Optional[int] = None
    rec_in_10: Optional[int] = None
    catch_pct_in_10: Optional[float] = None
    rec_yds_in_10: Optional[int] = None
    rec_td_in_10: Optional[int] = None
    targets_in_10_pct: Optional[float] = None
    # Link
    link_href: Optional[str] = None


# ---------------------------------------------------------------------------
# RedZoneReceiving (top-level for /years/{year}/redzone-receiving.htm)
# ---------------------------------------------------------------------------


class RedZoneReceiving(PFRBaseModel):
    players: List[RedZoneReceivingPlayer] = []


# ---------------------------------------------------------------------------
# RedZoneRushingPlayer (one row in /years/{year}/redzone-rushing.htm)
# ---------------------------------------------------------------------------


class RedZoneRushingPlayer(PFRBaseModel):
    player: Optional[str] = None
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    team: Optional[str] = None
    team_href: Optional[str] = None
    # Inside 20
    rush_att: Optional[int] = None
    rush_yds: Optional[int] = None
    rush_td: Optional[int] = None
    rush_att_pct: Optional[float] = None
    # Inside 10
    rush_att_in_10: Optional[int] = None
    rush_yds_in_10: Optional[int] = None
    rush_td_in_10: Optional[int] = None
    rush_att_in_10_pct: Optional[float] = None
    # Inside 5
    rush_att_in_5: Optional[int] = None
    rush_yds_in_5: Optional[int] = None
    rush_td_in_5: Optional[int] = None
    rush_att_in_5_pct: Optional[float] = None
    # Link
    link_href: Optional[str] = None


# ---------------------------------------------------------------------------
# RedZoneRushing (top-level for /years/{year}/redzone-rushing.htm)
# ---------------------------------------------------------------------------


class RedZoneRushing(PFRBaseModel):
    players: List[RedZoneRushingPlayer] = []
