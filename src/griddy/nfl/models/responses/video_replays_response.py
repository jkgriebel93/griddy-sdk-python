from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.entities.weekly_game_detail import (
    Replay,
    ReplayTypedDict,
)
from griddy.nfl.types import BaseModel


class VideoReplaysMetadataTypedDict(TypedDict):
    generated_at: NotRequired[Optional[str]]


class VideoReplaysMetadata(BaseModel):
    generated_at: Annotated[Optional[str], pydantic.Field(alias="generatedAt")] = None


class VideoReplaysPaginationTypedDict(TypedDict):
    token: NotRequired[Optional[str]]


class VideoReplaysPagination(BaseModel):
    token: Optional[str] = None


class VideoReplaysResponseTypedDict(TypedDict):
    items: NotRequired[Optional[List[ReplayTypedDict]]]
    metadata: NotRequired[Optional[VideoReplaysMetadataTypedDict]]
    pagination: NotRequired[Optional[VideoReplaysPaginationTypedDict]]


class VideoReplaysResponse(BaseModel):
    r"""Video replays for a game.

    Each item in the items array is a Replay object (same type used
    by WeeklyGameDetail.replays).
    """

    items: Optional[List[Replay]] = None

    metadata: Optional[VideoReplaysMetadata] = None

    pagination: Optional[VideoReplaysPagination] = None
