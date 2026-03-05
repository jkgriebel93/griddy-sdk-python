from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class VideoThumbnail(BaseModel):
    thumbnail_url: Annotated[str, pydantic.Field(alias="thumbnailUrl")]
    r"""Video thumbnail image URL"""
