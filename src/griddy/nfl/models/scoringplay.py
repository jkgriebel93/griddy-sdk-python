
from __future__ import annotations
from .team import Team, TeamTypedDict
from ..types import BaseModel
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


ScoreType = Literal[
    "TOUCHDOWN",
    "FIELD_GOAL",
    "SAFETY",
    "EXTRA_POINT",
    "TWO_POINT_CONVERSION",
]


class ScoringPlayTypedDict(TypedDict):
    away_score: NotRequired[int]
    description: NotRequired[str]
    game_clock: NotRequired[str]
    home_score: NotRequired[int]
    quarter: NotRequired[int]
    score_type: NotRequired[ScoreType]
    team: NotRequired[TeamTypedDict]


class ScoringPlay(BaseModel):
    away_score: Annotated[Optional[int], pydantic.Field(alias="awayScore")] = None

    description: Optional[str] = None

    game_clock: Annotated[Optional[str], pydantic.Field(alias="gameClock")] = None

    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None

    quarter: Optional[int] = None

    score_type: Annotated[Optional[ScoreType], pydantic.Field(alias="scoreType")] = None

    team: Optional[Team] = None
