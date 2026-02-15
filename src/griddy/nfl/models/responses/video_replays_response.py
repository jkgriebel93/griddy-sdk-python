from __future__ import annotations

from typing import Any, Dict, List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.types import BaseModel


class VideoReplaysResponseTypedDict(TypedDict):
    items: NotRequired[Optional[List[Dict[str, Any]]]]


class VideoReplaysResponse(BaseModel):
    r"""Video replays for a game.

    Each item in the items array is a video/replay object with 50+ fields
    including type, description, duration, authorizations, thumbnail, etc.
    """

    items: Optional[List[Dict[str, Any]]] = None
