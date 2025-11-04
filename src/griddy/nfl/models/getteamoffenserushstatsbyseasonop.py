from typing import Literal, Optional, TypedDict

import pydantic
from typing_extensions import Annotated, NotRequired

from griddy.nfl.types import BaseModel

GetTeamOffenseRushStatsBySeasonSortKey = Literal["rushYpg"]

from griddy.nfl.models.seasontypeenum import SeasonTypeEnum
from griddy.nfl.models.sortorderenum import SortOrderEnum
from griddy.nfl.models.weekslugenum import WeekSlugEnum
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetTeamOffenseRushStatsBySeasonRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    limit: NotRequired[int]
    r"""Maximum number of teams to return"""
    offset: NotRequired[int]
    r"""Number of records to skip for pagination"""
    page: NotRequired[int]
    r"""Page number for pagination"""
    sort_key: NotRequired[GetTeamOffenseRushStatsBySeasonSortKey]
    r"""Field to sort by"""
    sort_value: NotRequired[SortOrderEnum]
    r"""Sort direction"""


class GetTeamOffenseRushStatsBySeasonRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 35
    r"""Maximum number of teams to return"""

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Number of records to skip for pagination"""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number for pagination"""

    sort_key: Annotated[
        Optional[GetTeamOffenseRushStatsBySeasonSortKey],
        pydantic.Field(alias="sortKey"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "passYpg"
    r"""Field to sort by"""

    sort_value: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortValue"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sort direction"""
