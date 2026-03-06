from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .team_score import TeamScore


class BoxscoreScore(BaseModel):
    """Score breakdown within a boxscore."""

    home_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="homeTeamScore")
    ] = None

    phase: Optional[str | int] = None
    r"""Game phase (P=Pregame, 1-4=Quarter, F=Final)"""

    visitor_team_score: Annotated[
        Optional[TeamScore], pydantic.Field(alias="visitorTeamScore")
    ] = None
