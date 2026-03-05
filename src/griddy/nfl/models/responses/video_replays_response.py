from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.weekly_game_detail import (
    Replay,
)
from griddy.nfl.types import BaseModel


class VideoReplaysMetadata(BaseModel):
    generated_at: Annotated[Optional[str], pydantic.Field(alias="generatedAt")] = None


class VideoReplaysPagination(BaseModel):
    token: Optional[str] = None


class VideoReplaysResponse(BaseModel):
    r"""Video replays for a game.

    Each item in the items array is a Replay object (same type used
    by WeeklyGameDetail.replays).
    """

    items: Optional[List[Replay]] = None

    metadata: Optional[VideoReplaysMetadata] = None

    pagination: Optional[VideoReplaysPagination] = None
