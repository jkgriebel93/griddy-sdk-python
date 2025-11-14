from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .team_rankings import TeamRankings, TeamRankingsTypedDict


class TeamRankingsResponseTypedDict(TypedDict):
    away_rankings: NotRequired[TeamRankingsTypedDict]
    home_rankings: NotRequired[TeamRankingsTypedDict]


class TeamRankingsResponse(BaseModel):
    away_rankings: Annotated[
        Optional[TeamRankings], pydantic.Field(alias="awayRankings")
    ] = None

    home_rankings: Annotated[
        Optional[TeamRankings], pydantic.Field(alias="homeRankings")
    ] = None
