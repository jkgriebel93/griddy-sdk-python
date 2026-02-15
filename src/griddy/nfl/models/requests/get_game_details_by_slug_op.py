from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetGameDetailsBySlugRequestTypedDict(TypedDict):
    slug: str
    r"""Game slug identifier"""
    include_replays: NotRequired[bool]
    r"""Include replay videos in response"""


class GetGameDetailsBySlugRequest(BaseModel):
    slug: Annotated[
        str,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game slug identifier"""

    include_replays: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeReplays"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include replay videos in response"""
