from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.team_score import TeamScore
from griddy.nfl.models.enums.game_phase_enum import GamePhaseEnum
from griddy.nfl.types import BaseModel


class GameScore(BaseModel):
    """Score details for a game."""

    away_score: Annotated[Optional[int], pydantic.Field(alias="awayScore")] = None
    r"""Away team current score"""

    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None
    r"""Home team current score"""

    home_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="homeTeamScore")
    ] = None

    phase: Optional[GamePhaseEnum] = None
    r"""Game phase (P=Pregame, 1-4=Quarter, FINAL=Final)"""

    time: Optional[str] = None
    r"""Game clock time or status"""

    visitor_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="visitorTeamScore")
    ] = None
