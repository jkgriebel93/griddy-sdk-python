"""Tests verifying docstrings and type annotations for the nfl/hooks module (TGF-164)."""

import inspect

import pytest

from griddy.nfl._hooks.hack_auth import HackAuthHook
from griddy.nfl._hooks.registration import init_hooks
from griddy.nfl._hooks.sdkhooks import SDKHooks

_ITEMS_NEEDING_DOCSTRINGS = [
    # hack_auth.py
    (HackAuthHook, "HackAuthHook"),
    (HackAuthHook._do_refresh_token, "HackAuthHook._do_refresh_token"),
    (HackAuthHook.before_request, "HackAuthHook.before_request"),
    # sdkhooks.py
    (SDKHooks.__init__, "SDKHooks.__init__"),
]


@pytest.mark.unit
class TestDocstringsExist:
    @pytest.mark.parametrize(
        "obj,name",
        [pytest.param(obj, name, id=name) for obj, name in _ITEMS_NEEDING_DOCSTRINGS],
    )
    def test_has_docstring(self, obj, name):
        assert obj.__doc__ is not None, f"{name} is missing a docstring"
        assert len(obj.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestReturnTypeAnnotations:
    def test_init_hooks_has_return_type(self):
        hints = inspect.get_annotations(init_hooks)
        assert "return" in hints, "init_hooks is missing a return type annotation"

    def test_do_refresh_token_has_return_type(self):
        hints = inspect.get_annotations(HackAuthHook._do_refresh_token)
        assert "return" in hints, (
            "HackAuthHook._do_refresh_token is missing a return type annotation"
        )


@pytest.mark.unit
class TestParamTypeAnnotations:
    def test_do_refresh_token_refresh_token_has_type(self):
        hints = inspect.get_annotations(HackAuthHook._do_refresh_token)
        assert "refresh_token" in hints, (
            "HackAuthHook._do_refresh_token is missing type annotation for param 'refresh_token'"
        )
