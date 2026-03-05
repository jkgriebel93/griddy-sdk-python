from __future__ import annotations

from typing import Any, Dict, List, Optional

from ...types import BaseModel


class TopPlayerSummary(BaseModel):
    name: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    description: str


class MultiTeamPlayerStats(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    stats: Dict[str, Any]


class StatsTable(BaseModel):
    category: str
    teams: List[str]
    players: List[MultiTeamPlayerStats]


class MultiTeamPlayers(BaseModel):
    title: str
    total_players: Optional[int] = None
    teams: List[str]
    top_players: List[TopPlayerSummary]
    stats_tables: List[StatsTable]
