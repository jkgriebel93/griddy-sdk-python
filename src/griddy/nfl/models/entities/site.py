from __future__ import annotations

from typing import Literal, Optional

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable

SiteRoofType = Literal[
    "OUTDOOR",
    "INDOOR",
    "RETRACTABLE",
]


class SiteTypedDict(TypedDict):
    postal_code: NotRequired[Nullable[str]]
    roof_type: NotRequired[SiteRoofType]
    site_city: NotRequired[str]
    site_full_name: NotRequired[str]
    site_id: NotRequired[int]
    site_state: NotRequired[Nullable[str]]
    smart_id: NotRequired[str]


class Site(BaseModel):
    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET

    roof_type: Annotated[Optional[SiteRoofType], pydantic.Field(alias="roofType")] = (
        None
    )

    site_city: Annotated[Optional[str], pydantic.Field(alias="siteCity")] = None

    site_full_name: Annotated[Optional[str], pydantic.Field(alias="siteFullName")] = (
        None
    )

    site_id: Annotated[Optional[int], pydantic.Field(alias="siteId")] = None

    site_state: Annotated[OptionalNullable[str], pydantic.Field(alias="siteState")] = (
        UNSET
    )

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "postalCode",
            "roofType",
            "siteCity",
            "siteFullName",
            "siteId",
            "siteState",
            "smartId",
        ]
        nullable_fields = ["postalCode", "siteState"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(n)  # FIX: Use field name, not alias
            serialized.pop(n, None)

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
