from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.combine_profile import (
    CombineProfile,
    CombineProfileTypedDict,
)
from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.types import BaseModel


class CombineRankingsResponseTypedDict(TypedDict):
    combine_profiles: List[CombineProfileTypedDict]
    r"""List of combine profiles"""
    pagination: PaginationTypedDict
    r"""Pagination information"""


class CombineRankingsResponse(BaseModel):
    combine_profiles: Annotated[
        List[CombineProfile], pydantic.Field(alias="combineProfiles")
    ]
    r"""List of CombineProfile objects"""
    pagination: Pagination
    r"""Pagination information object"""
