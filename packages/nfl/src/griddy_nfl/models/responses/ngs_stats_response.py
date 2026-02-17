"""Response models for NGS stats endpoints (passing, receiving, rushing)."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.ngs_stats import (
    NgsPassingStat,
    NgsPassingStatTypedDict,
    NgsReceivingStat,
    NgsReceivingStatTypedDict,
    NgsRushingStat,
    NgsRushingStatTypedDict,
)
from griddy_nfl.types import BaseModel


class NgsPassingStatsResponseTypedDict(TypedDict):
    """Response from the NGS passing stats endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    filter: NotRequired[str]
    threshold: NotRequired[int]
    stats: NotRequired[List[NgsPassingStatTypedDict]]


class NgsPassingStatsResponse(BaseModel):
    """Response from the NGS passing stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    filter: Optional[str] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsPassingStat]] = None


class NgsReceivingStatsResponseTypedDict(TypedDict):
    """Response from the NGS receiving stats endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    threshold: NotRequired[int]
    stats: NotRequired[List[NgsReceivingStatTypedDict]]


class NgsReceivingStatsResponse(BaseModel):
    """Response from the NGS receiving stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsReceivingStat]] = None


class NgsRushingStatsResponseTypedDict(TypedDict):
    """Response from the NGS rushing stats endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    filter: NotRequired[str]
    threshold: NotRequired[int]
    stats: NotRequired[List[NgsRushingStatTypedDict]]


class NgsRushingStatsResponse(BaseModel):
    """Response from the NGS rushing stats endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    filter: Optional[str] = None
    threshold: Optional[int] = None
    stats: Optional[List[NgsRushingStat]] = None
