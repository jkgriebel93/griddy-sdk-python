from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


class GetStatsBoxscoreRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (10-digit format YYYYMMDDNN)"""


class GetStatsBoxscoreRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier (10-digit format YYYYMMDDNN)"""
