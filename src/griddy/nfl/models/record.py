from __future__ import annotations
from ..types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordTypedDict(TypedDict):
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins: NotRequired[int]


class Record(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None
