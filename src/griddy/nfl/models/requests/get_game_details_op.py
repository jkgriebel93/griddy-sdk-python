from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


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
