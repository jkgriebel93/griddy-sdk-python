from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.team_rankings import TeamRankings
from griddy.nfl.types import BaseModel


class TeamRankingsResponse(BaseModel):
    away_rankings: Annotated[
        Optional[TeamRankings], pydantic.Field(alias="awayRankings")
    ] = None

    home_rankings: Annotated[
        Optional[TeamRankings], pydantic.Field(alias="homeRankings")
    ] = None
