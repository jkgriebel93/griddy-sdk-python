
from __future__ import annotations
from ..types import BaseModel
from ..utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetPlayByPlayRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (UUID)"""
    include_penalties: NotRequired[bool]
    r"""Include penalty details"""
    include_formations: NotRequired[bool]
    r"""Include offensive/defensive formations"""


class GetPlayByPlayRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game identifier (UUID)"""

    include_penalties: Annotated[
        Optional[bool],
        pydantic.Field(alias="includePenalties"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include penalty details"""

    include_formations: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeFormations"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include offensive/defensive formations"""
