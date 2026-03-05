from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.boxscore_schedule import (
    BoxscoreSchedule,
)
from griddy.nfl.models.entities.team_boxscore import TeamBoxscore
from griddy.nfl.types import BaseModel
from griddy.nfl.utils.unmarshal_json_response import int_to_str


class BoxscoreResponse(BaseModel):
    away: Optional[TeamBoxscore] = None

    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None
    r"""Game identifier"""

    home: Optional[TeamBoxscore] = None

    schedule: Optional[BoxscoreSchedule] = None
