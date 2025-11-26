from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.entities.player_receiving_stats import (
    PlayerReceivingStats,
    PlayerReceivingStatsTypedDict,
)
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy.nfl.types import BaseModel


class ReceivingStatsResponseTypedDict(TypedDict):
    limit: int
    r"""Maximum number of results returned"""
    offset: int
    r"""Number of records skipped"""
    receivers: List[PlayerReceivingStatsTypedDict]
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sort_key: NotRequired[str]
    r"""Field used for sorting"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction for ordered results"""
    total: int
    r"""Total number of players matching the criteria"""
    qualified_receiver: NotRequired[bool]
    r"""Whether results are filtered to qualified receivers only"""
    team_offense: NotRequired[str]
    r"""Team filter applied (if any)"""
    week: NotRequired[str]
    r"""Week identifier"""


class ReceivingStatsResponse(BaseModel):
    limit: int
    r"""Maximum number of results returned"""

    offset: int
    r"""Number of records skipped"""

    receivers: List[PlayerReceivingStats]

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
    r"""Total number of players matching the criteria"""

    qualified_receiver: Annotated[
        Optional[bool], pydantic.Field(alias="qualifiedReceiver")
    ] = None
    r"""Whether results are filtered to qualified receivers only"""

    team_offense: Annotated[Optional[str], pydantic.Field(alias="teamOffense")] = None
    r"""Team filter applied (if any)"""

    week: Optional[str] = None
    r"""Week identifier"""
