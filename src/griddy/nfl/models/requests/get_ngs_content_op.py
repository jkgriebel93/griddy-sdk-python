"""Request models for NGS content endpoints (charts, highlights)."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsChartsRequest(BaseModel):
    """Request model for getting NGS charts."""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    count: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 12

    week: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "all"

    chart_type: Annotated[
        Optional[str],
        pydantic.Field(alias="type"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "all"

    team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "all"

    esb_id: Annotated[
        Optional[str],
        pydantic.Field(alias="esbId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "all"


class GetNgsHighlightsRequest(BaseModel):
    """Request model for getting NGS highlights."""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 16
