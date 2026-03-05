from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import BaseModel
from .statistic_ranking import StatisticRanking


class TeamRankings(BaseModel):
    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    statistics: Optional[List[StatisticRanking]] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
