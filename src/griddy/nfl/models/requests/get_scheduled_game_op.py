from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetScheduledGameRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier (UUID format)"""
