from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

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


class GetSeasonContentInsightsRequest(BaseModel):
    """Request parameters for fetching season content insights."""

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
