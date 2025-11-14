from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetTeamScheduleRequestTypedDict(TypedDict):
    team_id: str
    r"""Team identifier (4-digit string)"""
    season: int
    r"""Season year"""


class GetTeamScheduleRequest(BaseModel):
    team_id: Annotated[
        str,
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Team identifier (4-digit string)"""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""
