from __future__ import annotations
from .injuryentry import InjuryEntry, InjuryEntryTypedDict
from .team import Team, TeamTypedDict
from datetime import datetime
from ..types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


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
