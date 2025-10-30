from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata

Tag = Literal[
    "nfl-pro",
    "editorial",
    "next-gen-stats",
    "pregame",
    "postgame",
    "fantasy",
    "pro-preview",
    "pro-matchup",
    "evergreen",
]


class GetSeasonContentInsightsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    limit: NotRequired[int]
    r"""Maximum number of insights to return"""
    tags: NotRequired[List[Tag]]
    r"""Content tags to filter by (supports multiple comma-separated tags)"""
    team_id: NotRequired[str]
    r"""Filter by specific team identifier"""
    nfl_id: NotRequired[str]
    r"""Filter by specific player NFL identifier"""


class GetSeasonContentInsightsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of insights to return"""

    tags: Annotated[
        Optional[List[Tag]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Content tags to filter by (supports multiple comma-separated tags)"""

    team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific team identifier"""

    nfl_id: Annotated[
        Optional[str],
        pydantic.Field(alias="nflId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific player NFL identifier"""
