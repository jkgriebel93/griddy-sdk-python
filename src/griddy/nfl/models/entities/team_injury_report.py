from __future__ import annotations

from datetime import datetime
from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .injury_entry import InjuryEntry
from .team import Team


class TeamInjuryReport(BaseModel):
    injuries: Optional[List[InjuryEntry]] = None

    last_updated: Annotated[Optional[datetime], pydantic.Field(alias="lastUpdated")] = (
        None
    )

    team: Optional[Team] = None
