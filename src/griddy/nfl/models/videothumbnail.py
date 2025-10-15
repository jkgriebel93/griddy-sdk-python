from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class VideoThumbnailTypedDict(TypedDict):
    thumbnail_url: str
    r"""Video thumbnail image URL"""


class VideoThumbnail(BaseModel):
    thumbnail_url: Annotated[str, pydantic.Field(alias="thumbnailUrl")]
    r"""Video thumbnail image URL"""
