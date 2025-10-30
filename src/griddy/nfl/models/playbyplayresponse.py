from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .drive import Drive, DriveTypedDict
from .play import Play, PlayTypedDict
from .progame import ProGame, ProGameTypedDict
from .scoringplay import ScoringPlay, ScoringPlayTypedDict


class PlayByPlayResponseTypedDict(TypedDict):
    current_drive: NotRequired[DriveTypedDict]
    drives: NotRequired[List[DriveTypedDict]]
    game: NotRequired[ProGameTypedDict]
    last_play: NotRequired[PlayTypedDict]
    scoring_summary: NotRequired[List[ScoringPlayTypedDict]]


class PlayByPlayResponse(BaseModel):
    current_drive: Annotated[Optional[Drive], pydantic.Field(alias="currentDrive")] = (
        None
    )

    drives: Optional[List[Drive]] = None

    game: Optional[ProGame] = None

    last_play: Annotated[Optional[Play], pydantic.Field(alias="lastPlay")] = None

    scoring_summary: Annotated[
        Optional[List[ScoringPlay]], pydantic.Field(alias="scoringSummary")
    ] = None
