from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class InternationalWatchOption(BaseModel):
    broadcasters: Optional[List[str]] = None

    country_code: Annotated[Optional[str], pydantic.Field(alias="countryCode")] = None


class StreamingNetwork(BaseModel):
    host_network: Annotated[Optional[str], pydantic.Field(alias="hostNetwork")] = None
    r"""Primary streaming network"""

    networks: Optional[List[str]] = None
    r"""Available streaming networks"""


Territory = Literal[
    "NATIONAL",
    "REGIONAL",
]
r"""Broadcast territory scope"""


class BroadcastInfo(BaseModel):
    away_network_channels: Annotated[
        Optional[List[str]], pydantic.Field(alias="awayNetworkChannels")
    ] = None
    r"""Networks broadcasting in away market"""

    home_network_channels: Annotated[
        Optional[List[str]], pydantic.Field(alias="homeNetworkChannels")
    ] = None
    r"""Networks broadcasting in home market"""

    international_watch_options: Annotated[
        Optional[List[InternationalWatchOption]],
        pydantic.Field(alias="internationalWatchOptions"),
    ] = None
    r"""International viewing options"""

    streaming_networks: Annotated[
        Optional[List[StreamingNetwork]], pydantic.Field(alias="streamingNetworks")
    ] = None

    territory: Optional[Territory] = None
    r"""Broadcast territory scope"""
