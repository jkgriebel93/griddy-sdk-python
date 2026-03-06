from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetPlayerRequest(BaseModel):
    """Request parameters for fetching a player."""

    nfl_id: Annotated[
        int,
        pydantic.Field(alias="nflId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""NFL player identifier"""
