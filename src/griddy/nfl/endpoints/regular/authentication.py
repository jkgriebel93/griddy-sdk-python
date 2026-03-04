from typing import Mapping, Optional

from griddy.core._constants import COLLECTION_ERROR_CODES, STATS_ERROR_CODES
from griddy.core.decorators import sdk_endpoints
from griddy.nfl import models, utils
from griddy.nfl.basesdk import BaseSDK, EndpointConfig
from griddy.nfl.types import UNSET, OptionalNullable


@sdk_endpoints
class Authentication(BaseSDK):
    r"""Token generation and refresh operations for NFL API access"""

    def _generate_token_config(
        self,
        *,
        client_key: str,
        client_secret: str,
        device_id: str,
        device_info: str,
        network_type: models.TokenRequestNetworkType,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        r"""Generate Initial Access Token

        Creates a new access token and refresh token for a client device. This is the initial authentication
        endpoint that establishes a session for accessing NFL APIs. Requires client credentials and device information.


        :param client_key: Client application identifier key
        :param client_secret: Client application secret for authentication
        :param device_id: Unique device identifier (UUID format)
        :param device_info: Base64-encoded JSON containing device information such as: {\"model\":\"desktop\",\"version\":\"Chrome\",\"osName\":\"Windows\",\"osVersion\":\"10\"}
        :param network_type: Type of network connection
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        request = models.TokenRequest(
            client_key=client_key,
            client_secret=client_secret,
            device_id=device_id,
            device_info=device_info,
            network_type=network_type,
        )

        return EndpointConfig(
            method="POST",
            path="/identity/v3/token",
            operation_id="generateToken",
            request=request,
            response_type=models.TokenResponse,
            error_status_codes=COLLECTION_ERROR_CODES,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.TokenRequest
            ),
        )

    def _refresh_token_config(
        self,
        *,
        client_key: str,
        client_secret: str,
        device_id: str,
        device_info: str,
        network_type: models.RefreshTokenRequestNetworkType,
        refresh_token: str,
        signature_timestamp: str,
        uid: str,
        uid_signature: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> EndpointConfig:
        r"""Refresh Access Token

        Refreshes an existing access token using a valid refresh token. This endpoint extends the user's
        session by generating new access and refresh tokens. Requires the previous refresh token and
        signature verification.


        :param client_key: Client application identifier key
        :param client_secret: Client application secret for authentication
        :param device_id: Unique device identifier (UUID format)
        :param device_info: Base64-encoded JSON containing device information such as: {\"model\":\"desktop\",\"version\":\"Chrome\",\"osName\":\"Windows\",\"osVersion\":\"10\"}
        :param network_type: Type of network connection
        :param refresh_token: Valid refresh token from previous authentication
        :param signature_timestamp: Unix timestamp for signature verification
        :param uid: User identifier hash
        :param uid_signature: HMAC signature for request verification
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        request = models.RefreshTokenRequest(
            client_key=client_key,
            client_secret=client_secret,
            device_id=device_id,
            device_info=device_info,
            network_type=network_type,
            refresh_token=refresh_token,
            signature_timestamp=signature_timestamp,
            uid=uid,
            uid_signature=uid_signature,
        )

        return EndpointConfig(
            method="POST",
            path="/identity/v3/token/refresh",
            operation_id="refreshToken",
            request=request,
            response_type=models.TokenResponse,
            error_status_codes=STATS_ERROR_CODES,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RefreshTokenRequest
            ),
        )
