"""Response models for NGS stats endpoints (passing, receiving, rushing)."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.ngs_stats import (
    NgsPassingStat,
    NgsReceivingStat,
    NgsRushingStat,
)
from griddy.nfl.types import BaseModel


class NgsPassingStatsResponse(BaseModel):
    """Response from the NGS passing stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    filter: Optional[str] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsPassingStat]] = None


class NgsReceivingStatsResponse(BaseModel):
    """Response from the NGS receiving stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsReceivingStat]] = None


class NgsRushingStatsResponse(BaseModel):
    """Response from the NGS rushing stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    filter: Optional[str] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsRushingStat]] = None
