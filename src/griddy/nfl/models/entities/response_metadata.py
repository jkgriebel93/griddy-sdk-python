from __future__ import annotations

from datetime import datetime

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class ResponseMetadata(BaseModel):
    generated_at: Annotated[datetime, pydantic.Field(alias="generatedAt")]
    r"""Response generation timestamp"""
