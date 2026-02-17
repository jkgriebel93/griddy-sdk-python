"""Request model for NGS rushing stats endpoint."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetNgsRushingStatsRequestTypedDict(TypedDict):
    """Request parameters for getting NGS rushing stats."""

    season: int
    r"""Season year (e.g., 2025)"""
    season_type: str
    r"""Season type (REG, PRE, POST)"""
    week: NotRequired[int]
    r"""Optional week filter"""


class GetNgsRushingStatsRequest(BaseModel):
    """Request model for getting NGS rushing stats."""

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
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional week filter"""
