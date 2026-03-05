from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..base import PFRBaseModel


class TopPlayerSummary(PFRBaseModel):
    name: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    description: str


class MultiTeamPlayerStats(PFRBaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    stats: Dict[str, Any]


class StatsTable(PFRBaseModel):
    category: str
    teams: List[str]
    players: List[MultiTeamPlayerStats]


class MultiTeamPlayers(PFRBaseModel):
    title: str
    total_players: Optional[int] = None
    teams: List[str]
    top_players: List[TopPlayerSummary]
    stats_tables: List[StatsTable]
