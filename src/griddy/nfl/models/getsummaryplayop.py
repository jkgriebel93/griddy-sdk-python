from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


class GetSummaryPlayRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (UUID format)"""
    play_id: int
    r"""Play identifier within the game"""


class GetSummaryPlayRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier (UUID format)"""

    play_id: Annotated[
        int,
        pydantic.Field(alias="playId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Play identifier within the game"""
