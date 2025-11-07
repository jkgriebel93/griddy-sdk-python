import time
from uuid import uuid4

import pytest


@pytest.fixture
def nfl_auth_info():
    """
    Pytest fixture providing a sample NFL auth info dictionary.

    Returns a dictionary with:
    - expiresIn: Current timestamp (expired token)
    - refreshToken: Random UUID string
    - accessToken: "ZEBRA" test token

    Each test function gets a fresh instance with a new timestamp and UUID.
    """
    return {
        "expiresIn": time.time(),
        "refreshToken": str(uuid4()),
        "accessToken": "ZEBRA",
    }


@pytest.fixture
def nfl_auth_info_valid():
    """
    Pytest fixture providing a valid (non-expired) NFL auth info dictionary.

    Returns a dictionary with:
    - expiresIn: Timestamp 1 hour in the future
    - refreshToken: Random UUID string
    - accessToken: "ZEBRA" test token

    Each test function gets a fresh instance with a new timestamp and UUID.
    """
    return {
        "expiresIn": time.time() + 3600,  # Valid for 1 hour
        "refreshToken": str(uuid4()),
        "accessToken": "ZEBRA",
    }
