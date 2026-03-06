from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.team_offense_overview_stats import TeamOffenseStats
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel


class TeamOffenseStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offense: List[TeamOffenseStats]

    offset: int
    r"""Number of records skipped"""

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    sort_key: Annotated[Optional[str], pydantic.Field(alias="sortKey")] = None
    r"""Field used for sorting"""

    sort_value: Annotated[
        Optional[SortOrderEnum], pydantic.Field(alias="sortValue")
    ] = None
    r"""Sort direction for ordered results"""

    total: int
    r"""Total number of teams matching the criteria"""

    split: Optional[List[str]] = None
    r"""Applied offensive situation splits"""

    team_defense: Annotated[Optional[str], pydantic.Field(alias="teamDefense")] = None
    r"""Team filter applied (if any)"""
