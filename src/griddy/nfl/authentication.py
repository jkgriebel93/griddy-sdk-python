from typing import Mapping, Optional

from . import errors, models, utils
from ._hooks import HookContext
from .basesdk import BaseSDK
from .types import UNSET, OptionalNullable
from .utils import get_security_from_env
from .utils.unmarshal_json_response import unmarshal_json_response


class Authentication(BaseSDK):
    r"""Token generation and refresh operations for NFL API access"""

    def generate_token(
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
    ) -> models.TokenResponse:
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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.TokenRequest(
            client_key=client_key,
            client_secret=client_secret,
            device_id=device_id,
            device_info=device_info,
            network_type=network_type,
        )

        req = self._build_request(
            method="POST",
            path="/identity/v3/token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.TokenRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="generateToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.TokenResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    async def generate_token_async(
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
    ) -> models.TokenResponse:
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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.TokenRequest(
            client_key=client_key,
            client_secret=client_secret,
            device_id=device_id,
            device_info=device_info,
            network_type=network_type,
        )

        req = self._build_request_async(
            method="POST",
            path="/identity/v3/token",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.TokenRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="generateToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.TokenResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    def refresh_token(
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
    ) -> models.TokenResponse:
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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

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

        req = self._build_request(
            method="POST",
            path="/identity/v3/token/refresh",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RefreshTokenRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="refreshToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.TokenResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    async def refresh_token_async(
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
    ) -> models.TokenResponse:
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
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

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

        req = self._build_request_async(
            method="POST",
            path="/identity/v3/token/refresh",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RefreshTokenRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="refreshToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.TokenResponse, http_res)
        if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )
        if utils.match_response(http_res, ["500", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
