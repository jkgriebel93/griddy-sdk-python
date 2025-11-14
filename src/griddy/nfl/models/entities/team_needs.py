from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.models.enums.position_enums import TeamNeedsPositionEnum
from griddy.nfl.types import BaseModel


class TeamNeedsTypedDict(TypedDict):
    team_id: str
    r"""Team's UUID as defined by the NFL"""
    year: int
    r"""The year for which these team needs are relevant"""
    analysis: str
    r"""A couple sentence blurb providing justification for the listed needs."""
    position_needs: List[TeamNeedsPositionEnum]
    r"""List of positions the team needs to address in the draft"""


class TeamNeeds(BaseModel):
    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team's UUID as defined by the NFL"""
    year: int
    r"""The year for which these team needs are relevant"""
    analysis: str
    r"""A couple sentence blurb providing justification for the listed needs."""
    position_needs: Annotated[
        List[TeamNeedsPositionEnum], pydantic.Field(alias="positionNeeds")
    ]
    r"""List of positions the team needs to address in the draft"""
