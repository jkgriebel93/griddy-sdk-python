from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.player_game_stats import (
    PlayerGameStats,
    PlayerGameStatsTypedDict,
)
from griddy_nfl.models.entities.pro_game import ProGame, ProGameTypedDict
from griddy_nfl.models.entities.scoring_play import ScoringPlay, ScoringPlayTypedDict
from griddy_nfl.models.entities.team_game_stats import (
    TeamGameStats,
    TeamGameStatsTypedDict,
)
from griddy_nfl.types import BaseModel


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
