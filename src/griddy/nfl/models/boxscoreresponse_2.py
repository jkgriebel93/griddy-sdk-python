from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .playergamestats import PlayerGameStats, PlayerGameStatsTypedDict
from .progame import ProGame, ProGameTypedDict
from .scoringplay import ScoringPlay, ScoringPlayTypedDict
from .teamgamestats import TeamGameStats, TeamGameStatsTypedDict


class AwayTypedDict(TypedDict):
    defense: NotRequired[List[PlayerGameStatsTypedDict]]
    offense: NotRequired[List[PlayerGameStatsTypedDict]]


class Away(BaseModel):
    defense: Optional[List[PlayerGameStats]] = None

    offense: Optional[List[PlayerGameStats]] = None


class HomeTypedDict(TypedDict):
    defense: NotRequired[List[PlayerGameStatsTypedDict]]
    offense: NotRequired[List[PlayerGameStatsTypedDict]]


class Home(BaseModel):
    defense: Optional[List[PlayerGameStats]] = None

    offense: Optional[List[PlayerGameStats]] = None


class PlayerStatsTypedDict(TypedDict):
    away: NotRequired[AwayTypedDict]
    home: NotRequired[HomeTypedDict]


class PlayerStats(BaseModel):
    away: Optional[Away] = None

    home: Optional[Home] = None


class TeamStatsTypedDict(TypedDict):
    away: NotRequired[TeamGameStatsTypedDict]
    home: NotRequired[TeamGameStatsTypedDict]


class TeamStats(BaseModel):
    away: Optional[TeamGameStats] = None

    home: Optional[TeamGameStats] = None


class BoxScoreResponse2TypedDict(TypedDict):
    game: NotRequired[ProGameTypedDict]
    player_stats: NotRequired[PlayerStatsTypedDict]
    scoring_summary: NotRequired[List[ScoringPlayTypedDict]]
    team_stats: NotRequired[TeamStatsTypedDict]


class BoxScoreResponse2(BaseModel):
    game: Optional[ProGame] = None

    player_stats: Annotated[
        Optional[PlayerStats], pydantic.Field(alias="playerStats")
    ] = None

    scoring_summary: Annotated[
        Optional[List[ScoringPlay]], pydantic.Field(alias="scoringSummary")
    ] = None

    team_stats: Annotated[Optional[TeamStats], pydantic.Field(alias="teamStats")] = None
