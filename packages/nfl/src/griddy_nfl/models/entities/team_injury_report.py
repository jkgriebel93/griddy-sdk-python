from __future__ import annotations

from datetime import datetime
from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel
from .injury_entry import InjuryEntry, InjuryEntryTypedDict
from .team import Team, TeamTypedDict


class TeamInjuryReportTypedDict(TypedDict):
    injuries: NotRequired[List[InjuryEntryTypedDict]]
    last_updated: NotRequired[datetime]
    team: NotRequired[TeamTypedDict]


class TeamInjuryReport(BaseModel):
    injuries: Optional[List[InjuryEntry]] = None

    last_updated: Annotated[Optional[datetime], pydantic.Field(alias="lastUpdated")] = (
        None
    )

    team: Optional[Team] = None
