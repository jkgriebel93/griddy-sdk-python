from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


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
