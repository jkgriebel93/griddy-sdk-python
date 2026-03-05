from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .play import Play
from .team import Team

Result = Literal[
    "TOUCHDOWN",
    "FIELD_GOAL",
    "PUNT",
    "DOWNS",
    "FUMBLE",
    "INTERCEPTION",
    "SAFETY",
    "END_OF_HALF",
    "END_OF_GAME",
]


class Drive(BaseModel):
    drive_number: Annotated[Optional[int], pydantic.Field(alias="driveNumber")] = None

    end_time: Annotated[Optional[str], pydantic.Field(alias="endTime")] = None
    r"""Game clock at drive end"""

    end_yard_line: Annotated[Optional[str], pydantic.Field(alias="endYardLine")] = None
    r"""Ending field position"""

    plays: Optional[List[Play]] = None

    quarter: Optional[int] = None

    result: Optional[Result] = None

    start_time: Annotated[Optional[str], pydantic.Field(alias="startTime")] = None
    r"""Game clock at drive start"""

    start_yard_line: Annotated[Optional[str], pydantic.Field(alias="startYardLine")] = (
        None
    )
    r"""Starting field position"""

    team: Optional[Team] = None

    time_of_possession: Annotated[
        Optional[str], pydantic.Field(alias="timeOfPossession")
    ] = None
    r"""Drive duration (MM:SS)"""

    total_plays: Annotated[Optional[int], pydantic.Field(alias="totalPlays")] = None

    total_yards: Annotated[Optional[int], pydantic.Field(alias="totalYards")] = None
