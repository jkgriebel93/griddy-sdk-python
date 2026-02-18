from dataclasses import dataclass, field
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)
from urllib.parse import parse_qs, urlparse

import httpx

from griddy.core import utils
from griddy.core.hooks import (
    AfterErrorContext,
    AfterSuccessContext,
    BeforeRequestContext,
)
from griddy.core.hooks.types import HookContext
from griddy.core.types import UNSET, OptionalNullable
from griddy.core.utils import RetryConfig, SerializedRequestBody, get_body_content
from griddy.core.utils.unmarshal_json_response import unmarshal_json_response

T = TypeVar("T")


@dataclass
class EndpointConfig:
    """Configuration for an API endpoint, enabling sync/async factory pattern.

    This dataclass captures all the configuration needed to execute an endpoint,
    allowing a single definition to generate both sync and async implementations.
    """

    # HTTP method and path
    method: str
    path: str
    operation_id: str

    # Request model instance (already constructed with parameters)
    request: Any

    # Response configuration
    response_type: Type[T]
    error_status_codes: List[str]

    # Request configuration flags
    request_body_required: bool = False
    request_has_path_params: bool = False
    request_has_query_params: bool = True

    # Optional overrides
    server_url: Optional[str] = None
    timeout_ms: Optional[int] = None
    http_headers: Optional[Mapping[str, str]] = None
    retries: Any = field(default_factory=lambda: UNSET)  # OptionalNullable[RetryConfig]

    # For endpoints that need raw JSON (due to Pydantic model issues)
    return_raw_json: bool = False

    # Optional body serializer
    get_serialized_body: Optional[Callable[[], Optional[SerializedRequestBody]]] = None

    # Standard headers (rarely need to change)
    user_agent_header: str = "user-agent"
    accept_header_value: str = "application/json"


class BaseSDK:
    sdk_configuration: Any  # SDKConfiguration (provider-specific subclass)
    parent_ref: Optional[object] = None

    # Subclasses override these to inject provider-specific error/model classes.
    # Using properties allows lazy loading of error modules.
    @property
    def _default_error_cls(self) -> Type[Exception]:
        from griddy.core.errors import DefaultSDKError

        return DefaultSDKError

    @property
    def _no_response_error_cls(self) -> Type[Exception]:
        from griddy.core.errors import NoResponseError

        return NoResponseError

    @property
    def _security_model_cls(self) -> Any:
        return None

    @property
    def _security_env_mapping(self) -> Optional[Dict[str, str]]:
        """Mapping of security field names to environment variable names."""
        return None

    def __init__(
        self,
        sdk_config: Any,
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

    def _resolve_base_url(
        self,
        server_url: Optional[str] = None,
        url_variables: Optional[Dict[str, str]] = None,
    ) -> str:
        if server_url is not None:
            return server_url
        return self._get_url(None, url_variables)

    def _resolve_timeout(self, timeout_ms: Optional[int] = None) -> Optional[int]:
        if timeout_ms is None:
            return self.sdk_configuration.timeout_ms
        return timeout_ms

    def _resolve_retry_config(
        self,
        retries: OptionalNullable[RetryConfig],
        retry_status_codes: Optional[List[str]] = None,
    ) -> Optional[Tuple[RetryConfig, List[str]]]:
        if retry_status_codes is None:
            retry_status_codes = ["429", "500", "502", "503", "504"]

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        if isinstance(retries, RetryConfig):
            return (retries, retry_status_codes)
        return None

    def _get_security_from_env(self, security: Any) -> Any:
        """Resolve security from env vars. Subclasses can override."""
        security_cls = self._security_model_cls
        if security_cls is None:
            return security
        env_mapping = self._security_env_mapping
        from griddy.core.utils.security import get_security_from_env

        return get_security_from_env(security, security_cls, env_mapping)

    def _create_hook_context(
        self,
        operation_id: str,
        base_url: str,
    ) -> HookContext:
        return HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id=operation_id,
            oauth2_scopes=[],
            security_source=self._get_security_from_env(
                self.sdk_configuration.security
            ),
        )

    def _handle_json_response(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if client_errors and utils.match_response(http_res, client_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise self._default_error_cls("API error occurred", http_res, http_res_text)

        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if server_errors and utils.match_response(http_res, server_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise self._default_error_cls("API error occurred", http_res, http_res_text)

        raise self._default_error_cls("Unexpected response received", http_res)

    async def _handle_json_response_async(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if client_errors and utils.match_response(http_res, client_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise self._default_error_cls("API error occurred", http_res, http_res_text)

        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if server_errors and utils.match_response(http_res, server_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise self._default_error_cls("API error occurred", http_res, http_res_text)

        raise self._default_error_cls("Unexpected response received", http_res)

    def _execute_endpoint(self, config: EndpointConfig) -> T:
        base_url = self._resolve_base_url(config.server_url)
        timeout_ms = self._resolve_timeout(config.timeout_ms)

        req = self._build_request(
            method=config.method,
            path=config.path,
            base_url=base_url,
            url_variables=None,
            request=config.request,
            request_body_required=config.request_body_required,
            request_has_path_params=config.request_has_path_params,
            request_has_query_params=config.request_has_query_params,
            user_agent_header=config.user_agent_header,
            accept_header_value=config.accept_header_value,
            http_headers=config.http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
            get_serialized_body=config.get_serialized_body,
        )

        retry_config = self._resolve_retry_config(config.retries)
        http_res = self.do_request(
            hook_ctx=self._create_hook_context(config.operation_id, base_url),
            request=req,
            error_status_codes=config.error_status_codes,
            retry_config=retry_config,
        )

        if config.return_raw_json:
            if utils.match_response(http_res, "200", "application/json"):
                return http_res.json()

        return self._handle_json_response(
            http_res, config.response_type, config.error_status_codes
        )

    async def _execute_endpoint_async(self, config: EndpointConfig) -> T:
        base_url = self._resolve_base_url(config.server_url)
        timeout_ms = self._resolve_timeout(config.timeout_ms)

        req = self._build_request_async(
            method=config.method,
            path=config.path,
            base_url=base_url,
            url_variables=None,
            request=config.request,
            request_body_required=config.request_body_required,
            request_has_path_params=config.request_has_path_params,
            request_has_query_params=config.request_has_query_params,
            user_agent_header=config.user_agent_header,
            accept_header_value=config.accept_header_value,
            http_headers=config.http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
            get_serialized_body=config.get_serialized_body,
        )

        retry_config = self._resolve_retry_config(config.retries)

        http_res = await self.do_request_async(
            hook_ctx=self._create_hook_context(config.operation_id, base_url),
            request=req,
            error_status_codes=config.error_status_codes,
            retry_config=retry_config,
        )

        if config.return_raw_json:
            if utils.match_response(http_res, "200", "application/json"):
                return http_res.json()

        return await self._handle_json_response_async(
            http_res, config.response_type, config.error_status_codes
        )

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
            parsed_override = urlparse(str(url_override))
            query_params = parse_qs(parsed_override.query, keep_blank_values=True)

        headers = utils.get_headers(request, _globals)
        headers["Accept"] = accept_header_value
        headers[user_agent_header] = self.sdk_configuration.user_agent

        if security is not None:
            if callable(security):
                security = security()
        security = self._get_security_from_env(security)
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
                raise self._no_response_error_cls("No response received")

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
                    raise self._default_error_cls("Unexpected error occurred", http_res)

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
                raise self._no_response_error_cls("No response received")

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
                    raise self._default_error_cls("Unexpected error occurred", http_res)

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
