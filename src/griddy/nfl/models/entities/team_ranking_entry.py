from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class TeamRankingEntryTypedDict(TypedDict):
    rank: NotRequired[int]
    r"""Team's rank (1-32)"""
    stats: NotRequired[float]
    r"""Statistical value"""
    team_id: NotRequired[str]


class TeamRankingEntry(BaseModel):
    rank: Optional[int] = None
    r"""Team's rank (1-32)"""

    stats: Optional[float] = None
    r"""Statistical value"""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
