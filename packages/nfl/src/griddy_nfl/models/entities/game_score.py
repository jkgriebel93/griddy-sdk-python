from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.team_score import TeamScore, TeamScoreTypedDict
from griddy_nfl.models.enums.game_phase_enum import GamePhaseEnum
from griddy_nfl.types import BaseModel


class GameScoreTypedDict(TypedDict):
    away_score: NotRequired[int]
    r"""Away team current score"""
    home_score: NotRequired[int]
    r"""Home team current score"""
    home_team_score: NotRequired[TeamScoreTypedDict]
    phase: NotRequired[GamePhaseEnum]
    r"""Game phase (P=Pregame, 1-4=Quarter, FINAL=Final)"""
    time: NotRequired[str]
    r"""Game clock time or status"""
    visitor_team_score: NotRequired[TeamScoreTypedDict]


class GameScore(BaseModel):
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
