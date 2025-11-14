from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.drive import Drive, DriveTypedDict
from griddy.nfl.models.play import Play, PlayTypedDict
from griddy.nfl.models.pro_game import ProGame, ProGameTypedDict
from griddy.nfl.models.scoring_play import ScoringPlay, ScoringPlayTypedDict
from griddy.nfl.types import BaseModel


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
