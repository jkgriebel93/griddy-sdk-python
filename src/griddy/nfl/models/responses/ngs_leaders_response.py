"""Response models for NGS leaders endpoints."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.ngs_leaders import (
    NgsCompletionLeaderEntry,
    NgsDistanceLeaderEntry,
    NgsERYLeaderEntry,
    NgsSackLeaderEntry,
    NgsSpeedLeaderEntry,
    NgsTackleLeaderEntry,
    NgsYACLeaderEntry,
)
from griddy.nfl.types import BaseModel


class NgsSpeedLeadersResponse(BaseModel):
    """Response from the NGS fastest ball carriers endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsSpeedLeaderEntry]] = None


class NgsSackLeadersResponse(BaseModel):
    """Response from the NGS fastest sacks endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    league_average: Annotated[
        Optional[float], pydantic.Field(alias="leagueAverage")
    ] = None
    leaders: Optional[List[NgsSackLeaderEntry]] = None


class NgsCompletionLeadersResponse(BaseModel):
    """Response from the NGS improbable completions endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    completion_leaders: Annotated[
        Optional[List[NgsCompletionLeaderEntry]],
        pydantic.Field(alias="completionLeaders"),
    ] = None


class NgsYACLeadersResponse(BaseModel):
    """Response from the NGS incredible YAC endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    yac_leaders: Annotated[
        Optional[List[NgsYACLeaderEntry]], pydantic.Field(alias="yacLeaders")
    ] = None


class NgsDistanceLeadersResponse(BaseModel):
    """Response from the NGS longest plays endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsDistanceLeaderEntry]] = None


class NgsTackleLeadersResponse(BaseModel):
    """Response from the NGS longest tackles endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsTackleLeaderEntry]] = None


class NgsERYLeadersResponse(BaseModel):
    """Response from the NGS remarkable rushes endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    ery_leaders: Annotated[
        Optional[List[NgsERYLeaderEntry]], pydantic.Field(alias="eryLeaders")
    ] = None
