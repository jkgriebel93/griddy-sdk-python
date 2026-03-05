"""Request model for NGS full season schedule endpoint."""

from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsScheduleRequest(BaseModel):
    """Request model for getting the full NGS schedule."""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year (e.g., 2025)"""
