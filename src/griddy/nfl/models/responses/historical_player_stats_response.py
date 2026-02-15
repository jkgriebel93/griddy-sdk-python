from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class PersonStatLineupTypedDict(TypedDict):
    games_dnp: NotRequired[Optional[int]]
    games_ina: NotRequired[Optional[int]]
    games_played: NotRequired[Optional[int]]
    games_started: NotRequired[Optional[int]]
    games_sub: NotRequired[Optional[int]]


class PersonStatLineup(BaseModel):
    games_dnp: Annotated[Optional[int], pydantic.Field(alias="gamesDnp")] = None
    games_ina: Annotated[Optional[int], pydantic.Field(alias="gamesIna")] = None
    games_played: Annotated[Optional[int], pydantic.Field(alias="gamesPlayed")] = None
    games_started: Annotated[Optional[int], pydantic.Field(alias="gamesStarted")] = None
    games_sub: Annotated[Optional[int], pydantic.Field(alias="gamesSub")] = None


class PersonStatTypedDict(TypedDict):
    person: NotRequired[Optional[str]]
    role: NotRequired[Optional[str]]
    lineup: NotRequired[Optional[PersonStatLineupTypedDict]]
    stats: NotRequired[Optional[Dict[str, Any]]]


class PersonStat(BaseModel):
    r"""Individual player statistics for a game.

    The stats field contains nullable stat category objects (defense,
    passing, rushing, receiving, etc.) with camelCase keys.
    """

    person: Optional[str] = None

    role: Optional[str] = None

    lineup: Optional[PersonStatLineup] = None

    stats: Optional[Dict[str, Any]] = None


class HistoricalPlayerStatsResponseTypedDict(TypedDict):
    game: NotRequired[Optional[str]]
    team: NotRequired[Optional[str]]
    person_stats: NotRequired[Optional[List[PersonStatTypedDict]]]


class HistoricalPlayerStatsResponse(BaseModel):
    r"""Historical player statistics for a specific game and team."""

    game: Optional[str] = None

    team: Optional[str] = None

    person_stats: Annotated[
        Optional[List[PersonStat]], pydantic.Field(alias="personStats")
    ] = None
