# Implementation Plan: Extract Common Helpers to BaseSDK

## Priority: 2
## Estimated Effort: Low-Medium
## Impact: High - Reduces ~2,200+ lines of boilerplate across all endpoints

---

## Problem Statement

Every endpoint method contains identical boilerplate for:
1. Request preparation (base URL, timeout setup) - ~9 lines per method
2. Retry configuration - ~6 lines per method
3. Response handling and error raising - ~15-20 lines per method

With 100+ endpoint methods, this results in thousands of lines of duplicated code.

---

## Current Pattern (Repeated in Every Method)

```python
def some_endpoint(
    self,
    *,
    param: str,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> SomeResponse:
    # BLOCK 1: Request preparation (9 lines)
    base_url = None
    url_variables = None
    if timeout_ms is None:
        timeout_ms = self.sdk_configuration.timeout_ms

    if server_url is not None:
        base_url = server_url
    else:
        base_url = self._get_url(base_url, url_variables)

    request = models.SomeRequest(param=param)

    req = self._build_request(
        method="GET",
        path="/api/endpoint",
        base_url=base_url,
        url_variables=url_variables,
        request=request,
        request_body_required=False,
        request_has_path_params=False,
        request_has_query_params=True,
        user_agent_header="user-agent",
        accept_header_value="application/json",
        http_headers=http_headers,
        security=self.sdk_configuration.security,
        timeout_ms=timeout_ms,
    )

    # BLOCK 2: Retry configuration (6 lines)
    if retries == UNSET:
        if self.sdk_configuration.retry_config is not UNSET:
            retries = self.sdk_configuration.retry_config

    retry_config = None
    if isinstance(retries, utils.RetryConfig):
        retry_config = (retries, ["429", "500", "502", "503", "504"])

    # BLOCK 3: Execute and handle response (20 lines)
    http_res = self.do_request(
        hook_ctx=HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="someEndpoint",
            oauth2_scopes=[],
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.Security
            ),
        ),
        request=req,
        error_status_codes=["400", "401", "404", "4XX", "500", "5XX"],
        retry_config=retry_config,
    )

    if utils.match_response(http_res, "200", "application/json"):
        return unmarshal_json_response(SomeResponse, http_res)
    if utils.match_response(http_res, ["400", "401", "404", "4XX"], "*"):
        http_res_text = utils.stream_to_text(http_res)
        raise errors.GriddyNFLDefaultError("API error occurred", http_res, http_res_text)
    if utils.match_response(http_res, ["500", "5XX"], "*"):
        http_res_text = utils.stream_to_text(http_res)
        raise errors.GriddyNFLDefaultError("API error occurred", http_res, http_res_text)

    raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
```

---

## Implementation Steps

### Step 1: Add Helper Methods to BaseSDK

**File:** `src/griddy/nfl/basesdk.py`

Add these helper methods:

```python
from typing import Type, TypeVar, Tuple, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class RequestConfig:
    """Configuration for building an HTTP request."""
    method: str
    path: str
    request: object
    operation_id: str
    request_has_query_params: bool = True
    request_has_path_params: bool = False
    request_body_required: bool = False
    accept_header: str = "application/json"


class BaseSDK:
    # ... existing code ...

    def _resolve_base_url(
        self,
        server_url: Optional[str] = None,
        url_variables: Optional[Dict[str, str]] = None,
    ) -> str:
        """Resolve the base URL for a request."""
        if server_url is not None:
            return server_url
        return self._get_url(None, url_variables)

    def _resolve_timeout(self, timeout_ms: Optional[int] = None) -> Optional[int]:
        """Resolve timeout, falling back to SDK configuration."""
        if timeout_ms is None:
            return self.sdk_configuration.timeout_ms
        return timeout_ms

    def _resolve_retry_config(
        self,
        retries: OptionalNullable[utils.RetryConfig],
        retry_status_codes: Optional[List[str]] = None,
    ) -> Optional[Tuple[utils.RetryConfig, List[str]]]:
        """Resolve retry configuration."""
        if retry_status_codes is None:
            retry_status_codes = ["429", "500", "502", "503", "504"]

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        if isinstance(retries, utils.RetryConfig):
            return (retries, retry_status_codes)
        return None

    def _create_hook_context(
        self,
        operation_id: str,
        base_url: str,
    ) -> HookContext:
        """Create a HookContext for request execution."""
        return HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id=operation_id,
            oauth2_scopes=[],
            security_source=utils.get_security_from_env(
                self.sdk_configuration.security, models.Security
            ),
        )

    def _handle_json_response(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        """Handle JSON response with standard error handling."""
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        # Client errors (4XX)
        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if utils.match_response(http_res, client_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        # Server errors (5XX)
        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if utils.match_response(http_res, server_errors, "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)

    async def _handle_json_response_async(
        self,
        http_res: httpx.Response,
        response_type: Type[T],
        error_status_codes: List[str],
    ) -> T:
        """Handle JSON response with standard error handling (async version)."""
        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(response_type, http_res)

        client_errors = [code for code in error_status_codes if code.startswith("4")]
        if utils.match_response(http_res, client_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        server_errors = [code for code in error_status_codes if code.startswith("5")]
        if utils.match_response(http_res, server_errors, "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.GriddyNFLDefaultError(
                "API error occurred", http_res, http_res_text
            )

        raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
```

### Step 2: Update One Endpoint as Proof of Concept

**File:** `src/griddy/nfl/endpoints/pro/players.py`

Before (102 lines for sync method):
```python
def get_player(self, *, nfl_id: int, ...) -> models.PlayerDetail:
    # ... 35+ lines of boilerplate ...
```

After (~20 lines):
```python
def get_player(
    self,
    *,
    nfl_id: int,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.PlayerDetail:
    r"""Get Player Details"""
    base_url = self._resolve_base_url(server_url)
    timeout_ms = self._resolve_timeout(timeout_ms)

    request = models.GetPlayerRequest(nfl_id=nfl_id)

    req = self._build_request(
        method="GET",
        path="/api/players/player",
        base_url=base_url,
        url_variables=None,
        request=request,
        request_body_required=False,
        request_has_path_params=False,
        request_has_query_params=True,
        user_agent_header="user-agent",
        accept_header_value="application/json",
        http_headers=http_headers,
        security=self.sdk_configuration.security,
        timeout_ms=timeout_ms,
    )

    retry_config = self._resolve_retry_config(retries)
    error_codes = ["400", "401", "404", "4XX", "500", "5XX"]

    http_res = self.do_request(
        hook_ctx=self._create_hook_context("getPlayer", base_url),
        request=req,
        error_status_codes=error_codes,
        retry_config=retry_config,
    )

    return self._handle_json_response(http_res, models.PlayerDetail, error_codes)
```

### Step 3: Create Migration Script

Create a script to assist with updating other endpoints:

**File:** `scripts/refactor_endpoints.py`

```python
#!/usr/bin/env python3
"""Helper script to identify refactoring candidates in endpoint files."""

import re
from pathlib import Path

BOILERPLATE_PATTERNS = [
    r"base_url = None\n\s+url_variables = None",
    r"if timeout_ms is None:\n\s+timeout_ms = self\.sdk_configuration\.timeout_ms",
    r"if retries == UNSET:\n\s+if self\.sdk_configuration\.retry_config",
]

def find_boilerplate(file_path: Path) -> list:
    """Find boilerplate patterns in a file."""
    content = file_path.read_text()
    findings = []
    for pattern in BOILERPLATE_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            findings.append((pattern, len(matches)))
    return findings

def main():
    endpoints_dir = Path("src/griddy/nfl/endpoints")
    for py_file in endpoints_dir.rglob("*.py"):
        if py_file.name.startswith("_"):
            continue
        findings = find_boilerplate(py_file)
        if findings:
            print(f"\n{py_file}:")
            for pattern, count in findings:
                print(f"  - Found {count} instances of boilerplate")

if __name__ == "__main__":
    main()
```

### Step 4: Update Remaining Pro Endpoints

Apply the refactoring to all Pro API endpoints:

- [ ] `endpoints/pro/players.py` (4 methods)
- [ ] `endpoints/pro/teams.py` (7 methods)
- [ ] `endpoints/pro/games.py` (4 methods)
- [ ] `endpoints/pro/schedules.py` (7 methods)
- [ ] `endpoints/pro/content.py` (9 methods)
- [ ] `endpoints/pro/betting.py` (2 methods)
- [ ] `endpoints/pro/transactions.py` (1 method)
- [ ] `endpoints/pro/mixins.py` (19 methods across mixins)
- [ ] `endpoints/pro/stats/*.py` (24+ methods)

### Step 5: Update Regular API Endpoints

Apply the refactoring to Regular API endpoints:

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

### Step 6: Add Unit Tests for Helpers

**File:** `tests/test_nfl/test_basesdk.py`

```python
import pytest
from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.types import UNSET


class TestBaseSDKHelpers:
    def test_resolve_timeout_uses_provided_value(self, mock_sdk):
        result = mock_sdk._resolve_timeout(5000)
        assert result == 5000

    def test_resolve_timeout_falls_back_to_config(self, mock_sdk):
        mock_sdk.sdk_configuration.timeout_ms = 3000
        result = mock_sdk._resolve_timeout(None)
        assert result == 3000

    def test_resolve_retry_config_with_unset(self, mock_sdk):
        result = mock_sdk._resolve_retry_config(UNSET)
        assert result is None

    def test_resolve_retry_config_with_config(self, mock_sdk):
        from griddy.nfl.utils import RetryConfig
        retry = RetryConfig(max_retries=3)
        result = mock_sdk._resolve_retry_config(retry)
        assert result[0] == retry
        assert "429" in result[1]
```

---

## Validation Checklist

- [ ] Helper methods added to `BaseSDK`
- [ ] Unit tests for all helper methods
- [ ] One endpoint fully refactored as proof of concept
- [ ] All Pro API endpoints updated
- [ ] All Regular API endpoints updated
- [ ] Integration tests pass
- [ ] Type checker (`mypy`) passes
- [ ] No behavioral changes (responses identical)

---

## Estimated Line Reduction

| Helper | Lines Saved Per Method | Methods | Total Saved |
|--------|------------------------|---------|-------------|
| `_resolve_base_url()` | 4 | 109 | 436 |
| `_resolve_timeout()` | 2 | 109 | 218 |
| `_resolve_retry_config()` | 6 | 109 | 654 |
| `_handle_json_response()` | 12 | 109 | 1,308 |
| **Total** | **24** | **109** | **~2,600** |

---

## Files Modified

| File | Change Type |
|------|-------------|
| `basesdk.py` | Add helper methods |
| `endpoints/pro/*.py` | Refactor all endpoint files |
| `endpoints/regular/**/*.py` | Refactor all endpoint files |
| `tests/test_nfl/test_basesdk.py` | Add tests |
