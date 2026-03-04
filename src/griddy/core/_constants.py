"""Shared constants for the NFL SDK.

This module provides standardized error codes and other constants used across
all SDK endpoints.
"""

from typing import List

# ---------------------------------------------------------------------------
# HTTP status code constants
# ---------------------------------------------------------------------------

# Successful response
HTTP_OK: str = "200"

# Prefix used to identify client error status codes (4xx)
CLIENT_ERROR_PREFIX: str = "4"

# Prefix used to identify server error status codes (5xx)
SERVER_ERROR_PREFIX: str = "5"

# Default status codes that trigger request retries
DEFAULT_RETRY_STATUS_CODES: List[str] = ["429", "500", "502", "503", "504"]

# ---------------------------------------------------------------------------
# Endpoint error code sets
# ---------------------------------------------------------------------------

# Standard error codes for collection endpoints (list operations)
# Does not include 404 since empty collections are valid responses
COLLECTION_ERROR_CODES: List[str] = ["400", "401", "4XX", "500", "5XX"]

# Standard error codes for single resource endpoints
# Includes 404 for when the resource doesn't exist
RESOURCE_ERROR_CODES: List[str] = ["400", "401", "404", "4XX", "500", "5XX"]

# Error codes for stats API endpoints
# Includes 403 for authorization/access control errors
STATS_ERROR_CODES: List[str] = ["400", "401", "403", "4XX", "500", "5XX"]

# Error codes for secured/protected resource endpoints
# Includes both 403 (forbidden) and 404 (not found)
SECURED_RESOURCE_ERROR_CODES: List[str] = [
    "400",
    "401",
    "403",
    "404",
    "4XX",
    "500",
    "5XX",
]

# Error codes for Next Gen Stats (NGS) endpoints
# Includes both 403 (forbidden) and 404 (not found)
NGS_ERROR_CODES: List[str] = ["400", "401", "403", "404", "4XX", "500", "5XX"]

# Error codes for parameterless endpoints (no query/path params to validate)
# Excludes 400 (no params to be invalid) and 403/404
PARAMETERLESS_ERROR_CODES: List[str] = ["401", "4XX", "500", "5XX"]
