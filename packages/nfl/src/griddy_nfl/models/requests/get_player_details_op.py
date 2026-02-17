from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetPlayerDetailsRequestTypedDict(TypedDict):
    player_id: str
    r"""Player identifier"""
    season: NotRequired[int]
    r"""Season for statistics (defaults to current)"""


class GetPlayerDetailsRequest(BaseModel):
    player_id: Annotated[
        str,
        pydantic.Field(alias="playerId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Player identifier"""

    season: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Season for statistics (defaults to current)"""
