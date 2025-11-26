# NFL SDK Refactoring Analysis

## Package Overview

- **338 Python files** (~43,195 lines of code)
- **272 model files** (entities, requests, responses, enums)
- **31 endpoint files** across Pro and Regular APIs

---

## High-Priority Refactoring Opportunities

### 1. Sync/Async Method Duplication (~5,000+ lines)

Every endpoint method has nearly identical sync and async versions:

```python
# players.py - 103 lines sync + 103 lines async for same logic
def get_player(...): ...
async def get_player_async(...): ...  # Near-identical implementation
```

**Recommendation:** Create a decorator or method factory pattern:
```python
def _execute_request(self, sync: bool, ...):
    # Shared logic here

def get_player(...):
    return self._execute_request(sync=True, ...)

async def get_player_async(...):
    return await self._execute_request(sync=False, ...)
```

### 2. Request Handling Boilerplate (repeated 100+ times)

This 30+ line block appears in every method:

```python
base_url = None
url_variables = None
if timeout_ms is None:
    timeout_ms = self.sdk_configuration.timeout_ms
if server_url is not None:
    base_url = server_url
else:
    base_url = self._get_url(base_url, url_variables)
# ... setup continues
```

**Recommendation:** Extract to `_prepare_request()` helper in `BaseSDK`.

### 3. Response Handling Inconsistency

Some methods use proper unmarshaling, others bypass it:

```python
# Proper pattern (most methods)
return unmarshal_json_response(models.PlayerDetail, http_res)

# Bypass pattern (due to model issues)
return http_res.json()  # TODO: Fix Pydantic model
```

**Files with TODOs indicating broken models:**
- `endpoints/pro/games.py` - `get_gamecenter()`, `get_live_game_scores()`
- `endpoints/pro/mixins.py` - `get_game_team_rankings()` (returns empty dict)

### 4. Duplicated Dynamic Import Logic

Both `sdk.py:37-55` and `endpoints/pro/stats/__init__.py` contain identical `dynamic_import()` methods.

**Recommendation:** Extract to shared utility in `utils/imports.py`.

### 5. Inconsistent Error Status Codes

Different endpoints use different error codes for similar operations:
- `get_player()`: `["400", "401", "404", "4XX", "500", "5XX"]`
- `get_all_teams()`: `["401", "4XX", "500", "5XX"]` (missing 400)
- `get_projected_stats()`: `["400", "401", "4XX", "500", "5XX"]` (missing 404)

**Recommendation:** Define constants:
```python
DEFAULT_ERROR_CODES = ["400", "401", "4XX", "500", "5XX"]
WITH_NOT_FOUND_CODES = ["400", "401", "404", "4XX", "500", "5XX"]
```

---

## Medium-Priority Refactoring Opportunities

### 6. Oversized Files

| File | Lines | Issue |
|------|-------|-------|
| `endpoints/pro/mixins.py` | 1,917 | Contains multiple unrelated mixins |
| `endpoints/regular/football/games.py` | 887 | Multiple game-related concerns |
| `models/__init__.py` | ~2,600 | Consider generating dynamically |

### 7. Model Redundancy

Stats response models repeat identical pagination fields:
```python
# Appears in 6+ response models
limit: int
offset: int
season: int
season_type: SeasonTypeEnum
sort_key: str
sort_value: SortOrderEnum
total: int
```

**Recommendation:** Create `PaginatedStatsResponse` base class.

### 8. Request Parameter Repetition

Pagination parameters repeated across 20+ stats methods:
```python
limit: Optional[int] = 35,
offset: Optional[int] = 0,
page: Optional[int] = 1,
sort_key: Optional[...] = None,
sort_value: Optional[SortOrderEnum] = None,
```

**Recommendation:** Create `PaginationParams` dataclass or TypedDict.

### 9. Non-Standard Import Paths (66 cases)

Some models have inconsistent module paths in `_dynamic_imports`:
```python
# Non-standard (should be .responses.defensive_stats_response)
"DefensiveStatsResponse": ".defensivestatsresponse",

# Non-standard (lives in response file, not entity)
"Leaders": ".game_center_response",
```

---

## Low-Priority / Good Practices Already Present

### What's Working Well

1. **Lazy-loading sub-SDKs** - Prevents circular imports, reduces startup time
2. **Type safety** - Pydantic + TypedDict dual-model pattern
3. **Consistent naming** - `Get{Resource}Request`, `{Resource}Response`
4. **Mixin pattern** - `GameScheduleMixin`, `GameContentMixin` for shared logic
5. **Hook system** - Clean request/response interception

---

## Estimated Impact

| Refactoring | LOC Reduction | Effort |
|-------------|---------------|--------|
| Sync/async deduplication | 5,000+ | High |
| Request preparation helper | 1,000+ | Low |
| Response handler helper | 1,600+ | Medium |
| Retry config helper | 600+ | Low |
| Error code constants | 100+ | Very Low |
| **Total potential** | **~8,300+ lines** | |

---

## Recommended Priority Order

Each item below links to a detailed implementation plan:

1. **[Fix broken Pydantic models](refactoring/01_FIX_PYDANTIC_MODELS.md)** - Restore type safety by fixing models that currently return `http_res.json()`
2. **[Extract common helpers to BaseSDK](refactoring/02_EXTRACT_BASESDK_HELPERS.md)** - Reduce boilerplate with request prep, retry config, and response handling helpers
3. **[Deduplicate dynamic_import logic](refactoring/03_DEDUPLICATE_DYNAMIC_IMPORT.md)** - Consolidate duplicated import utilities
4. **[Standardize error codes](refactoring/04_STANDARDIZE_ERROR_CODES.md)** - Define constants for consistent error handling
5. **[Split large files](refactoring/05_SPLIT_LARGE_FILES.md)** - Break up oversized files (mixins.py, games.py)
6. **[Sync/async factory pattern](refactoring/06_SYNC_ASYNC_FACTORY.md)** - Eliminate method duplication (largest impact, highest effort)

---

## Implementation Plan Summary

| Plan | Priority | Effort | LOC Impact | Key Files |
|------|----------|--------|------------|-----------|
| [01 - Fix Pydantic Models](refactoring/01_FIX_PYDANTIC_MODELS.md) | 1 | Medium | Type safety | `models/entities/*.py` |
| [02 - BaseSDK Helpers](refactoring/02_EXTRACT_BASESDK_HELPERS.md) | 2 | Low-Med | ~2,600 lines | `basesdk.py` |
| [03 - Dynamic Import](refactoring/03_DEDUPLICATE_DYNAMIC_IMPORT.md) | 3 | Low | ~26 lines | `utils/imports.py` |
| [04 - Error Codes](refactoring/04_STANDARDIZE_ERROR_CODES.md) | 4 | Very Low | ~100 lines | `errors/__init__.py` |
| [05 - Split Files](refactoring/05_SPLIT_LARGE_FILES.md) | 5 | Medium | Maintainability | `endpoints/pro/mixins/` |
| [06 - Sync/Async Factory](refactoring/06_SYNC_ASYNC_FACTORY.md) | 6 | High | ~15,260 lines | All endpoints |
