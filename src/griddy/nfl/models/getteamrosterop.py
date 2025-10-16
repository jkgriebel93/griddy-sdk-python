from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


class GetTeamRosterRequestTypedDict(TypedDict):
    team_id: str
    r"""Team identifier (4-digit string)"""
    season: int
    r"""Season year"""


class GetTeamRosterRequest(BaseModel):
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
