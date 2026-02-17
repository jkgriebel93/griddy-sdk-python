"""Response models for NGS leaders endpoints."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.ngs_leaders import (
    NgsCompletionLeaderEntry,
    NgsCompletionLeaderEntryTypedDict,
    NgsDistanceLeaderEntry,
    NgsDistanceLeaderEntryTypedDict,
    NgsERYLeaderEntry,
    NgsERYLeaderEntryTypedDict,
    NgsSackLeaderEntry,
    NgsSackLeaderEntryTypedDict,
    NgsSpeedLeaderEntry,
    NgsSpeedLeaderEntryTypedDict,
    NgsTackleLeaderEntry,
    NgsTackleLeaderEntryTypedDict,
    NgsYACLeaderEntry,
    NgsYACLeaderEntryTypedDict,
)
from griddy_nfl.types import BaseModel


class NgsSpeedLeadersResponseTypedDict(TypedDict):
    """Response from the NGS fastest ball carriers endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    leaders: NotRequired[List[NgsSpeedLeaderEntryTypedDict]]


class NgsSpeedLeadersResponse(BaseModel):
    """Response from the NGS fastest ball carriers endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsSpeedLeaderEntry]] = None


class NgsSackLeadersResponseTypedDict(TypedDict):
    """Response from the NGS fastest sacks endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    league_average: NotRequired[float]
    leaders: NotRequired[List[NgsSackLeaderEntryTypedDict]]


class NgsSackLeadersResponse(BaseModel):
    """Response from the NGS fastest sacks endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    league_average: Annotated[
        Optional[float], pydantic.Field(alias="leagueAverage")
    ] = None
    leaders: Optional[List[NgsSackLeaderEntry]] = None


class NgsCompletionLeadersResponseTypedDict(TypedDict):
    """Response from the NGS improbable completions endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    completion_leaders: NotRequired[List[NgsCompletionLeaderEntryTypedDict]]


class NgsCompletionLeadersResponse(BaseModel):
    """Response from the NGS improbable completions endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    completion_leaders: Annotated[
        Optional[List[NgsCompletionLeaderEntry]],
        pydantic.Field(alias="completionLeaders"),
    ] = None


class NgsYACLeadersResponseTypedDict(TypedDict):
    """Response from the NGS incredible YAC endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    yac_leaders: NotRequired[List[NgsYACLeaderEntryTypedDict]]


class NgsYACLeadersResponse(BaseModel):
    """Response from the NGS incredible YAC endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    yac_leaders: Annotated[
        Optional[List[NgsYACLeaderEntry]], pydantic.Field(alias="yacLeaders")
    ] = None


class NgsDistanceLeadersResponseTypedDict(TypedDict):
    """Response from the NGS longest plays endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    leaders: NotRequired[List[NgsDistanceLeaderEntryTypedDict]]


class NgsDistanceLeadersResponse(BaseModel):
    """Response from the NGS longest plays endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsDistanceLeaderEntry]] = None


class NgsTackleLeadersResponseTypedDict(TypedDict):
    """Response from the NGS longest tackles endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    leaders: NotRequired[List[NgsTackleLeaderEntryTypedDict]]


class NgsTackleLeadersResponse(BaseModel):
    """Response from the NGS longest tackles endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    leaders: Optional[List[NgsTackleLeaderEntry]] = None


class NgsERYLeadersResponseTypedDict(TypedDict):
    """Response from the NGS remarkable rushes endpoint."""

    season: NotRequired[int]
    season_type: NotRequired[str]
    ery_leaders: NotRequired[List[NgsERYLeaderEntryTypedDict]]


class NgsERYLeadersResponse(BaseModel):
    """Response from the NGS remarkable rushes endpoint."""

    season: Optional[int] = None
    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None
    ery_leaders: Annotated[
        Optional[List[NgsERYLeaderEntry]], pydantic.Field(alias="eryLeaders")
    ] = None
