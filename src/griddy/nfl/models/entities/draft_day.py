import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.types import BaseModel


class DraftDayTypedDict(TypedDict):
    year: int
    day: int
    first_pick: int
    last_pick: int


class DraftDay(BaseModel):
    year: int
    day: int
    first_pick: Annotated[int, pydantic.Field(alias="firstPick")]
    last_pick: Annotated[int, pydantic.Field(alias="lastPick")]
