from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .team import Team, TeamTypedDict


class ExperienceTeamsResponseTypedDict(TypedDict):
    teams: NotRequired[List[TeamTypedDict]]


class ExperienceTeamsResponse(BaseModel):
    teams: Optional[List[Team]] = None
