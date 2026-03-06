"""Pydantic models for the PFR Multi-Team Players page.

Covers ``/friv/players-who-played-for-multiple-teams-in-one-season.htm``,
listing players who appeared for more than one team in a single season
along with their combined statistics.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..base import PFRBaseModel


class TopPlayerSummary(PFRBaseModel):
    """Brief summary of a notable multi-team player."""

    name: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    description: str


class MultiTeamPlayerStats(PFRBaseModel):
    """A player row in a multi-team stats table with arbitrary stat columns."""

    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    stats: Dict[str, Any]


class StatsTable(PFRBaseModel):
    """A single stat-category table of multi-team players."""

    category: str
    teams: List[str]
    players: List[MultiTeamPlayerStats]


class MultiTeamPlayers(PFRBaseModel):
    """Top-level result for the PFR multi-team players page."""

    title: str
    total_players: Optional[int] = None
    teams: List[str]
    top_players: List[TopPlayerSummary]
    stats_tables: List[StatsTable]
