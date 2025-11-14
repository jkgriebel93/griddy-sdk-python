from __future__ import annotations

from typing import Literal

import pydantic
from typing_extensions import Annotated, TypedDict

from ..types import BaseModel

RefreshTokenRequestNetworkType = Literal[
    "other",
    "wifi",
    "cellular",
    "ethernet",
]
r"""Type of network connection"""


class RefreshTokenRequestTypedDict(TypedDict):
    client_key: str
    r"""Client application identifier key"""
    client_secret: str
    r"""Client application secret for authentication"""
    device_id: str
    r"""Unique device identifier (UUID format)"""
    device_info: str
    r"""Base64-encoded JSON containing device information such as:
    {\"model\":\"desktop\",\"version\":\"Chrome\",\"osName\":\"Windows\",\"osVersion\":\"10\"}

    """
    network_type: RefreshTokenRequestNetworkType
    r"""Type of network connection"""
    refresh_token: str
    r"""Valid refresh token from previous authentication"""
    signature_timestamp: str
    r"""Unix timestamp for signature verification"""
    uid: str
    r"""User identifier hash"""
    uid_signature: str
    r"""HMAC signature for request verification"""


class RefreshTokenRequest(BaseModel):
    client_key: Annotated[str, pydantic.Field(alias="clientKey")]
    r"""Client application identifier key"""

    client_secret: Annotated[str, pydantic.Field(alias="clientSecret")]
    r"""Client application secret for authentication"""

    device_id: Annotated[str, pydantic.Field(alias="deviceId")]
    r"""Unique device identifier (UUID format)"""

    device_info: Annotated[str, pydantic.Field(alias="deviceInfo")]
    r"""Base64-encoded JSON containing device information such as:
    {\"model\":\"desktop\",\"version\":\"Chrome\",\"osName\":\"Windows\",\"osVersion\":\"10\"}

    """

    network_type: Annotated[
        RefreshTokenRequestNetworkType, pydantic.Field(alias="networkType")
    ]
    r"""Type of network connection"""

    refresh_token: Annotated[str, pydantic.Field(alias="refreshToken")]
    r"""Valid refresh token from previous authentication"""

    signature_timestamp: Annotated[str, pydantic.Field(alias="signatureTimestamp")]
    r"""Unix timestamp for signature verification"""

    uid: str
    r"""User identifier hash"""

    uid_signature: Annotated[str, pydantic.Field(alias="uidSignature")]
    r"""HMAC signature for request verification"""
