"""Request model for NGS full season schedule endpoint."""

from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsScheduleRequestTypedDict(TypedDict):
    """Request parameters for getting the full NGS schedule."""

    season: int
    r"""Season year (e.g., 2025)"""


class GetNgsScheduleRequest(BaseModel):
    """Request model for getting the full NGS schedule."""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year (e.g., 2025)"""
