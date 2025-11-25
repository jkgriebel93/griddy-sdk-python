from typing import Callable, Dict, List, Mapping, Optional, Tuple, Type, TypeVar
from urllib.parse import parse_qs, urlparse

import httpx

from ..nfl._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext
from ..nfl._hooks.types import HookContext
from ..nfl.utils import RetryConfig, SerializedRequestBody, get_body_content
from . import errors, models, utils
from .sdkconfiguration import SDKConfiguration
from .types import UNSET, OptionalNullable
from .utils.unmarshal_json_response import unmarshal_json_response

T = TypeVar("T")


class BaseSDK:
    sdk_configuration: SDKConfiguration
    parent_ref: Optional[object] = None
    """
    Reference to the root SDK instance, if any. This will prevent it from
    being garbage collected while there are active streams.
    """

    def __init__(
        self,
        sdk_config: SDKConfiguration,
        parent_ref: Optional[object] = None,
    ) -> None:
        self.sdk_configuration = sdk_config
        self.parent_ref = parent_ref

    def _get_url(self, base_url, url_variables):
        sdk_url, sdk_variables = self.sdk_configuration.get_server_details()

        if base_url is None:
            base_url = sdk_url

        if url_variables is None:
            url_variables = sdk_variables

        return utils.template_url(base_url, url_variables)

    # -------------------------------------------------------------------------
    # Helper methods to reduce boilerplate in endpoint implementations
    # -------------------------------------------------------------------------

    def _resolve_base_url(
        self,
        server_url: Optional[str] = None,
        url_variables: Optional[Dict[str, str]] = None,
    ) -> str:
        """
        Resolve the base URL for a request.

        Args:
            server_url: Optional server URL override
            url_variables: Optional URL template variables

        Returns:
            The resolved base URL string
        """
        if server_url is not None:
            return server_url
        return self._get_url(None, url_variables)

    def _resolve_timeout(self, timeout_ms: Optional[int] = None) -> Optional[int]:
        """
        Resolve timeout, falling back to SDK configuration.

        Args:
            timeout_ms: Optional timeout override in milliseconds

        Returns:
            The resolved timeout in milliseconds, or None
        """
        if timeout_ms is None:
            return self.sdk_configuration.timeout_ms
        return timeout_ms

    def _resolve_retry_config(
        self,
        retries: OptionalNullable[RetryConfig],
        retry_status_codes: Optional[List[str]] = None,
    ) -> Optional[Tuple[RetryConfig, List[str]]]:
        """
        Resolve retry configuration.

        Args:
            retries: Retry configuration from method parameter
            retry_status_codes: Status codes that should trigger a retry.
                               Defaults to ["429", "500", "502", "503", "504"]

        Returns:
            Tuple of (RetryConfig, status_codes) if retries are configured, else None
        """
        if retry_status_codes is None:
            retry_status_codes = ["429", "500", "502", "503", "504"]

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        if isinstance(retries, RetryConfig):
            return (retries, retry_status_codes)
        return None

    def _create_hook_context(
        self,
        operation_id: str,
        base_url: str,
    ) -> HookContext:
        """
        Create a HookContext for request execution.

        Args:
            operation_id: The operation identifier (e.g., "getPlayer")
            base_url: The base URL for the request

        Returns:
            A configured HookContext instance
        """
        return HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id=operation_id,
            oauth2_scopes=[],
            security_source=utils.get_security_from_env(
                self.sdk_configuration.security, models.Security
            ),
        )

    def _handle_json_response(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        """
        Handle JSON response with standard error handling.

        Args:
            http_res: The HTTP response object
            response_type: The Pydantic model type to unmarshal into
            error_status_codes: List of error status codes to handle

        Returns:
            The unmarshaled response object

        Raises:
            GriddyNFLDefaultError: If the response indicates an error
        """
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        # Handle client errors (4XX)
        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if client_errors and utils.match_response(http_res, client_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        # Handle server errors (5XX)
        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if server_errors and utils.match_response(http_res, server_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    async def _handle_json_response_async(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        """
        Handle JSON response with standard error handling (async version).

        Args:
            http_res: The HTTP response object
            response_type: The Pydantic model type to unmarshal into
            error_status_codes: List of error status codes to handle

        Returns:
            The unmarshaled response object

        Raises:
            GriddyNFLDefaultError: If the response indicates an error
        """
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        # Handle client errors (4XX)
        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if client_errors and utils.match_response(http_res, client_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        # Handle server errors (5XX)
        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if server_errors and utils.match_response(http_res, server_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    # -------------------------------------------------------------------------
    # End of helper methods
    # -------------------------------------------------------------------------

    def _build_request_async(
        self,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        client = self.sdk_configuration.async_client
        return self._build_request_with_client(
            client,
            method,
            path,
            base_url,
            url_variables,
            request,
            request_body_required,
            request_has_path_params,
            request_has_query_params,
            user_agent_header,
            accept_header_value,
            _globals,
            security,
            timeout_ms,
            get_serialized_body,
            url_override,
            http_headers,
        )

    def _build_request(
        self,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        client = self.sdk_configuration.client
        return self._build_request_with_client(
            client,
            method,
            path,
            base_url,
            url_variables,
            request,
            request_body_required,
            request_has_path_params,
            request_has_query_params,
            user_agent_header,
            accept_header_value,
            _globals,
            security,
            timeout_ms,
            get_serialized_body,
            url_override,
            http_headers,
        )

    def _build_request_with_client(
        self,
        client,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        query_params = {}

        url = url_override
        if url is None:
            url = utils.generate_url(
                self._get_url(base_url, url_variables),
                path,
                request if request_has_path_params else None,
                _globals if request_has_path_params else None,
            )

            query_params = utils.get_query_params(
                request if request_has_query_params else None,
                _globals if request_has_query_params else None,
            )
        else:
            # Pick up the query parameter from the override so they can be
            # preserved when building the request later on (necessary as of
            # httpx 0.28).
            parsed_override = urlparse(str(url_override))
            query_params = parse_qs(parsed_override.query, keep_blank_values=True)

        headers = utils.get_headers(request, _globals)
        headers["Accept"] = accept_header_value
        headers[user_agent_header] = self.sdk_configuration.user_agent

        if security is not None:
            if callable(security):
                security = security()
        security = utils.get_security_from_env(security, models.Security)
        if security is not None:
            security_headers, security_query_params = utils.get_security(security)
            headers = {**headers, **security_headers}
            query_params = {**query_params, **security_query_params}

        serialized_request_body = SerializedRequestBody()
        if get_serialized_body is not None:
            rb = get_serialized_body()
            if request_body_required and rb is None:
                raise ValueError("request body is required")

            if rb is not None:
                serialized_request_body = rb

        if (
            serialized_request_body.media_type is not None
            and serialized_request_body.media_type
            not in (
                "multipart/form-data",
                "multipart/mixed",
            )
        ):
            headers["content-type"] = serialized_request_body.media_type

        if http_headers is not None:
            for header, value in http_headers.items():
                headers[header] = value

        timeout = timeout_ms / 1000 if timeout_ms is not None else None

        return client.build_request(
            method,
            url,
            params=query_params,
            content=serialized_request_body.content,
            data=serialized_request_body.data,
            files=serialized_request_body.files,
            headers=headers,
            timeout=timeout,
        )

    def do_request(
        self,
        hook_ctx,
        request,
        error_status_codes,
        stream=False,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.client
        logger = self.sdk_configuration.debug_logger

        hooks = self.sdk_configuration.__dict__["_hooks"]

        def do():
            http_res = None
            try:
                req = hooks.before_request(BeforeRequestContext(hook_ctx), request)
                logger.debug(
                    "Request:\nMethod: %s\nURL: %s\nHeaders: %s\nBody: %s",
                    req.method,
                    req.url,
                    req.headers,
                    get_body_content(req),
                )

                if client is None:
                    raise ValueError("client is required")

                http_res = client.send(req, stream=stream)
            except Exception as e:
                _, e = hooks.after_error(AfterErrorContext(hook_ctx), None, e)
                if e is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise e

            if http_res is None:
                logger.debug("Raising no response SDK error")
                raise errors.NoResponseError("No response received")

            logger.debug(
                "Response:\nStatus Code: %s\nURL: %s\nHeaders: %s\nBody: %s",
                http_res.status_code,
                http_res.url,
                http_res.headers,
                "<streaming response>" if stream else http_res.text,
            )

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, err = hooks.after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if err is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise err
                if result is not None:
                    http_res = result
                else:
                    logger.debug("Raising unexpected SDK error")
                    raise errors.GriddyNFLDefaultError(
                        "Unexpected error occurred", http_res
                    )

            return http_res

        if retry_config is not None:
            http_res = utils.retry(do, utils.Retries(retry_config[0], retry_config[1]))
        else:
            http_res = do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = hooks.after_success(AfterSuccessContext(hook_ctx), http_res)

        return http_res

    async def do_request_async(
        self,
        hook_ctx,
        request,
        error_status_codes,
        stream=False,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.async_client
        logger = self.sdk_configuration.debug_logger

        hooks = self.sdk_configuration.__dict__["_hooks"]

        async def do():
            http_res = None
            try:
                req = hooks.before_request(BeforeRequestContext(hook_ctx), request)
                logger.debug(
                    "Request:\nMethod: %s\nURL: %s\nHeaders: %s\nBody: %s",
                    req.method,
                    req.url,
                    req.headers,
                    get_body_content(req),
                )

                if client is None:
                    raise ValueError("client is required")

                http_res = await client.send(req, stream=stream)
            except Exception as e:
                _, e = hooks.after_error(AfterErrorContext(hook_ctx), None, e)
                if e is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise e

            if http_res is None:
                logger.debug("Raising no response SDK error")
                raise errors.NoResponseError("No response received")

            logger.debug(
                "Response:\nStatus Code: %s\nURL: %s\nHeaders: %s\nBody: %s",
                http_res.status_code,
                http_res.url,
                http_res.headers,
                "<streaming response>" if stream else http_res.text,
            )

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, err = hooks.after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if err is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise err
                if result is not None:
                    http_res = result
                else:
                    logger.debug("Raising unexpected SDK error")
                    raise errors.GriddyNFLDefaultError(
                        "Unexpected error occurred", http_res
                    )

            return http_res

        if retry_config is not None:
            http_res = await utils.retry_async(
                do, utils.Retries(retry_config[0], retry_config[1])
            )
        else:
            http_res = await do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = hooks.after_success(AfterSuccessContext(hook_ctx), http_res)

        return http_res
