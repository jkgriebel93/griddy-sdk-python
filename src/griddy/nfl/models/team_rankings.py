from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .season_type_enum import SeasonTypeEnum
from .statistic_ranking import StatisticRanking, StatisticRankingTypedDict


class TeamRankingsTypedDict(TypedDict):
    season: NotRequired[int]
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    statistics: NotRequired[List[StatisticRankingTypedDict]]
    team_id: NotRequired[str]


class TeamRankings(BaseModel):
    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    statistics: Optional[List[StatisticRanking]] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
