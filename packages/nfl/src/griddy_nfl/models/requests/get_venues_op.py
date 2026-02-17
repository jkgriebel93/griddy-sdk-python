from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetVenuesRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    limit: NotRequired[int]
    r"""Maximum number of venues to return"""


class GetVenuesRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of venues to return"""
