from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .team import Team

ScoreType = Literal[
    "TOUCHDOWN",
    "FIELD_GOAL",
    "SAFETY",
    "EXTRA_POINT",
    "TWO_POINT_CONVERSION",
]


class ScoringPlay(BaseModel):
    """Scoring play within a game."""

    away_score: Annotated[Optional[int], pydantic.Field(alias="awayScore")] = None

    description: Optional[str] = None

    game_clock: Annotated[Optional[str], pydantic.Field(alias="gameClock")] = None

    home_score: Annotated[Optional[int], pydantic.Field(alias="homeScore")] = None

    quarter: Optional[int] = None

    score_type: Annotated[Optional[ScoreType], pydantic.Field(alias="scoreType")] = None

    team: Optional[Team] = None
