from __future__ import annotations

from datetime import datetime

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel


class ResponseMetadataTypedDict(TypedDict):
    generated_at: datetime
    r"""Response generation timestamp"""


class ResponseMetadata(BaseModel):
    generated_at: Annotated[datetime, pydantic.Field(alias="generatedAt")]
    r"""Response generation timestamp"""
