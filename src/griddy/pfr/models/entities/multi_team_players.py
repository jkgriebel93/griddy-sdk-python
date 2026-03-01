from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class TopPlayerSummaryTypedDict(TypedDict):
    name: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    description: str


class TopPlayerSummary(BaseModel):
    name: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    description: str


class MultiTeamPlayerStatsTypedDict(TypedDict):
    player: str
    player_href: NotRequired[Optional[str]]
    player_id: NotRequired[Optional[str]]
    stats: Dict[str, Any]


class MultiTeamPlayerStats(BaseModel):
    player: str
    player_href: Optional[str] = None
    player_id: Optional[str] = None
    stats: Dict[str, Any]


class StatsTableTypedDict(TypedDict):
    category: str
    teams: List[str]
    players: List[MultiTeamPlayerStatsTypedDict]


class StatsTable(BaseModel):
    category: str
    teams: List[str]
    players: List[MultiTeamPlayerStats]


class MultiTeamPlayersTypedDict(TypedDict):
    title: str
    total_players: NotRequired[Optional[int]]
    teams: List[str]
    top_players: List[TopPlayerSummaryTypedDict]
    stats_tables: List[StatsTableTypedDict]


class MultiTeamPlayers(BaseModel):
    title: str
    total_players: Optional[int] = None
    teams: List[str]
    top_players: List[TopPlayerSummary]
    stats_tables: List[StatsTable]
