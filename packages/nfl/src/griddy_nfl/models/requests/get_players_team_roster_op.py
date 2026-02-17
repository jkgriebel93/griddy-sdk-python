from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetPlayersTeamRosterRequestTypedDict(TypedDict):
    team_id: str
    r"""Team identifier (UUID)"""
    season: int
    r"""Season year"""
    include_stats: NotRequired[bool]
    r"""Include current season statistics"""


class GetPlayersTeamRosterRequest(BaseModel):
    team_id: Annotated[
        str,
        pydantic.Field(alias="teamId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Team identifier (UUID)"""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    include_stats: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeStats"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include current season statistics"""
