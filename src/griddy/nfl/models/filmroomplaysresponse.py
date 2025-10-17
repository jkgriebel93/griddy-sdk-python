from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from ..types import BaseModel
from .filmroomplay import FilmroomPlay, FilmroomPlayTypedDict


class FilmroomPlaysResponseTypedDict(TypedDict):
    count: int
    r"""Total number of plays matching the filter criteria"""
    plays: List[FilmroomPlayTypedDict]
    r"""Array of play data matching the filter criteria"""


class FilmroomPlaysResponse(BaseModel):
    count: int
    r"""Total number of plays matching the filter criteria"""

    plays: List[FilmroomPlay]
    r"""Array of play data matching the filter criteria"""
