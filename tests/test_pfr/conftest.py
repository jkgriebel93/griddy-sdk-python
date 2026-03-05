"""Shared fixtures for PFR tests."""

from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def _mock_browserless_settings():
    with (
        patch(
            "griddy.pfr.utils.browserless.BROWSERLESS_HOST",
            "fake-host.example.com",
        ),
        patch(
            "griddy.pfr.utils.browserless.BROWSERLESS_TOKEN",
            "fake-token",
        ),
    ):
        yield
