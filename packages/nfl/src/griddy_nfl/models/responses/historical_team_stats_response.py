from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.historical_stat_categories import (
    HistoricalStatCategories,
    HistoricalStatCategoriesTypedDict,
)
from griddy_nfl.models.entities.team import Team, TeamTypedDict
from griddy_nfl.models.entities.venue import Venue, VenueTypedDict
from griddy_nfl.types import BaseModel


class HistoricalGameInfoTypedDict(TypedDict):
    id: str
    home_team: NotRequired[Optional[TeamTypedDict]]
    away_team: NotRequired[Optional[TeamTypedDict]]
    game_time: NotRequired[Optional[str]]
    venue: NotRequired[Optional[VenueTypedDict]]


class HistoricalGameInfo(BaseModel):
    id: str

    home_team: Annotated[Optional[Team], pydantic.Field(alias="homeTeam")] = None

    away_team: Annotated[Optional[Team], pydantic.Field(alias="awayTeam")] = None

    game_time: Annotated[Optional[str], pydantic.Field(alias="gameTime")] = None

    venue: Optional[Venue] = None


class HistoricalTeamStatsResponseTypedDict(TypedDict):
    game: NotRequired[Optional[HistoricalGameInfoTypedDict]]
    team: NotRequired[Optional[TeamTypedDict]]
    stats: NotRequired[Optional[HistoricalStatCategoriesTypedDict]]


class HistoricalTeamStatsResponse(BaseModel):
    r"""Historical team statistics for a specific game.

    The stats field contains typed stat category models for defense,
    passing, rushing, receiving, kicking, and other categories.
    """

    game: Optional[HistoricalGameInfo] = None

    team: Optional[Team] = None

    stats: Optional[HistoricalStatCategories] = None
