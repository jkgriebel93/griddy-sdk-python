from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetPlayerRequestTypedDict(TypedDict):
    nfl_id: int
    r"""NFL player identifier"""


class GetPlayerRequest(BaseModel):
    nfl_id: Annotated[
        int,
        pydantic.Field(alias="nflId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""NFL player identifier"""
