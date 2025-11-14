from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetMultipleRankingsAllTeamsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    stat0: str
    r"""First statistical category"""
    stat1: NotRequired[str]
    r"""Second statistical category"""
    stat2: NotRequired[str]
    r"""Third statistical category"""
    stat3: NotRequired[str]
    r"""Fourth statistical category"""
    stat4: NotRequired[str]
    r"""Fifth statistical category"""


class GetMultipleRankingsAllTeamsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""

    stat0: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""First statistical category"""

    stat1: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Second statistical category"""

    stat2: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Third statistical category"""

    stat3: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Fourth statistical category"""

    stat4: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Fifth statistical category"""
