from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetGameDetailsRequestTypedDict(TypedDict):
    game_id: str
    r"""Game identifier (UUID)"""
    include_drive_chart: NotRequired[bool]
    r"""Include drive chart data in response"""
    include_replays: NotRequired[bool]
    r"""Include replay videos in response"""
    include_standings: NotRequired[bool]
    r"""Include standings data in response"""
    include_tagged_videos: NotRequired[bool]
    r"""Include tagged videos in response"""
    include_summary: NotRequired[bool]
    r"""Include summary information in response"""


class GetGameDetailsRequest(BaseModel):
    game_id: Annotated[
        str,
        pydantic.Field(alias="gameId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Game identifier (UUID)"""

    include_drive_chart: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeDriveChart"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include drive chart data in response"""

    include_replays: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeReplays"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include replay videos in response"""

    include_standings: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeStandings"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include standings data in response"""

    include_tagged_videos: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeTaggedVideos"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include tagged videos in response"""

    include_summary: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeSummary"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include summary information in response"""
