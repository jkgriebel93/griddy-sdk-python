from typing import List

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.combine_profile import (
    CombineProfile,
)
from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.types import BaseModel


class CombineProfilesResponse(BaseModel):
    combine_profiles: Annotated[
        List[CombineProfile], pydantic.Field(alias="combineProfiles")
    ]
    r"""List of CombineProfile objects"""
    pagination: Pagination
    r"""Pagination information object"""
