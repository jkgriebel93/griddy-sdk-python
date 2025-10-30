
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Literal
from typing_extensions import Annotated, TypedDict


TokenRequestNetworkType = Literal[
    "other",
    "wifi",
    "cellular",
    "ethernet",
]
r"""Type of network connection"""


class TokenRequestTypedDict(TypedDict):
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
    network_type: TokenRequestNetworkType
    r"""Type of network connection"""


class TokenRequest(BaseModel):
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
        TokenRequestNetworkType, pydantic.Field(alias="networkType")
    ]
    r"""Type of network connection"""
