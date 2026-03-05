from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .team import Team


class TeamGameStats(BaseModel):
    first_downs: Annotated[Optional[int], pydantic.Field(alias="firstDowns")] = None

    fourth_down_conversions: Annotated[
        Optional[str], pydantic.Field(alias="fourthDownConversions")
    ] = None

    passing_yards: Annotated[Optional[int], pydantic.Field(alias="passingYards")] = None

    penalties: Optional[int] = None

    penalty_yards: Annotated[Optional[int], pydantic.Field(alias="penaltyYards")] = None

    rushing_yards: Annotated[Optional[int], pydantic.Field(alias="rushingYards")] = None

    score: Optional[int] = None

    team: Optional[Team] = None

    third_down_conversions: Annotated[
        Optional[str], pydantic.Field(alias="thirdDownConversions")
    ] = None

    time_of_possession: Annotated[
        Optional[str], pydantic.Field(alias="timeOfPossession")
    ] = None

    total_yards: Annotated[Optional[int], pydantic.Field(alias="totalYards")] = None

    turnovers: Optional[int] = None
