
from __future__ import annotations
from .playerreceivingstats import PlayerReceivingStats, PlayerReceivingStatsTypedDict
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum
from ..types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


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
    sort_key: str
    r"""Field used for sorting"""
    sort_value: SortOrderEnum
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

    sort_key: Annotated[str, pydantic.Field(alias="sortKey")]
    r"""Field used for sorting"""

    sort_value: Annotated[SortOrderEnum, pydantic.Field(alias="sortValue")]
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
