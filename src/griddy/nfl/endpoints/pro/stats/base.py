"""Base class for player stats endpoints."""

from typing import Type

from griddy.core._constants import STATS_ERROR_CODES
from griddy.nfl.basesdk import EndpointConfig
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET


class PlayerStatsBase(ProSDK):
    """Base class for player stats endpoints.

    Provides ``_make_stats_config`` to build ``EndpointConfig`` instances for
    GET-based stats endpoints, centralising the boilerplate that every player
    stats file otherwise repeats.
    """

    def _make_stats_config(
        self,
        path: str,
        operation_id: str,
        request_type: Type,
        response_type: Type,
        **kwargs,
    ) -> EndpointConfig:
        """Build an EndpointConfig for a stats endpoint.

        Positional args define the endpoint identity.  Keyword args are split:
        ``server_url``, ``timeout_ms``, ``http_headers``, and ``retries`` are
        forwarded to :class:`EndpointConfig`; everything else is passed to
        *request_type()* to construct the request model.
        """
        server_url = kwargs.pop("server_url", None)
        timeout_ms = kwargs.pop("timeout_ms", None)
        http_headers = kwargs.pop("http_headers", None)
        retries = kwargs.pop("retries", UNSET)
        return EndpointConfig(
            method="GET",
            path=path,
            operation_id=operation_id,
            request=request_type(**kwargs),
            response_type=response_type,
            error_status_codes=STATS_ERROR_CODES,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            return_raw_json=False,
        )
