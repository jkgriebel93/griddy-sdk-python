"""Tests for griddy.core.hooks module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.hooks.sdkhooks import SDKHooks
from griddy.core.hooks.types import (
    AfterErrorContext,
    AfterErrorHook,
    AfterSuccessContext,
    AfterSuccessHook,
    BeforeRequestContext,
    BeforeRequestHook,
    HookContext,
    SDKInitHook,
)


def _make_hook_context(**kwargs):
    defaults = {
        "config": Mock(),
        "base_url": "https://example.com",
        "operation_id": "testOp",
        "oauth2_scopes": [],
        "security_source": None,
    }
    defaults.update(kwargs)
    return HookContext(**defaults)


@pytest.mark.unit
class TestHookContext:
    def test_stores_attributes(self):
        config = Mock()
        ctx = HookContext(
            config=config,
            base_url="https://example.com",
            operation_id="testOp",
            oauth2_scopes=["read"],
            security_source=None,
        )
        assert ctx.config is config
        assert ctx.base_url == "https://example.com"
        assert ctx.operation_id == "testOp"
        assert ctx.oauth2_scopes == ["read"]
        assert ctx.security_source is None

    def test_before_request_context_wraps_hook_context(self):
        ctx = _make_hook_context(operation_id="myOp")
        before_ctx = BeforeRequestContext(ctx)
        assert before_ctx.operation_id == "myOp"
        assert before_ctx.base_url == ctx.base_url

    def test_after_success_context_wraps_hook_context(self):
        ctx = _make_hook_context(operation_id="myOp")
        after_ctx = AfterSuccessContext(ctx)
        assert after_ctx.operation_id == "myOp"

    def test_after_error_context_wraps_hook_context(self):
        ctx = _make_hook_context(operation_id="myOp")
        err_ctx = AfterErrorContext(ctx)
        assert err_ctx.operation_id == "myOp"


@pytest.mark.unit
class TestSDKHooks:
    def test_init_without_hooks(self):
        hooks = SDKHooks()
        assert hooks.sdk_init_hooks == []
        assert hooks.before_request_hooks == []
        assert hooks.after_success_hooks == []
        assert hooks.after_error_hooks == []

    def test_init_with_hook_registration_fn(self):
        class MyInitHook(SDKInitHook):
            def sdk_init(self, config):
                return config

        def register(hooks):
            hooks.register_sdk_init_hook(MyInitHook())

        sdk_hooks = SDKHooks(init_hooks_fn=register)
        assert len(sdk_hooks.sdk_init_hooks) == 1

    def test_sdk_init_calls_hooks_in_order(self):
        calls = []

        class Hook1(SDKInitHook):
            def sdk_init(self, config):
                calls.append("hook1")
                return config

        class Hook2(SDKInitHook):
            def sdk_init(self, config):
                calls.append("hook2")
                return config

        hooks = SDKHooks()
        hooks.register_sdk_init_hook(Hook1())
        hooks.register_sdk_init_hook(Hook2())
        hooks.sdk_init(Mock())
        assert calls == ["hook1", "hook2"]

    def test_before_request_calls_hooks(self):
        request = Mock(spec=httpx.Request)
        modified_request = Mock(spec=httpx.Request)

        class MyHook(BeforeRequestHook):
            def before_request(self, hook_ctx, req):
                return modified_request

        hooks = SDKHooks()
        hooks.register_before_request_hook(MyHook())

        ctx = BeforeRequestContext(_make_hook_context())
        result = hooks.before_request(ctx, request)
        assert result is modified_request

    def test_before_request_raises_on_exception_return(self):
        class MyHook(BeforeRequestHook):
            def before_request(self, hook_ctx, req):
                return ValueError("hook error")

        hooks = SDKHooks()
        hooks.register_before_request_hook(MyHook())

        ctx = BeforeRequestContext(_make_hook_context())
        with pytest.raises(ValueError, match="hook error"):
            hooks.before_request(ctx, Mock(spec=httpx.Request))

    def test_after_success_calls_hooks(self):
        response = Mock(spec=httpx.Response)
        modified_response = Mock(spec=httpx.Response)

        class MyHook(AfterSuccessHook):
            def after_success(self, hook_ctx, resp):
                return modified_response

        hooks = SDKHooks()
        hooks.register_after_success_hook(MyHook())

        ctx = AfterSuccessContext(_make_hook_context())
        result = hooks.after_success(ctx, response)
        assert result is modified_response

    def test_after_error_returns_tuple(self):
        response = Mock(spec=httpx.Response)
        error = ValueError("test")

        class MyHook(AfterErrorHook):
            def after_error(self, hook_ctx, resp, err):
                return (resp, None)

        hooks = SDKHooks()
        hooks.register_after_error_hook(MyHook())

        ctx = AfterErrorContext(_make_hook_context())
        result_resp, result_err = hooks.after_error(ctx, response, error)
        assert result_resp is response
        assert result_err is None

    def test_after_error_raises_on_exception_return(self):
        class MyHook(AfterErrorHook):
            def after_error(self, hook_ctx, resp, err):
                return RuntimeError("hook error")

        hooks = SDKHooks()
        hooks.register_after_error_hook(MyHook())

        ctx = AfterErrorContext(_make_hook_context())
        with pytest.raises(RuntimeError, match="hook error"):
            hooks.after_error(ctx, None, ValueError("original"))

    def test_no_hooks_passthrough(self):
        hooks = SDKHooks()
        request = Mock(spec=httpx.Request)
        response = Mock(spec=httpx.Response)

        ctx = _make_hook_context()
        assert hooks.before_request(BeforeRequestContext(ctx), request) is request
        assert hooks.after_success(AfterSuccessContext(ctx), response) is response
        r, e = hooks.after_error(AfterErrorContext(ctx), response, None)
        assert r is response
        assert e is None
