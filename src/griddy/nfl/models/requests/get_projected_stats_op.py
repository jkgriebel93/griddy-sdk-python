from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetProjectedStatsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    week: int
    r"""Week number within the season"""
    filter_nfl_team_id: NotRequired[str]
    r"""Filter by NFL team ID (UUID format)"""
    page_size: NotRequired[int]
    r"""Number of results per page"""


class GetProjectedStatsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number within the season"""

    filter_nfl_team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="filter[nflTeamId]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by NFL team ID (UUID format)"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="page[size]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results per page"""
