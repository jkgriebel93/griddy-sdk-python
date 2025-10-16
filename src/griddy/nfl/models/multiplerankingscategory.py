from __future__ import annotations
from .teamrankingentry import TeamRankingEntry, TeamRankingEntryTypedDict
from ..types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MultipleRankingsCategoryPaginationTypedDict(TypedDict):
    limit: NotRequired[int]
    token: NotRequired[Nullable[str]]


class MultipleRankingsCategoryPagination(BaseModel):
    limit: Optional[int] = None

    token: OptionalNullable[str] = UNSET

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


class MultipleRankingsCategoryTypedDict(TypedDict):
    pagination: NotRequired[MultipleRankingsCategoryPaginationTypedDict]
    stat_category: NotRequired[str]
    r"""Category of statistic"""
    stat_name: NotRequired[str]
    r"""Name of specific statistic"""
    teams: NotRequired[List[TeamRankingEntryTypedDict]]


class MultipleRankingsCategory(BaseModel):
    pagination: Optional[MultipleRankingsCategoryPagination] = None

    stat_category: Annotated[Optional[str], pydantic.Field(alias="statCategory")] = None
    r"""Category of statistic"""

    stat_name: Annotated[Optional[str], pydantic.Field(alias="statName")] = None
    r"""Name of specific statistic"""

    teams: Optional[List[TeamRankingEntry]] = None
