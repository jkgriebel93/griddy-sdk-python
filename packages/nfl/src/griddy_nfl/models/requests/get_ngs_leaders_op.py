"""Request models for NGS leaders/top plays endpoints."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsLeadersRequestTypedDict(TypedDict):
    """Request parameters for NGS leaders endpoints with limit/week support."""

    season: int
    r"""Season year (e.g., 2025)"""
    season_type: str
    r"""Season type (REG, PRE, POST)"""
    limit: NotRequired[int]
    r"""Number of results to return (default: 20)"""
    week: NotRequired[int]
    r"""Optional week filter"""


class GetNgsLeadersRequest(BaseModel):
    """Request model for NGS leaders endpoints with limit/week support."""

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

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results to return (default: 20)"""

    week: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional week filter"""


class GetNgsSeasonLeadersRequestTypedDict(TypedDict):
    """Request parameters for NGS season-aggregated leaders (no week/limit)."""

    season: int
    r"""Season year (e.g., 2025)"""
    season_type: str
    r"""Season type (REG, PRE, POST)"""


class GetNgsSeasonLeadersRequest(BaseModel):
    """Request model for NGS season-aggregated leaders (no week/limit)."""

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
