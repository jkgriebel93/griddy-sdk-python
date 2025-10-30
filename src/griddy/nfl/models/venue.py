
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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VenueTypedDict(TypedDict):
    address: NotRequired[Nullable[str]]
    r"""Street address"""
    city: NotRequired[str]
    r"""City name"""
    country: NotRequired[str]
    r"""Country name"""
    id: NotRequired[str]
    r"""Unique venue identifier"""
    name: NotRequired[str]
    r"""Venue name"""
    postal_code: NotRequired[Nullable[str]]
    r"""Postal/ZIP code"""
    territory: NotRequired[Nullable[str]]
    r"""State or territory code"""


class Venue(BaseModel):
    address: OptionalNullable[str] = UNSET
    r"""Street address"""

    city: Optional[str] = None
    r"""City name"""

    country: Optional[str] = None
    r"""Country name"""

    id: Optional[str] = None
    r"""Unique venue identifier"""

    name: Optional[str] = None
    r"""Venue name"""

    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET
    r"""Postal/ZIP code"""

    territory: OptionalNullable[str] = UNSET
    r"""State or territory code"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "address",
            "city",
            "country",
            "id",
            "name",
            "postalCode",
            "territory",
        ]
        nullable_fields = ["address", "postalCode", "territory"]
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
