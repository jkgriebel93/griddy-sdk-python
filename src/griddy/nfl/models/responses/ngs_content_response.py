"""Response models for NGS content endpoints (charts, players, highlights)."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.ngs_content import (
    NgsChart,
    NgsChartPlayer,
    NgsHighlight,
)
from griddy.nfl.types import BaseModel


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


class NgsChartPlayersResponse(BaseModel):
    """Response from the NGS chart players endpoint."""

    players: Optional[List[NgsChartPlayer]] = None


class NgsHighlightsResponse(BaseModel):
    """Response from the NGS highlights endpoint."""

    season: Optional[int] = None
    highlights: Optional[List[NgsHighlight]] = None
    total: Optional[int] = None
    count: Optional[int] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
