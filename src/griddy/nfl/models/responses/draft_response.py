from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.draft_day import DraftDay
from griddy.nfl.models.entities.draft_pick import DraftPick
from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.types import BaseModel


class DraftResponse(BaseModel):
    year: int
    current_day: Annotated[int, pydantic.Field(alias="currentDay")]
    current_overall: Annotated[int, pydantic.Field(alias="currentOverall")]
    current_pick: Annotated[int, pydantic.Field(alias="currentPick")]
    current_round: Annotated[int, pydantic.Field(alias="currentRound")]
    draft_state: Annotated[str, pydantic.Field(alias="draftState")]
    team_on_the_clock: Annotated[str, pydantic.Field(alias="teamOnTheClock")]
    days: List[DraftDay]
    picks: List[DraftPick]
    pagination: Pagination
