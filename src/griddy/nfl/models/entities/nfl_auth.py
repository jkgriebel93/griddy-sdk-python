from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel


class NFLAuth(BaseModel):
    access_token: Annotated[str, pydantic.Field(alias="accessToken")]
    r"""Bearer token for NFL API requests."""
    refresh_token: Annotated[Optional[str], pydantic.Field(alias="refreshToken")] = None
    r"""Token used to obtain a new access token when the current one expires."""
    expires_in: Annotated[Optional[float], pydantic.Field(alias="expiresIn")] = None
    r"""Unix timestamp (seconds) when the access token expires."""
