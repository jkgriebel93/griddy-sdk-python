from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel


class VideoThumbnailTypedDict(TypedDict):
    thumbnail_url: str
    r"""Video thumbnail image URL"""


class VideoThumbnail(BaseModel):
    thumbnail_url: Annotated[str, pydantic.Field(alias="thumbnailUrl")]
    r"""Video thumbnail image URL"""
