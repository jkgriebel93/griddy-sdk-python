from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.team import Team, TeamTypedDict
from griddy.nfl.types import BaseModel


class ExperienceTeamsResponseTypedDict(TypedDict):
    teams: NotRequired[List[TeamTypedDict]]


class ExperienceTeamsResponse(BaseModel):
    teams: Optional[List[Team]] = None
