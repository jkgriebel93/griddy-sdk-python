from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.live_stat_entries import (
    LivePlayerTeamEntry,
)
from griddy.nfl.types import BaseModel


class LivePlayerStatisticsResponse(BaseModel):
    r"""Live player statistics for a game.

    The awayTeam and homeTeam fields each contain a teamId and a players
    array. Each player has identification fields (gsisPlayerId, gsisPlayerName,
    personId) and 100+ stat fields.
    """

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None

    offset: Optional[int] = None

    away_team: Annotated[
        Optional[LivePlayerTeamEntry], pydantic.Field(alias="awayTeam")
    ] = None

    home_team: Annotated[
        Optional[LivePlayerTeamEntry], pydantic.Field(alias="homeTeam")
    ] = None
