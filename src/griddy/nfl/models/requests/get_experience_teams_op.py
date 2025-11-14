from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetExperienceTeamsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    allteams: NotRequired[bool]
    r"""Include all teams including special teams"""


class GetExperienceTeamsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    allteams: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include all teams including special teams"""
