from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class HistoricalTeamInfoTypedDict(TypedDict):
    id: str
    current_logo: NotRequired[Optional[str]]
    full_name: NotRequired[Optional[str]]


class HistoricalTeamInfo(BaseModel):
    id: str

    current_logo: Annotated[Optional[str], pydantic.Field(alias="currentLogo")] = None

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None


class HistoricalGameVenueTypedDict(TypedDict):
    id: NotRequired[Optional[str]]
    name: NotRequired[Optional[str]]
    city: NotRequired[Optional[str]]
    country: NotRequired[Optional[str]]


class HistoricalGameVenue(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None


class HistoricalGameInfoTypedDict(TypedDict):
    id: str
    home_team: NotRequired[Optional[HistoricalTeamInfoTypedDict]]
    away_team: NotRequired[Optional[HistoricalTeamInfoTypedDict]]
    game_time: NotRequired[Optional[str]]
    venue: NotRequired[Optional[HistoricalGameVenueTypedDict]]


class HistoricalGameInfo(BaseModel):
    id: str

    home_team: Annotated[
        Optional[HistoricalTeamInfo], pydantic.Field(alias="homeTeam")
    ] = None

    away_team: Annotated[
        Optional[HistoricalTeamInfo], pydantic.Field(alias="awayTeam")
    ] = None

    game_time: Annotated[Optional[str], pydantic.Field(alias="gameTime")] = None

    venue: Optional[HistoricalGameVenue] = None


class HistoricalTeamStatsResponseTypedDict(TypedDict):
    game: NotRequired[Optional[HistoricalGameInfoTypedDict]]
    team: NotRequired[Optional[HistoricalTeamInfoTypedDict]]
    stats: NotRequired[Optional[Dict[str, Any]]]


class HistoricalTeamStatsResponse(BaseModel):
    r"""Historical team statistics for a specific game.

    The stats field contains deeply nested stat category objects (defense,
    passing, rushing, receiving, kicking, etc.) with camelCase keys.
    """

    game: Optional[HistoricalGameInfo] = None

    team: Optional[HistoricalTeamInfo] = None

    stats: Optional[Dict[str, Any]] = None
