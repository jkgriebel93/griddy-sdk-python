from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .defensivenearestdefenderstats import (
    DefensiveNearestDefenderStats,
    DefensiveNearestDefenderStatsTypedDict,
)
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum


class NearestDefenderStatsResponseTypedDict(TypedDict):
    defenders: List[DefensiveNearestDefenderStatsTypedDict]
    limit: int
    r"""Maximum number of results returned"""
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
    r"""Total number of players matching the criteria"""
    qualified_defender: NotRequired[bool]
    r"""Whether results are filtered to qualified defenders only"""


class NearestDefenderStatsResponse(BaseModel):
    defenders: List[DefensiveNearestDefenderStats]

    limit: int
    r"""Maximum number of results returned"""

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
    r"""Total number of players matching the criteria"""

    qualified_defender: Annotated[
        Optional[bool], pydantic.Field(alias="qualifiedDefender")
    ] = None
    r"""Whether results are filtered to qualified defenders only"""
