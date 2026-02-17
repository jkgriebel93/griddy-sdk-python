from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.draft_day import DraftDay, DraftDayTypedDict
from griddy_nfl.models.entities.draft_pick import DraftPick, DraftPickTypedDict
from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.types import BaseModel


class DraftResponseTypedDict(TypedDict):
    year: int
    current_day: int
    current_overall: int
    current_pick: int
    current_round: int
    draft_state: str
    team_on_the_clock: str
    days: List[DraftDayTypedDict]
    picks: List[DraftPickTypedDict]
    pagination: PaginationTypedDict


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
