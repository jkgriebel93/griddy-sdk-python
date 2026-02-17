from typing import Optional, TypedDict

import pydantic
from typing_extensions import Annotated

from griddy_nfl.models.enums.combine_enums import EventFilterEnum
from griddy_nfl.models.enums.sort_order_enum import SortOrderEnum
from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetCombineRankingsRequestTypedDict(TypedDict):
    rank_attribute: EventFilterEnum
    r"""Which event to get rankings for"""
    sort_order: SortOrderEnum
    r"""Sort ascending or descending"""
    year: Optional[int]
    r"""Get performances only for the specified year. If omitted, get all time"""
    limit: int
    r"""Maximum number of rankings to fetch"""


class GetCombineRankingsRequest(BaseModel):
    rank_attribute: Annotated[
        Optional[EventFilterEnum],
        pydantic.Field(alias="rankAttribute"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Which event to get rankings for"""
    sort_order: Annotated[
        Optional[SortOrderEnum],
        pydantic.Field(alias="sortOrder"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Sort ascending or descending"""
    year: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Get performances only for the specified year. If omitted, get all time"""
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 25
    r"""Maximum number of rankings to fetch"""
