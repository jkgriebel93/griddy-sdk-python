from __future__ import annotations
from ..types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class PlayerWeekProjectedPointsAttributesTypedDict(TypedDict):
    player_id: str
    r"""Player SMART ID"""
    season: int
    r"""Season year"""
    settings_code: str
    r"""Fantasy settings code"""
    week: int
    r"""Week number"""
    points: NotRequired[Nullable[float]]
    r"""Projected fantasy points"""


class PlayerWeekProjectedPointsAttributes(BaseModel):
    player_id: Annotated[str, pydantic.Field(alias="playerId")]
    r"""Player SMART ID"""

    season: int
    r"""Season year"""

    settings_code: Annotated[str, pydantic.Field(alias="settingsCode")]
    r"""Fantasy settings code"""

    week: int
    r"""Week number"""

    points: OptionalNullable[float] = UNSET
    r"""Projected fantasy points"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["points"]
        nullable_fields = ["points"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


PlayerWeekProjectedPointsType = Literal["player-week-projected-points",]


class PlayerWeekProjectedPointsTypedDict(TypedDict):
    attributes: PlayerWeekProjectedPointsAttributesTypedDict
    id: str
    r"""Unique identifier for this projection"""
    type: PlayerWeekProjectedPointsType


class PlayerWeekProjectedPoints(BaseModel):
    attributes: PlayerWeekProjectedPointsAttributes

    id: str
    r"""Unique identifier for this projection"""

    type: PlayerWeekProjectedPointsType
