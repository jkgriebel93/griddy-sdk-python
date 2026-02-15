from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class LiveTeamStatisticsResponseTypedDict(TypedDict):
    game_id: NotRequired[Optional[str]]
    offset: NotRequired[Optional[int]]
    away_team: NotRequired[Optional[Dict[str, Any]]]
    home_team: NotRequired[Optional[Dict[str, Any]]]


class LiveTeamStatisticsResponse(BaseModel):
    r"""Live team statistics for a game.

    The awayTeam and homeTeam fields each contain a teamId and 100+ stat
    fields with camelCase keys (defensiveFumblesForced, passingYards, etc.).
    """

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None

    offset: Optional[int] = None

    away_team: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="awayTeam")] = (
        None
    )

    home_team: Annotated[Optional[Dict[str, Any]], pydantic.Field(alias="homeTeam")] = (
        None
    )
