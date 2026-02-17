from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.live_stat_entries import (
    LiveTeamStatEntry,
    LiveTeamStatEntryTypedDict,
)
from griddy_nfl.types import BaseModel


class LiveTeamStatisticsResponseTypedDict(TypedDict):
    game_id: NotRequired[Optional[str]]
    offset: NotRequired[Optional[int]]
    away_team: NotRequired[Optional[LiveTeamStatEntryTypedDict]]
    home_team: NotRequired[Optional[LiveTeamStatEntryTypedDict]]


class LiveTeamStatisticsResponse(BaseModel):
    r"""Live team statistics for a game.

    The awayTeam and homeTeam fields each contain a teamId and 100+ stat
    fields covering defense, passing, rushing, receiving, kicking, and more.
    """

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None

    offset: Optional[int] = None

    away_team: Annotated[
        Optional[LiveTeamStatEntry], pydantic.Field(alias="awayTeam")
    ] = None

    home_team: Annotated[
        Optional[LiveTeamStatEntry], pydantic.Field(alias="homeTeam")
    ] = None
