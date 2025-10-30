
from __future__ import annotations
from ..types import BaseModel
from ..utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDraftInfoRequestTypedDict(TypedDict):
    year: int
    r"""Draft year"""
    round: NotRequired[int]
    r"""Filter by round"""
    team_id: NotRequired[str]
    r"""Filter by team"""


class GetDraftInfoRequest(BaseModel):
    year: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Draft year"""

    round: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by round"""

    team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by team"""
