from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class RecordTypedDict(TypedDict):
    losses: NotRequired[int]
    ties: NotRequired[int]
    wins: NotRequired[int]


class Record(BaseModel):
    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None
