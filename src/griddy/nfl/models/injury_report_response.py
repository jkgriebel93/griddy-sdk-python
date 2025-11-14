from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .team_injury_report import TeamInjuryReport, TeamInjuryReportTypedDict


class InjuryReportResponseTypedDict(TypedDict):
    reports: NotRequired[List[TeamInjuryReportTypedDict]]
    season: NotRequired[int]
    week: NotRequired[int]


class InjuryReportResponse(BaseModel):
    reports: Optional[List[TeamInjuryReport]] = None

    season: Optional[int] = None

    week: Optional[int] = None
