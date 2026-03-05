from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.game_phase_enum import GamePhaseEnum
from griddy.nfl.types import BaseModel


class AwayTeam(BaseModel):
    abbreviation: Optional[str] = None

    score: Optional[int] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None


class HomeTeam(BaseModel):
    abbreviation: Optional[str] = None

    score: Optional[int] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None


class LiveGame(BaseModel):
    r"""Live game scoring and status information"""

    away_team: Annotated[Optional[AwayTeam], pydantic.Field(alias="awayTeam")] = None

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier"""

    home_team: Annotated[Optional[HomeTeam], pydantic.Field(alias="homeTeam")] = None

    last_play: Annotated[Optional[str], pydantic.Field(alias="lastPlay")] = None
    r"""Description of last play"""

    possession: Optional[str] = None
    r"""Team abbreviation with current possession"""

    quarter: Optional[str] = None
    r"""Current quarter/period"""

    red_zone: Annotated[Optional[bool], pydantic.Field(alias="redZone")] = None
    r"""Whether team is in red zone"""

    status: Optional[GamePhaseEnum] = None

    time_remaining: Annotated[Optional[str], pydantic.Field(alias="timeRemaining")] = (
        None
    )
    r"""Time remaining in current period"""
