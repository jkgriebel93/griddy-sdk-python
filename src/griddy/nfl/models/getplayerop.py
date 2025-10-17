from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata


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
