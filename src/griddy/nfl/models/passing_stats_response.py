from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum

from ..types import BaseModel
from .playerpassingstats import PlayerPassingStats, PlayerPassingStatsTypedDict


class PassingStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    passers: List[PlayerPassingStatsTypedDict]
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
    qualified_passer: NotRequired[bool]
    r"""Whether results are filtered to qualified passers only"""


class PassingStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offset: int
    r"""Number of records skipped"""

    passers: List[PlayerPassingStats]

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

    qualified_passer: Annotated[
        Optional[bool], pydantic.Field(alias="qualifiedPasser")
    ] = None
    r"""Whether results are filtered to qualified passers only"""
