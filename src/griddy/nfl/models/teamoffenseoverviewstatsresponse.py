from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum
from .teamoffenseoverviewstats import TeamOffenseStats, TeamOffenseStatsTypedDict


class TeamOffenseStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offense: List[TeamOffenseStatsTypedDict]
    offset: int
    r"""Number of records skipped"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sort_key: str
    r"""Field used for sorting"""
    sort_value: SortOrderEnum
    r"""Sort direction for ordered results"""
    total: int
    r"""Total number of teams matching the criteria"""
    split: NotRequired[List[str]]
    r"""Applied offensive situation splits"""
    team_defense: NotRequired[str]
    r"""Team filter applied (if any)"""


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

    sort_key: Annotated[str, pydantic.Field(alias="sortKey")]
    r"""Field used for sorting"""

    sort_value: Annotated[SortOrderEnum, pydantic.Field(alias="sortValue")]
    r"""Sort direction for ordered results"""

    total: int
    r"""Total number of teams matching the criteria"""

    split: Optional[List[str]] = None
    r"""Applied offensive situation splits"""

    team_defense: Annotated[Optional[str], pydantic.Field(alias="teamDefense")] = None
    r"""Team filter applied (if any)"""
