from __future__ import annotations

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel


class TokenResponseTypedDict(TypedDict):
    access_token: str
    r"""JWT access token containing user permissions, subscription plans, location data, and roles.
    Include this token in the Authorization header as \"Bearer {accessToken}\" for authenticated requests.

    """
    expires_in: int
    r"""Unix timestamp when the access token expires"""
    refresh_token: str
    r"""New refresh token for future token refresh requests"""


class TokenResponse(BaseModel):
    access_token: Annotated[str, pydantic.Field(alias="accessToken")]
    r"""JWT access token containing user permissions, subscription plans, location data, and roles.
    Include this token in the Authorization header as \"Bearer {accessToken}\" for authenticated requests.

    """

    expires_in: Annotated[int, pydantic.Field(alias="expiresIn")]
    r"""Unix timestamp when the access token expires"""

    refresh_token: Annotated[str, pydantic.Field(alias="refreshToken")]
    r"""New refresh token for future token refresh requests"""
