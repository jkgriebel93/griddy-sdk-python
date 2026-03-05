"""Request models for NGS news endpoints (api.nfl.com)."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsMixedContentRequest(BaseModel):
    """Request model for getting NGS mixed content."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 16

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0


class GetNgsArticlesRequest(BaseModel):
    """Request model for getting NGS articles."""

    category: Annotated[
        str,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 16

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0


class GetNgsVideoClipsRequest(BaseModel):
    """Request model for getting NGS video clips."""

    video_channel: Annotated[
        str,
        pydantic.Field(alias="videoChannel"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 16

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
