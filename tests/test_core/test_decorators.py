"""Unit tests for the sdk_endpoints class decorator."""

import inspect
from dataclasses import dataclass

import pytest

from griddy.core.decorators import sdk_endpoints

# ---------------------------------------------------------------------------
# Minimal stubs so we don't depend on the real BaseSDK / EndpointConfig
# ---------------------------------------------------------------------------


@dataclass
class FakeConfig:
    value: str


class FakeBaseSDK:
    """Mimics the two methods the decorator delegates to."""

    def _execute_endpoint(self, config):
        return f"sync:{config.value}"

    async def _execute_endpoint_async(self, config):
        return f"async:{config.value}"


# ---------------------------------------------------------------------------
# Decorated test classes
# ---------------------------------------------------------------------------


@sdk_endpoints
class SingleEndpoint(FakeBaseSDK):
    def _get_items_config(self, *, page: int = 1) -> FakeConfig:
        """List all items."""
        return FakeConfig(value=f"items-page-{page}")


@sdk_endpoints
class MultipleEndpoints(FakeBaseSDK):
    def _get_alpha_config(self) -> FakeConfig:
        """Alpha endpoint."""
        return FakeConfig(value="alpha")

    def _get_beta_config(self, *, key: str) -> FakeConfig:
        """Beta endpoint."""
        return FakeConfig(value=f"beta-{key}")


@sdk_endpoints
class NonGetNaming(FakeBaseSDK):
    """Config methods that don't start with _get_."""

    def _generate_token_config(self, *, secret: str) -> FakeConfig:
        """Generate a token."""
        return FakeConfig(value=f"token-{secret}")


@sdk_endpoints
class ManualOverride(FakeBaseSDK):
    def _get_data_config(self) -> FakeConfig:
        return FakeConfig(value="default")

    def get_data(self):
        """Manually overridden sync method."""
        return "custom-sync"


@sdk_endpoints
class MixinEndpoint:
    """Mixin that defines config but no _execute_endpoint — resolved at MRO time."""

    def _get_mixin_data_config(self) -> FakeConfig:
        """Mixin data."""
        return FakeConfig(value="mixin")


class ConcreteMixin(FakeBaseSDK, MixinEndpoint):
    pass


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestSyncGeneration:
    def test_sync_method_exists(self):
        assert hasattr(SingleEndpoint, "get_items")
        assert callable(SingleEndpoint.get_items)

    def test_sync_method_returns_correct_value(self):
        obj = SingleEndpoint()
        result = obj.get_items(page=3)
        assert result == "sync:items-page-3"

    def test_sync_default_args(self):
        obj = SingleEndpoint()
        result = obj.get_items()
        assert result == "sync:items-page-1"


@pytest.mark.unit
class TestAsyncGeneration:
    def test_async_method_exists(self):
        assert hasattr(SingleEndpoint, "get_items_async")
        assert callable(SingleEndpoint.get_items_async)

    @pytest.mark.asyncio
    async def test_async_method_returns_correct_value(self):
        obj = SingleEndpoint()
        result = await obj.get_items_async(page=5)
        assert result == "async:items-page-5"

    def test_async_method_is_coroutine(self):
        assert inspect.iscoroutinefunction(SingleEndpoint.get_items_async)


@pytest.mark.unit
class TestMultipleEndpoints:
    def test_alpha_sync(self):
        obj = MultipleEndpoints()
        assert obj.get_alpha() == "sync:alpha"

    @pytest.mark.asyncio
    async def test_beta_async(self):
        obj = MultipleEndpoints()
        assert await obj.get_beta_async(key="x") == "async:beta-x"


@pytest.mark.unit
class TestNonGetNaming:
    """Config methods that don't start with _get_ still work."""

    def test_sync_generated(self):
        obj = NonGetNaming()
        assert obj.generate_token(secret="abc") == "sync:token-abc"

    @pytest.mark.asyncio
    async def test_async_generated(self):
        obj = NonGetNaming()
        assert await obj.generate_token_async(secret="xyz") == "async:token-xyz"


@pytest.mark.unit
class TestManualOverride:
    def test_sync_not_overwritten(self):
        obj = ManualOverride()
        assert obj.get_data() == "custom-sync"

    @pytest.mark.asyncio
    async def test_async_still_generated(self):
        obj = ManualOverride()
        result = await obj.get_data_async()
        assert result == "async:default"


@pytest.mark.unit
class TestSignaturePreservation:
    def test_sync_preserves_params(self):
        sig = inspect.signature(SingleEndpoint.get_items)
        assert "page" in sig.parameters
        assert sig.parameters["page"].default == 1

    def test_async_preserves_params(self):
        sig = inspect.signature(SingleEndpoint.get_items_async)
        assert "page" in sig.parameters

    def test_annotations_inherited_from_config(self):
        """Annotations come from the config method via functools.wraps."""
        # functools.wraps copies __wrapped__, so inspect.signature
        # follows through to the config method's signature.
        sig = inspect.signature(SingleEndpoint.get_items)
        assert "page" in sig.parameters


@pytest.mark.unit
class TestDocstringPreservation:
    def test_sync_inherits_docstring(self):
        assert SingleEndpoint.get_items.__doc__ == "List all items."

    def test_async_inherits_docstring(self):
        assert SingleEndpoint.get_items_async.__doc__ == "List all items."


@pytest.mark.unit
class TestMixin:
    def test_mixin_methods_on_concrete_class(self):
        obj = ConcreteMixin()
        assert obj.get_mixin_data() == "sync:mixin"

    @pytest.mark.asyncio
    async def test_mixin_async_on_concrete_class(self):
        obj = ConcreteMixin()
        assert await obj.get_mixin_data_async() == "async:mixin"
