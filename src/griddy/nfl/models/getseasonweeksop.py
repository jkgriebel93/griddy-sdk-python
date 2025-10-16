from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetSeasonWeeksRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    limit: NotRequired[int]
    r"""Maximum number of weeks to return"""


class GetSeasonWeeksRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Season year"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of weeks to return"""
