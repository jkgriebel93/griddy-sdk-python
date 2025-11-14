from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.combine_profile import CombineProfile, CombineProfileTypedDict
from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.types import BaseModel


class CombineProfilesResponseTypedDict(TypedDict):
    combine_profiles: List[CombineProfileTypedDict]
    r"""List of combine profiles"""
    pagination: PaginationTypedDict
    r"""Pagination information"""


class CombineProfilesResponse(BaseModel):
    combine_profiles: Annotated[
        List[CombineProfile], pydantic.Field(alias="combineProfiles")
    ]
    r"""List of CombineProfile objects"""
    pagination: Pagination
    r"""Pagination information object"""
