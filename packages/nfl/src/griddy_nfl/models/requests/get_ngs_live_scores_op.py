"""Request model for NGS live scores endpoint."""

from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsLiveScoresRequestTypedDict(TypedDict):
    """Request parameters for getting NGS live scores."""

    season: int
    r"""Season year (e.g., 2025)"""
    season_type: str
    r"""Season type (REG, PRE, POST)"""
    week: int
    r"""Week number"""


class GetNgsLiveScoresRequest(BaseModel):
    """Request model for getting NGS live scores."""

    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year (e.g., 2025)"""

    season_type: Annotated[
        str,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Season type (REG, PRE, POST)"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number"""
