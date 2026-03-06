from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.historical_stat_categories import (
    HistoricalStatCategories,
)
from griddy.nfl.models.entities.team import Team
from griddy.nfl.models.entities.venue import Venue
from griddy.nfl.types import BaseModel


class HistoricalGameInfo(BaseModel):
    """Historical game information with stats."""

    id: str

    home_team: Annotated[Optional[Team], pydantic.Field(alias="homeTeam")] = None

    away_team: Annotated[Optional[Team], pydantic.Field(alias="awayTeam")] = None

    game_time: Annotated[Optional[str], pydantic.Field(alias="gameTime")] = None

    venue: Optional[Venue] = None


class HistoricalTeamStatsResponse(BaseModel):
    r"""Historical team statistics for a specific game.

    The stats field contains typed stat category models for defense,
    passing, rushing, receiving, kicking, and other categories.
    """

    game: Optional[HistoricalGameInfo] = None

    team: Optional[Team] = None

    stats: Optional[HistoricalStatCategories] = None
