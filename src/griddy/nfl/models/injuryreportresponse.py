from __future__ import annotations
from .teaminjuryreport import TeamInjuryReport, TeamInjuryReportTypedDict
from ..types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InjuryReportResponseTypedDict(TypedDict):
    reports: NotRequired[List[TeamInjuryReportTypedDict]]
    season: NotRequired[int]
    week: NotRequired[int]


class InjuryReportResponse(BaseModel):
    reports: Optional[List[TeamInjuryReport]] = None

    season: Optional[int] = None

    week: Optional[int] = None
