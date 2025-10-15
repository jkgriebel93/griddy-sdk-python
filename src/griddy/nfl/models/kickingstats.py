from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class KickingStatsTypedDict(TypedDict):
    extra_points_attempted: NotRequired[int]
    extra_points_made: NotRequired[int]
    field_goal_pct: NotRequired[float]
    field_goals_attempted: NotRequired[int]
    field_goals_made: NotRequired[int]
    long_field_goal: NotRequired[int]
    points: NotRequired[int]


class KickingStats(BaseModel):
    extra_points_attempted: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsAttempted")
    ] = None

    extra_points_made: Annotated[
        Optional[int], pydantic.Field(alias="extraPointsMade")
    ] = None

    field_goal_pct: Annotated[Optional[float], pydantic.Field(alias="fieldGoalPct")] = (
        None
    )

    field_goals_attempted: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsAttempted")
    ] = None

    field_goals_made: Annotated[
        Optional[int], pydantic.Field(alias="fieldGoalsMade")
    ] = None

    long_field_goal: Annotated[Optional[int], pydantic.Field(alias="longFieldGoal")] = (
        None
    )

    points: Optional[int] = None
