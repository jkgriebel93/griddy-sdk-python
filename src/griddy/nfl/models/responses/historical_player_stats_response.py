from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel


class PersonStatLineup(BaseModel):
    games_dnp: Annotated[Optional[int], pydantic.Field(alias="gamesDnp")] = None
    games_ina: Annotated[Optional[int], pydantic.Field(alias="gamesIna")] = None
    games_played: Annotated[Optional[int], pydantic.Field(alias="gamesPlayed")] = None
    games_started: Annotated[Optional[int], pydantic.Field(alias="gamesStarted")] = None
    games_sub: Annotated[Optional[int], pydantic.Field(alias="gamesSub")] = None


class PersonStat(BaseModel):
    r"""Individual player statistics for a game.

    The stats field contains nullable stat category objects (defense,
    passing, rushing, receiving, etc.) with camelCase keys.
    """

    person: Optional[str] = None

    role: Optional[str] = None

    lineup: Optional[PersonStatLineup] = None

    # TODO: Fill this in with a real type
    stats: Optional[Dict[str, Any]] = None


class HistoricalPlayerStatsResponse(BaseModel):
    r"""Historical player statistics for a specific game and team."""

    # TODO: Verify this object schema
    game: Optional[str] = None
    # TODO: Verify this object schema
    team: Optional[str] = None
    # TODO: Verify this object schema
    person_stats: Annotated[
        Optional[List[PersonStat]], pydantic.Field(alias="personStats")
    ] = None
