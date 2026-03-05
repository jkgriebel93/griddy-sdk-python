"""Request model for NGS game center overview endpoint."""

from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsGameOverviewRequest(BaseModel):
    """Request model for getting NGS game overview."""

    game_id: Annotated[
        int,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Unique game identifier (e.g., 2025112700)"""
