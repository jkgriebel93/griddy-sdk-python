from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.player_game_stats import (
    PlayerGameStats,
)
from griddy.nfl.models.entities.pro_game import ProGame
from griddy.nfl.models.entities.scoring_play import ScoringPlay
from griddy.nfl.models.entities.team_game_stats import (
    TeamGameStats,
)
from griddy.nfl.types import BaseModel


class Away(BaseModel):
    defense: Optional[List[PlayerGameStats]] = None

    offense: Optional[List[PlayerGameStats]] = None


class Home(BaseModel):
    defense: Optional[List[PlayerGameStats]] = None

    offense: Optional[List[PlayerGameStats]] = None


class PlayerStats(BaseModel):
    away: Optional[Away] = None

    home: Optional[Home] = None


class TeamStats(BaseModel):
    away: Optional[TeamGameStats] = None

    home: Optional[TeamGameStats] = None


class BoxScoreResponse2(BaseModel):
    game: Optional[ProGame] = None

    player_stats: Annotated[
        Optional[PlayerStats], pydantic.Field(alias="playerStats")
    ] = None

    scoring_summary: Annotated[
        Optional[List[ScoringPlay]], pydantic.Field(alias="scoringSummary")
    ] = None

    team_stats: Annotated[Optional[TeamStats], pydantic.Field(alias="teamStats")] = None
