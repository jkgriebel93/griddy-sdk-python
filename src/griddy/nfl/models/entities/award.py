from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel

AwardType = Literal[
    "MVP",
    "OPOY",
    "DPOY",
    "OROY",
    "DROY",
    "PRO_BOWL",
    "ALL_PRO",
    "SUPER_BOWL_MVP",
]


class AwardTypedDict(TypedDict):
    award_type: NotRequired[AwardType]
    description: NotRequired[str]
    year: NotRequired[int]


class Award(BaseModel):
    award_type: Annotated[Optional[AwardType], pydantic.Field(alias="awardType")] = None

    description: Optional[str] = None

    year: Optional[int] = None
