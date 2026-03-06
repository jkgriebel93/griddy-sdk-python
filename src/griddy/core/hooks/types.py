from abc import ABC, abstractmethod
from typing import Any, Callable, List, Optional, Tuple, Union

import httpx


class HookContext:
    """Base context carrying config, base URL, operation ID, and security for hook callbacks."""

    config: Any  # SDKConfiguration (generic — each SDK provides its own)
    base_url: str
    operation_id: str
    oauth2_scopes: Optional[List[str]] = None
    security_source: Optional[Union[Any, Callable[[], Any]]] = None

    def __init__(
        self,
        config: Any,
        base_url: str,
        operation_id: str,
        oauth2_scopes: Optional[List[str]],
        security_source: Optional[Union[Any, Callable[[], Any]]],
    ):
        """Initialize the hook context."""
        self.config = config
        self.base_url = base_url
        self.operation_id = operation_id
        self.oauth2_scopes = oauth2_scopes
        self.security_source = security_source


class BeforeRequestContext(HookContext):
    """Hook context passed to before-request hooks."""

    def __init__(self, hook_ctx: HookContext):
        """Initialize from an existing HookContext."""
        super().__init__(
            hook_ctx.config,
            hook_ctx.base_url,
            hook_ctx.operation_id,
            hook_ctx.oauth2_scopes,
            hook_ctx.security_source,
        )


class AfterSuccessContext(HookContext):
    """Hook context passed to after-success hooks."""

    def __init__(self, hook_ctx: HookContext):
        """Initialize from an existing HookContext."""
        super().__init__(
            hook_ctx.config,
            hook_ctx.base_url,
            hook_ctx.operation_id,
            hook_ctx.oauth2_scopes,
            hook_ctx.security_source,
        )


class AfterErrorContext(HookContext):
    """Hook context passed to after-error hooks."""

    def __init__(self, hook_ctx: HookContext):
        """Initialize from an existing HookContext."""
        super().__init__(
            hook_ctx.config,
            hook_ctx.base_url,
            hook_ctx.operation_id,
            hook_ctx.oauth2_scopes,
            hook_ctx.security_source,
        )


class SDKInitHook(ABC):
    """Abstract hook called once during SDK initialization."""

    @abstractmethod
    def sdk_init(self, config: Any) -> Any:
        """Receive and optionally modify the SDK configuration."""
        pass


class BeforeRequestHook(ABC):
    """Abstract hook called before each HTTP request is sent."""

    @abstractmethod
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        """Inspect or modify the request before sending."""
        pass


class AfterSuccessHook(ABC):
    """Abstract hook called after a successful HTTP response."""

    @abstractmethod
    def after_success(
        self, hook_ctx: AfterSuccessContext, response: httpx.Response
    ) -> Union[httpx.Response, Exception]:
        """Inspect or modify the response after success."""
        pass


class AfterErrorHook(ABC):
    """Abstract hook called after an HTTP error response or exception."""

    @abstractmethod
    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception],
    ) -> Union[Tuple[Optional[httpx.Response], Optional[Exception]], Exception]:
        """Handle or modify the error response and exception."""
        pass


class Hooks(ABC):
    """Abstract base for hook registries."""

    @abstractmethod
    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        """Register an SDK initialization hook."""
        pass

    @abstractmethod
    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        """Register a before-request hook."""
        pass

    @abstractmethod
    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        """Register an after-success hook."""
        pass

    @abstractmethod
    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        """Register an after-error hook."""
        pass
