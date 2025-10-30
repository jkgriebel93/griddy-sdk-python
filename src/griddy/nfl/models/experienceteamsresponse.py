
from __future__ import annotations
from .team import Team, TeamTypedDict
from ..types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ExperienceTeamsResponseTypedDict(TypedDict):
    teams: NotRequired[List[TeamTypedDict]]


class ExperienceTeamsResponse(BaseModel):
    teams: Optional[List[Team]] = None
