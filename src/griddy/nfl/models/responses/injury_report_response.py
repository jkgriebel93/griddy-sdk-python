from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.team_injury_report import TeamInjuryReport
from griddy.nfl.types import BaseModel


class InjuryReportResponse(BaseModel):
    reports: Optional[List[TeamInjuryReport]] = None

    season: Optional[int] = None

    week: Optional[int] = None
