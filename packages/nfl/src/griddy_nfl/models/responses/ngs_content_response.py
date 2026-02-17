"""Response models for NGS content endpoints (charts, players, highlights)."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.ngs_content import (
    NgsChart,
    NgsChartPlayer,
    NgsChartPlayerTypedDict,
    NgsChartTypedDict,
    NgsHighlight,
    NgsHighlightTypedDict,
)
from griddy_nfl.types import BaseModel


class NgsChartsResponseTypedDict(TypedDict):
    """Response from the NGS charts endpoint."""

    charts: NotRequired[List[NgsChartTypedDict]]
    count: NotRequired[int]
    offset: NotRequired[int]
    total: NotRequired[int]
    season: NotRequired[str]
    team_id: NotRequired[str]
    type: NotRequired[str]
    week: NotRequired[str]
    season_type: NotRequired[str]


class NgsChartsResponse(BaseModel):
    """Response from the NGS charts endpoint."""

    charts: Optional[List[NgsChart]] = None
    count: Optional[int] = None
    offset: Optional[int] = None
    total: Optional[int] = None
    season: Optional[str] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    type: Optional[str] = None
    week: Optional[str] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None


class NgsChartPlayersResponseTypedDict(TypedDict):
    """Response from the NGS chart players endpoint."""

    players: NotRequired[List[NgsChartPlayerTypedDict]]


class NgsChartPlayersResponse(BaseModel):
    """Response from the NGS chart players endpoint."""

    players: Optional[List[NgsChartPlayer]] = None


class NgsHighlightsResponseTypedDict(TypedDict):
    """Response from the NGS highlights endpoint."""

    season: NotRequired[int]
    highlights: NotRequired[List[NgsHighlightTypedDict]]
    total: NotRequired[int]
    count: NotRequired[int]
    offset: NotRequired[int]
    limit: NotRequired[int]


class NgsHighlightsResponse(BaseModel):
    """Response from the NGS highlights endpoint."""

    season: Optional[int] = None
    highlights: Optional[List[NgsHighlight]] = None
    total: Optional[int] = None
    count: Optional[int] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
