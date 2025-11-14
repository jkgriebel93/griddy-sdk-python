from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .team_score import TeamScore, TeamScoreTypedDict


class BoxscoreScoreTypedDict(TypedDict):
    home_team_score: NotRequired[TeamScoreTypedDict]
    phase: NotRequired[str]
    r"""Game phase (P=Pregame, 1-4=Quarter, F=Final)"""
    visitor_team_score: NotRequired[TeamScoreTypedDict]


class BoxscoreScore(BaseModel):
    home_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="homeTeamScore")
    ] = None

    phase: Optional[str] = None
    r"""Game phase (P=Pregame, 1-4=Quarter, F=Final)"""

    visitor_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="visitorTeamScore")
    ] = None
