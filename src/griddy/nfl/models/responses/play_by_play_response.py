from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.drive import Drive
from griddy.nfl.models.entities.play import Play
from griddy.nfl.models.entities.pro_game import ProGame
from griddy.nfl.models.entities.scoring_play import ScoringPlay
from griddy.nfl.types import BaseModel


class PlayByPlayResponse(BaseModel):
    """Response containing play-by-play data."""

    current_drive: Annotated[Optional[Drive], pydantic.Field(alias="currentDrive")] = (
        None
    )

    drives: Optional[List[Drive]] = None

    game: Optional[ProGame] = None

    last_play: Annotated[Optional[Play], pydantic.Field(alias="lastPlay")] = None

    scoring_summary: Annotated[
        Optional[List[ScoringPlay]], pydantic.Field(alias="scoringSummary")
    ] = None
