from __future__ import annotations
from .seasontypeenum import SeasonTypeEnum
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWeeklyGameDetailsRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    type: SeasonTypeEnum
    r"""Season type"""
    week: int
    r"""Week number"""
    include_drive_chart: NotRequired[bool]
    r"""Include drive chart data"""
    include_replays: NotRequired[bool]
    r"""Include replay videos"""
    include_standings: NotRequired[bool]
    r"""Include team standings"""
    include_tagged_videos: NotRequired[bool]
    r"""Include tagged video content"""


class GetWeeklyGameDetailsRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    type: Annotated[
        SeasonTypeEnum,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Season type"""

    week: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Week number"""

    include_drive_chart: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeDriveChart"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include drive chart data"""

    include_replays: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeReplays"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include replay videos"""

    include_standings: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeStandings"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include team standings"""

    include_tagged_videos: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeTaggedVideos"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include tagged video content"""
