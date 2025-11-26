# Implementation Plan: Sync/Async Factory Pattern

## Priority: 6 (Lowest, but Highest Impact)
## Estimated Effort: High
## Impact: Very High - Eliminates ~5,000+ lines of duplicated code

---

## Problem Statement

Every endpoint method is duplicated for sync and async versions:

```python
# 103 lines
def get_player(self, *, nfl_id: int, ...) -> models.PlayerDetail:
    # Setup
    # Build request
    # Configure retry
    # Execute sync
    # Handle response

# 103 lines (nearly identical)
async def get_player_async(self, *, nfl_id: int, ...) -> models.PlayerDetail:
    # Setup (same)
    # Build request (same, but _build_request_async)
    # Configure retry (same)
    # Execute async
    # Handle response (same, but stream_to_text_async)
```

With 109 endpoint methods, this results in ~11,000 lines where ~5,500 are duplicates.

---

## Analysis of Differences

The sync and async versions differ only in:

| Aspect | Sync | Async |
|--------|------|-------|
| Method definition | `def method()` | `async def method_async()` |
| Request builder | `_build_request()` | `_build_request_async()` |
| Request executor | `do_request()` | `do_request_async()` |
| Stream to text | `utils.stream_to_text()` | `utils.stream_to_text_async()` |

Everything else (setup, validation, error handling logic) is identical.

---

## Proposed Solution: Request Executor Pattern

Create a generic request executor that can run in both sync and async modes.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Endpoint Method                          │
│  def get_player(self, nfl_id: int, ...) -> PlayerDetail    │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  RequestConfig                              │
│  - method, path, request model                              │
│  - response type, error codes                               │
│  - operation_id for hooks                                   │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  _execute_request()                         │
│  - sync: bool parameter                                     │
│  - Handles all request/response logic                       │
│  - Returns properly typed response                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation Steps

### Step 1: Create Request Configuration Dataclass

**File:** `src/griddy/nfl/types/request_config.py`

```python
"""Request configuration for endpoint methods."""

from dataclasses import dataclass, field
from typing import Any, List, Mapping, Optional, Type, TypeVar

T = TypeVar('T')


@dataclass
class RequestConfig:
    """Configuration for executing an API request."""

    # HTTP method and path
    method: str
    path: str

    # Request model instance (contains query params, path params, body)
    request: Any

    # Response type for unmarshaling
    response_type: Type[T]

    # Operation identifier for hooks
    operation_id: str

    # Error handling
    error_status_codes: List[str] = field(
        default_factory=lambda: ["400", "401", "4XX", "500", "5XX"]
    )

    # Request configuration
    request_has_query_params: bool = True
    request_has_path_params: bool = False
    request_body_required: bool = False

    # Headers
    accept_header: str = "application/json"
    user_agent_header: str = "user-agent"

    # Optional overrides (passed from method parameters)
    server_url: Optional[str] = None
    timeout_ms: Optional[int] = None
    http_headers: Optional[Mapping[str, str]] = None
    retries: Any = None  # OptionalNullable[RetryConfig]
```

### Step 2: Add Unified Executor to BaseSDK

**File:** `src/griddy/nfl/basesdk.py`

```python
from typing import Type, TypeVar, Union, overload
from griddy.nfl.types.request_config import RequestConfig

T = TypeVar('T')


class BaseSDK:
    # ... existing methods ...

    def _execute_request(
        self,
        config: RequestConfig,
    ) -> T:
        """
        Execute a synchronous API request.

        This is the main entry point for all sync endpoint methods.
        """
        return self._execute_request_impl(config, is_async=False)

    async def _execute_request_async(
        self,
        config: RequestConfig,
    ) -> T:
        """
        Execute an asynchronous API request.

        This is the main entry point for all async endpoint methods.
        """
        return await self._execute_request_impl(config, is_async=True)

    def _execute_request_impl(
        self,
        config: RequestConfig,
        is_async: bool,
    ):
        """
        Internal implementation of request execution.

        Handles both sync and async modes with unified logic.
        """
        # Resolve configuration
        base_url = self._resolve_base_url(config.server_url)
        timeout_ms = self._resolve_timeout(config.timeout_ms)

        # Build request
        build_fn = self._build_request_async if is_async else self._build_request
        req = build_fn(
            method=config.method,
            path=config.path,
            base_url=base_url,
            url_variables=None,
            request=config.request,
            request_body_required=config.request_body_required,
            request_has_path_params=config.request_has_path_params,
            request_has_query_params=config.request_has_query_params,
            user_agent_header=config.user_agent_header,
            accept_header_value=config.accept_header,
            http_headers=config.http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        # Resolve retry config
        retry_config = self._resolve_retry_config(config.retries)

        # Create hook context
        hook_ctx = self._create_hook_context(config.operation_id, base_url)

        # Execute request
        if is_async:
            return self._execute_async_request(
                hook_ctx, req, config.error_status_codes,
                retry_config, config.response_type
            )
        else:
            return self._execute_sync_request(
                hook_ctx, req, config.error_status_codes,
                retry_config, config.response_type
            )

    def _execute_sync_request(
        self,
        hook_ctx: HookContext,
        req: httpx.Request,
        error_status_codes: List[str],
        retry_config: Optional[tuple],
        response_type: Type[T],
    ) -> T:
        """Execute sync request and handle response."""
        http_res = self.do_request(
            hook_ctx=hook_ctx,
            request=req,
            error_status_codes=error_status_codes,
            retry_config=retry_config,
        )
        return self._handle_json_response(http_res, response_type, error_status_codes)

    async def _execute_async_request(
        self,
        hook_ctx: HookContext,
        req: httpx.Request,
        error_status_codes: List[str],
        retry_config: Optional[tuple],
        response_type: Type[T],
    ) -> T:
        """Execute async request and handle response."""
        http_res = await self.do_request_async(
            hook_ctx=hook_ctx,
            request=req,
            error_status_codes=error_status_codes,
            retry_config=retry_config,
        )
        return await self._handle_json_response_async(
            http_res, response_type, error_status_codes
        )
```

### Step 3: Refactor One Endpoint as Proof of Concept

**File:** `src/griddy/nfl/endpoints/pro/players.py`

```python
# Before: 206 lines for sync + async
def get_player(
    self,
    *,
    nfl_id: int,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.PlayerDetail:
    r"""Get Player Details

    Retrieves detailed information about a specific NFL player.
    """
    # ... 90+ lines of implementation

async def get_player_async(
    self,
    *,
    nfl_id: int,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.PlayerDetail:
    r"""Get Player Details

    Retrieves detailed information about a specific NFL player.
    """
    # ... 90+ lines of nearly identical implementation
```

```python
# After: ~40 lines total for both sync + async
from griddy.nfl.types.request_config import RequestConfig
from griddy.nfl.errors import RESOURCE_ERROR_CODES


def get_player(
    self,
    *,
    nfl_id: int,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.PlayerDetail:
    r"""Get Player Details

    Retrieves detailed information about a specific NFL player.
    """
    config = RequestConfig(
        method="GET",
        path="/api/players/player",
        request=models.GetPlayerRequest(nfl_id=nfl_id),
        response_type=models.PlayerDetail,
        operation_id="getPlayer",
        error_status_codes=RESOURCE_ERROR_CODES,
        server_url=server_url,
        timeout_ms=timeout_ms,
        http_headers=http_headers,
        retries=retries,
    )
    return self._execute_request(config)


async def get_player_async(
    self,
    *,
    nfl_id: int,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.PlayerDetail:
    r"""Get Player Details

    Retrieves detailed information about a specific NFL player.
    """
    config = RequestConfig(
        method="GET",
        path="/api/players/player",
        request=models.GetPlayerRequest(nfl_id=nfl_id),
        response_type=models.PlayerDetail,
        operation_id="getPlayer",
        error_status_codes=RESOURCE_ERROR_CODES,
        server_url=server_url,
        timeout_ms=timeout_ms,
        http_headers=http_headers,
        retries=retries,
    )
    return await self._execute_request_async(config)
```

### Step 4: Further Reduce with Helper Method (Optional)

For endpoints with many methods, create a helper to reduce config duplication:

```python
class Players(ProSDK):

    def _make_config(
        self,
        method: str,
        path: str,
        request: Any,
        response_type: Type[T],
        operation_id: str,
        *,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        error_codes: List[str] = RESOURCE_ERROR_CODES,
    ) -> RequestConfig:
        return RequestConfig(
            method=method,
            path=path,
            request=request,
            response_type=response_type,
            operation_id=operation_id,
            error_status_codes=error_codes,
            server_url=server_url,
            timeout_ms=timeout_ms,
            http_headers=http_headers,
            retries=retries,
        )

    def get_player(self, *, nfl_id: int, **kwargs) -> models.PlayerDetail:
        r"""Get Player Details"""
        config = self._make_config(
            "GET", "/api/players/player",
            models.GetPlayerRequest(nfl_id=nfl_id),
            models.PlayerDetail, "getPlayer",
            **kwargs
        )
        return self._execute_request(config)

    async def get_player_async(self, *, nfl_id: int, **kwargs) -> models.PlayerDetail:
        r"""Get Player Details"""
        config = self._make_config(
            "GET", "/api/players/player",
            models.GetPlayerRequest(nfl_id=nfl_id),
            models.PlayerDetail, "getPlayer",
            **kwargs
        )
        return await self._execute_request_async(config)
```

### Step 5: Create Migration Script

**File:** `scripts/refactor_sync_async.py`

```python
#!/usr/bin/env python3
"""
Helper script to refactor endpoint files to use the new factory pattern.

This script analyzes endpoint files and generates refactored versions.
"""

import ast
import re
from pathlib import Path
from typing import List, Tuple


def find_endpoint_methods(file_path: Path) -> List[Tuple[str, str]]:
    """Find sync/async method pairs in an endpoint file."""
    content = file_path.read_text()
    tree = ast.parse(content)

    methods = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not node.name.startswith('_'):
                methods.append(('sync', node.name))
        elif isinstance(node, ast.AsyncFunctionDef):
            if not node.name.startswith('_'):
                methods.append(('async', node.name))

    return methods


def analyze_method_for_refactoring(method_source: str) -> dict:
    """Extract key information from a method for refactoring."""
    # Extract: method, path, request model, response type, operation_id
    info = {
        'http_method': re.search(r'method="(\w+)"', method_source),
        'path': re.search(r'path="([^"]+)"', method_source),
        'operation_id': re.search(r'operation_id="([^"]+)"', method_source),
        # ... more extraction
    }
    return info


def main():
    endpoints_dir = Path("src/griddy/nfl/endpoints")
    for py_file in endpoints_dir.rglob("*.py"):
        if py_file.name.startswith('_') or py_file.name == '__init__.py':
            continue

        methods = find_endpoint_methods(py_file)
        sync_methods = [m[1] for m in methods if m[0] == 'sync']
        async_methods = [m[1] for m in methods if m[0] == 'async']

        # Find pairs
        pairs = []
        for sync in sync_methods:
            async_name = f"{sync}_async"
            if async_name in async_methods:
                pairs.append((sync, async_name))

        if pairs:
            print(f"\n{py_file}: {len(pairs)} method pairs")
            for sync, async_ in pairs:
                print(f"  - {sync}() / {async_}()")


if __name__ == "__main__":
    main()
```

### Step 6: Incremental Migration

Migrate files in order of complexity:

**Phase 1: Simple Endpoints (1-3 methods)**
- [ ] `endpoints/pro/transactions.py`
- [ ] `endpoints/pro/betting.py`
- [ ] `endpoints/regular/football/injuries.py`
- [ ] `endpoints/regular/football/venues.py`
- [ ] `endpoints/regular/football/weeks.py`

**Phase 2: Medium Endpoints (4-6 methods)**
- [ ] `endpoints/pro/players.py`
- [ ] `endpoints/pro/games.py`
- [ ] `endpoints/regular/football/standings.py`
- [ ] `endpoints/regular/football/rosters.py`
- [ ] `endpoints/regular/football/combine.py`
- [ ] `endpoints/regular/football/draft.py`

**Phase 3: Complex Endpoints (7+ methods)**
- [ ] `endpoints/pro/teams.py`
- [ ] `endpoints/pro/schedules.py`
- [ ] `endpoints/pro/content.py`
- [ ] `endpoints/regular/football/games.py`

**Phase 4: Stats Endpoints**
- [ ] `endpoints/pro/stats/passing.py`
- [ ] `endpoints/pro/stats/rushing.py`
- [ ] `endpoints/pro/stats/receiving.py`
- [ ] `endpoints/pro/stats/defense.py`
- [ ] `endpoints/pro/stats/team_offense.py`
- [ ] `endpoints/pro/stats/team_defense.py`
- [ ] `endpoints/pro/stats/fantasy.py`

**Phase 5: Mixins**
- [ ] `endpoints/pro/mixins.py` (or split files)

---

## Validation Checklist

- [ ] `RequestConfig` dataclass created
- [ ] `_execute_request()` and `_execute_request_async()` added to BaseSDK
- [ ] Helper response handlers working
- [ ] One endpoint fully migrated as proof of concept
- [ ] All tests pass for migrated endpoint
- [ ] Type hints work correctly with generics
- [ ] Migration script created
- [ ] Phase 1 endpoints migrated
- [ ] Phase 2 endpoints migrated
- [ ] Phase 3 endpoints migrated
- [ ] Phase 4 endpoints migrated
- [ ] Phase 5 (mixins) migrated
- [ ] All integration tests pass
- [ ] Mypy passes

---

## Estimated Impact

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Lines per method pair | ~180 | ~40 | 78% |
| Total endpoint LOC | ~19,620 | ~4,360 | ~15,260 lines |
| Boilerplate ratio | ~85% | ~20% | 65 points |

---

## Risk Mitigation

### Type Safety
The generic `T` type parameter ensures proper typing:
```python
def _execute_request(self, config: RequestConfig[T]) -> T:
```

### Behavioral Parity
Add integration tests that compare responses:
```python
def test_sync_async_parity(client):
    sync_result = client.players.get_player(nfl_id=12345)
    async_result = asyncio.run(client.players.get_player_async(nfl_id=12345))

    assert sync_result.model_dump() == async_result.model_dump()
```

### Rollback
Keep original implementations commented initially:
```python
def get_player(self, *, nfl_id: int, ...) -> models.PlayerDetail:
    # NEW IMPLEMENTATION
    config = RequestConfig(...)
    return self._execute_request(config)

    # ORIGINAL (remove after validation)
    # base_url = None
    # url_variables = None
    # ...
```

---

## Files Modified/Created

| File | Change Type |
|------|-------------|
| `types/request_config.py` | New file |
| `basesdk.py` | Add executor methods |
| `endpoints/pro/*.py` | Refactor all |
| `endpoints/pro/stats/*.py` | Refactor all |
| `endpoints/regular/**/*.py` | Refactor all |
| `scripts/refactor_sync_async.py` | New file |
| `tests/test_nfl/test_basesdk.py` | Add tests |
