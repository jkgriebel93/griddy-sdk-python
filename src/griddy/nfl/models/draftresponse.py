from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .draftpick import DraftPick, DraftPickTypedDict


class RoundTypedDict(TypedDict):
    picks: NotRequired[List[DraftPickTypedDict]]
    round: NotRequired[int]


class Round(BaseModel):
    picks: Optional[List[DraftPick]] = None

    round: Optional[int] = None


class DraftResponseTypedDict(TypedDict):
    rounds: NotRequired[List[RoundTypedDict]]
    year: NotRequired[int]


class DraftResponse(BaseModel):
    rounds: Optional[List[Round]] = None

    year: Optional[int] = None
