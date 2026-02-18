from typing import Any, Callable, List, Optional, Tuple

import httpx

from .types import (
    AfterErrorContext,
    AfterErrorHook,
    AfterSuccessContext,
    AfterSuccessHook,
    BeforeRequestContext,
    BeforeRequestHook,
    Hooks,
    SDKInitHook,
)


class SDKHooks(Hooks):
    """Generic SDK hooks dispatcher.

    Args:
        init_hooks_fn: Optional callable that registers hooks on this instance.
            Each SDK passes its own registration function.
    """

    def __init__(
        self, init_hooks_fn: Optional[Callable[["SDKHooks"], None]] = None
    ) -> None:
        self.sdk_init_hooks: List[SDKInitHook] = []
        self.before_request_hooks: List[BeforeRequestHook] = []
        self.after_success_hooks: List[AfterSuccessHook] = []
        self.after_error_hooks: List[AfterErrorHook] = []
        if init_hooks_fn is not None:
            init_hooks_fn(self)

    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        self.sdk_init_hooks.append(hook)

    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        self.before_request_hooks.append(hook)

    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        self.after_success_hooks.append(hook)

    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        self.after_error_hooks.append(hook)

    def sdk_init(self, config: Any) -> Any:
        for hook in self.sdk_init_hooks:
            config = hook.sdk_init(config)
        return config

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        for hook in self.before_request_hooks:
            out = hook.before_request(hook_ctx, request)
            if isinstance(out, Exception):
                raise out
            request = out

        return request

    def after_success(
        self, hook_ctx: AfterSuccessContext, response: httpx.Response
    ) -> httpx.Response:
        for hook in self.after_success_hooks:
            out = hook.after_success(hook_ctx, response)
            if isinstance(out, Exception):
                raise out
            response = out
        return response

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception],
    ) -> Tuple[Optional[httpx.Response], Optional[Exception]]:
        for hook in self.after_error_hooks:
            result = hook.after_error(hook_ctx, response, error)
            if isinstance(result, Exception):
                raise result
            response, error = result
        return response, error
