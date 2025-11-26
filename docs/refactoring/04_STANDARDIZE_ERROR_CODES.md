# Implementation Plan: Standardize Error Status Codes

## Priority: 4
## Estimated Effort: Very Low
## Impact: Medium - Improves consistency and maintainability

---

## Problem Statement

Different endpoint methods use different error status code sets for similar operations, leading to inconsistent error handling:

| Method | Error Codes |
|--------|-------------|
| `get_player()` | `["400", "401", "404", "4XX", "500", "5XX"]` |
| `get_all_teams()` | `["401", "4XX", "500", "5XX"]` |
| `get_projected_stats()` | `["400", "401", "4XX", "500", "5XX"]` |
| `get_current_week_games()` | `["401", "4XX", "500", "5XX"]` |
| `get_team_roster()` | `["400", "401", "404", "4XX", "500", "5XX"]` |

This inconsistency makes it unclear which errors an endpoint might raise and complicates error handling for SDK consumers.

---

## Current Usage Analysis

From grep analysis of `error_status_codes=` across the codebase:

### Pattern 1: Full Error Set (Most Common)
```python
error_status_codes=["400", "401", "404", "4XX", "500", "5XX"]
```
Used by: Single-resource GET endpoints (get_player, get_team, get_game)

### Pattern 2: Without 404 (List Endpoints)
```python
error_status_codes=["400", "401", "4XX", "500", "5XX"]
```
Used by: List/collection endpoints (get_all_teams, get_schedules)

### Pattern 3: Minimal (Auth-Only)
```python
error_status_codes=["401", "4XX", "500", "5XX"]
```
Used by: Some endpoints missing 400 validation errors

### Pattern 4: With 403 (Rare)
```python
error_status_codes=["400", "401", "403", "4XX", "500", "5XX"]
```
Used by: Endpoints that may have authorization restrictions

---

## Implementation Steps

### Step 1: Define Error Code Constants

**File:** `src/griddy/nfl/errors/__init__.py`

```python
"""Error handling for the NFL SDK."""

from .griddynflerror import GriddyNFLError
from .griddynfldefaulterror import GriddyNFLDefaultError
from .no_response_error import NoResponseError
from .responsevalidationerror import ResponseValidationError

# Standard error status code sets
# Use these constants instead of inline lists for consistency

# Standard set for single-resource endpoints (GET /resource/{id})
# Includes 404 for "not found" scenarios
RESOURCE_ERROR_CODES = ["400", "401", "404", "4XX", "500", "5XX"]

# Standard set for collection/list endpoints (GET /resources)
# No 404 because empty list is valid response, not an error
COLLECTION_ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]

# Standard set for authenticated endpoints without resource lookup
# Used when 404 is not applicable
AUTH_ERROR_CODES = ["401", "4XX", "500", "5XX"]

# Standard set for endpoints with authorization checks
# Includes 403 Forbidden in addition to 401 Unauthorized
AUTHZ_ERROR_CODES = ["400", "401", "403", "4XX", "500", "5XX"]

# Standard retry status codes (used with RetryConfig)
RETRY_STATUS_CODES = ["429", "500", "502", "503", "504"]

__all__ = [
    "GriddyNFLError",
    "GriddyNFLDefaultError",
    "NoResponseError",
    "ResponseValidationError",
    # Error code constants
    "RESOURCE_ERROR_CODES",
    "COLLECTION_ERROR_CODES",
    "AUTH_ERROR_CODES",
    "AUTHZ_ERROR_CODES",
    "RETRY_STATUS_CODES",
]
```

### Step 2: Document Error Code Usage

Add docstrings explaining when to use each set:

```python
# RESOURCE_ERROR_CODES
"""
Use for endpoints that fetch a single resource by ID.

Example endpoints:
- GET /api/players/player?nflId={id}
- GET /api/teams/team?teamId={id}
- GET /api/schedules/game?gameId={id}

Expected errors:
- 400: Invalid request parameters
- 401: Authentication required/invalid
- 404: Resource not found
- 4XX: Other client errors
- 5XX: Server errors
"""

# COLLECTION_ERROR_CODES
"""
Use for endpoints that return lists/collections.

Example endpoints:
- GET /api/teams
- GET /api/schedules
- GET /api/stats/passing

Expected errors:
- 400: Invalid request parameters (e.g., invalid season)
- 401: Authentication required/invalid
- 4XX: Other client errors
- 5XX: Server errors

Note: Empty results return 200 with empty array, not 404.
"""
```

### Step 3: Update Endpoint Files

#### Example: `endpoints/pro/players.py`

```python
# Before
from griddy.nfl import errors, models, utils

# ...

http_res = self.do_request(
    hook_ctx=HookContext(...),
    request=req,
    error_status_codes=["400", "401", "404", "4XX", "500", "5XX"],
    retry_config=retry_config,
)
```

```python
# After
from griddy.nfl import errors, models, utils
from griddy.nfl.errors import RESOURCE_ERROR_CODES, RETRY_STATUS_CODES

# ...

http_res = self.do_request(
    hook_ctx=HookContext(...),
    request=req,
    error_status_codes=RESOURCE_ERROR_CODES,
    retry_config=retry_config,
)
```

#### Example: `endpoints/pro/teams.py`

```python
# get_all_teams - uses COLLECTION_ERROR_CODES
http_res = self.do_request(
    hook_ctx=HookContext(...),
    request=req,
    error_status_codes=COLLECTION_ERROR_CODES,  # No 404
    retry_config=retry_config,
)

# get_team - uses RESOURCE_ERROR_CODES
http_res = self.do_request(
    hook_ctx=HookContext(...),
    request=req,
    error_status_codes=RESOURCE_ERROR_CODES,  # With 404
    retry_config=retry_config,
)
```

### Step 4: Update Retry Configuration

Also standardize the retry status codes:

```python
# Before (in every method)
retry_config = None
if isinstance(retries, utils.RetryConfig):
    retry_config = (retries, ["429", "500", "502", "503", "504"])

# After
from griddy.nfl.errors import RETRY_STATUS_CODES

retry_config = None
if isinstance(retries, utils.RetryConfig):
    retry_config = (retries, RETRY_STATUS_CODES)
```

### Step 5: Create Migration Checklist

Track which files have been updated:

**Pro API Endpoints:**
- [ ] `endpoints/pro/players.py`
- [ ] `endpoints/pro/teams.py`
- [ ] `endpoints/pro/games.py`
- [ ] `endpoints/pro/schedules.py`
- [ ] `endpoints/pro/content.py`
- [ ] `endpoints/pro/betting.py`
- [ ] `endpoints/pro/transactions.py`
- [ ] `endpoints/pro/mixins.py`
- [ ] `endpoints/pro/stats/passing.py`
- [ ] `endpoints/pro/stats/rushing.py`
- [ ] `endpoints/pro/stats/receiving.py`
- [ ] `endpoints/pro/stats/defense.py`
- [ ] `endpoints/pro/stats/team_offense.py`
- [ ] `endpoints/pro/stats/team_defense.py`
- [ ] `endpoints/pro/stats/fantasy.py`

**Regular API Endpoints:**
- [ ] `endpoints/regular/football/games.py`
- [ ] `endpoints/regular/football/draft.py`
- [ ] `endpoints/regular/football/combine.py`
- [ ] `endpoints/regular/football/rosters.py`
- [ ] `endpoints/regular/football/standings.py`
- [ ] `endpoints/regular/football/teams.py`
- [ ] `endpoints/regular/football/venues.py`
- [ ] `endpoints/regular/football/weeks.py`
- [ ] `endpoints/regular/football/injuries.py`
- [ ] `endpoints/regular/authentication.py`

### Step 6: Add Validation in BaseSDK (Optional)

Add runtime validation to catch incorrect usage:

```python
# basesdk.py
VALID_ERROR_CODE_SETS = {
    frozenset(["400", "401", "404", "4XX", "500", "5XX"]),  # RESOURCE_ERROR_CODES
    frozenset(["400", "401", "4XX", "500", "5XX"]),         # COLLECTION_ERROR_CODES
    frozenset(["401", "4XX", "500", "5XX"]),                # AUTH_ERROR_CODES
    frozenset(["400", "401", "403", "4XX", "500", "5XX"]),  # AUTHZ_ERROR_CODES
}

def do_request(
    self,
    hook_ctx,
    request,
    error_status_codes,
    # ...
):
    # Optional: Warn about non-standard error code sets in development
    if __debug__:
        code_set = frozenset(error_status_codes)
        if code_set not in VALID_ERROR_CODE_SETS:
            import warnings
            warnings.warn(
                f"Non-standard error_status_codes: {error_status_codes}. "
                f"Consider using a standard set from griddy.nfl.errors.",
                UserWarning,
            )
    # ... rest of method
```

---

## Validation Checklist

- [ ] Error code constants defined in `errors/__init__.py`
- [ ] Constants exported in `__all__`
- [ ] Documentation added for each constant
- [ ] All Pro API endpoints updated
- [ ] All Regular API endpoints updated
- [ ] Retry status codes also standardized
- [ ] All tests pass
- [ ] Type checker passes

---

## Files Modified

| File | Change Type |
|------|-------------|
| `errors/__init__.py` | Add constants |
| `endpoints/pro/*.py` | Use constants |
| `endpoints/pro/stats/*.py` | Use constants |
| `endpoints/regular/**/*.py` | Use constants |
| `basesdk.py` | Optional validation |

---

## Benefits

1. **Consistency**: All similar endpoints use same error codes
2. **Maintainability**: Change error handling in one place
3. **Documentation**: Constants are self-documenting
4. **Discoverability**: IDE autocomplete shows available options
5. **Type Safety**: Can type-hint as `Literal[...]` if needed

---

## Error Code Reference

| Constant | Codes | Use Case |
|----------|-------|----------|
| `RESOURCE_ERROR_CODES` | 400, 401, 404, 4XX, 5XX | Single resource by ID |
| `COLLECTION_ERROR_CODES` | 400, 401, 4XX, 5XX | List/collection endpoints |
| `AUTH_ERROR_CODES` | 401, 4XX, 5XX | Auth-only endpoints |
| `AUTHZ_ERROR_CODES` | 400, 401, 403, 4XX, 5XX | With authorization |
| `RETRY_STATUS_CODES` | 429, 500, 502, 503, 504 | Retryable errors |
