
from __future__ import annotations
from ..types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PaginationTypedDict(TypedDict):
    limit: NotRequired[int]
    r"""Maximum items per page"""
    token: NotRequired[Nullable[str]]
    r"""Token for next page of results"""


class Pagination(BaseModel):
    limit: Optional[int] = None
    r"""Maximum items per page"""

    token: OptionalNullable[str] = UNSET
    r"""Token for next page of results"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["limit", "token"]
        nullable_fields = ["token"]
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
