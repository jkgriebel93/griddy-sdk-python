# Implementation Plan: Fix Broken Pydantic Models

## Priority: 1 (Highest)
## Estimated Effort: Medium
## Impact: High - Restores type safety and consistent API responses

---

## Problem Statement

Several endpoint methods bypass Pydantic model validation by returning raw `http_res.json()` instead of properly unmarshaled responses. This breaks type safety guarantees and causes inconsistent return types across the SDK.

### Affected Files and Methods

| File | Method | Current Return | Expected Return |
|------|--------|----------------|-----------------|
| `endpoints/pro/players.py:89` | `get_player()` | `http_res.json()` | `models.PlayerDetail` |
| `endpoints/regular/football/games.py:768` | (weekly game details) | `http_res.json()` | `List[models.WeeklyGameDetail]` |
| `endpoints/regular/football/draft.py:88` | `get_draft()` | `http_res.json()` | `models.DraftResponse` |

### Root Cause

TODO comments indicate "Something is being lost in the unmarshaling process" - suggesting the Pydantic models don't match the actual API response structure.

---

## Implementation Steps

### Step 1: Capture Raw API Responses

For each broken endpoint, capture the actual JSON response:

```python
# Temporary debugging approach
http_res = self.do_request(...)
if utils.match_response(http_res, "200", "application/json"):
    raw_json = http_res.json()
    # Save to file for analysis
    import json
    with open(f"debug_{operation_id}.json", "w") as f:
        json.dump(raw_json, f, indent=2)
```

**Files to create:**
- `tests/fixtures/debug/player_detail_raw.json`
- `tests/fixtures/debug/weekly_game_detail_raw.json`
- `tests/fixtures/debug/draft_response_raw.json`

### Step 2: Compare Against Pydantic Models

For each model, compare the raw JSON structure against the Pydantic model definition:

```bash
# Example analysis for PlayerDetail
# Check models/entities/player_detail.py against the raw JSON
```

**Common issues to look for:**
1. **Missing fields** - API returns fields not defined in model
2. **Type mismatches** - API returns string, model expects int
3. **Nested object differences** - Child models have similar issues
4. **Optional vs Required** - Field marked required but sometimes null in API
5. **Alias mismatches** - `camelCase` API field not mapped to `snake_case` Python field

### Step 3: Fix PlayerDetail Model

**File:** `src/griddy/nfl/models/entities/player_detail.py`

1. Load raw JSON response from Step 1
2. Generate corrected model using Pydantic's `model_json_schema()`:

```python
from pydantic import BaseModel
from typing import Optional, List

# Use datamodel-codegen or manual analysis
# datamodel-codegen --input debug_player_detail.json --output player_detail_fixed.py
```

3. Update the model with:
   - Correct field types
   - Proper `Optional[]` annotations for nullable fields
   - Correct `alias` values in `pydantic.Field()`
   - Any missing nested models

4. Add validation test:

```python
# tests/test_nfl/test_models/test_player_detail.py
def test_player_detail_validates_raw_response():
    with open("tests/fixtures/debug/player_detail_raw.json") as f:
        raw = json.load(f)

    # This should not raise
    player = models.PlayerDetail.model_validate(raw)
    assert player.nfl_id is not None
```

### Step 4: Fix WeeklyGameDetail Model

**File:** `src/griddy/nfl/models/entities/weekly_game_detail.py`

Follow same process as Step 3:
1. Analyze raw JSON structure
2. Update model fields
3. Add validation test

**Note:** This returns `List[WeeklyGameDetail]`, so ensure the model handles array responses.

### Step 5: Fix DraftResponse Model

**File:** `src/griddy/nfl/models/responses/draft_response.py`

Follow same process as Steps 3-4.

### Step 6: Update Endpoint Methods

Once models are fixed, update the endpoint methods to use proper unmarshaling:

**`endpoints/pro/players.py`:**
```python
# Before (line 86-89)
if utils.match_response(http_res, "200", "application/json"):
    # TODO: Something is being lost in the unmarshaling process. Fix it.
    # return unmarshal_json_response(models.PlayerDetail, http_res)
    return http_res.json()

# After
if utils.match_response(http_res, "200", "application/json"):
    return unmarshal_json_response(models.PlayerDetail, http_res)
```

**`endpoints/regular/football/games.py`:**
```python
# Before (line 766-768)
if utils.match_response(http_res, "200", "application/json"):
    # TODO: Fix Pydantic models
    # return unmarshal_json_response(List[models.WeeklyGameDetail], http_res)
    return http_res.json()

# After
if utils.match_response(http_res, "200", "application/json"):
    return unmarshal_json_response(List[models.WeeklyGameDetail], http_res)
```

**`endpoints/regular/football/draft.py`:**
```python
# Before (line 85-88)
if utils.match_response(http_res, "200", "application/json"):
    # return unmarshal_json_response(models.DraftResponse, http_res)
    # TODO: Return a proper pydantic object here
    return http_res.json()

# After
if utils.match_response(http_res, "200", "application/json"):
    return unmarshal_json_response(models.DraftResponse, http_res)
```

### Step 7: Update Type Hints

Ensure the method signatures return the correct types:

```python
# Before
def get_player(...) -> models.PlayerDetail:  # Lies! Returns dict
    ...
    return http_res.json()

# After
def get_player(...) -> models.PlayerDetail:  # Correct
    ...
    return unmarshal_json_response(models.PlayerDetail, http_res)
```

### Step 8: Add Integration Tests

Create tests that verify the full request/response cycle:

```python
# tests/test_nfl/test_endpoints/pro/test_players_integration.py
@pytest.mark.integration
def test_get_player_returns_pydantic_model(nfl_client):
    result = nfl_client.players.get_player(nfl_id=12345)

    # Verify it's a Pydantic model, not a dict
    assert isinstance(result, models.PlayerDetail)
    assert hasattr(result, 'model_dump')
```

---

## Validation Checklist

- [ ] Raw API responses captured for all broken endpoints
- [ ] Model discrepancies documented
- [ ] `PlayerDetail` model fixed and tested
- [ ] `WeeklyGameDetail` model fixed and tested
- [ ] `DraftResponse` model fixed and tested
- [ ] All `http_res.json()` calls replaced with `unmarshal_json_response()`
- [ ] TODO comments removed
- [ ] Integration tests pass
- [ ] Type checker (`mypy`) passes

---

## Rollback Plan

If issues arise:
1. Revert model changes
2. Keep `http_res.json()` fallback with proper type annotation:

```python
def get_player(...) -> Union[models.PlayerDetail, Dict[str, Any]]:
    """Returns PlayerDetail if model validates, otherwise raw dict."""
    ...
    try:
        return unmarshal_json_response(models.PlayerDetail, http_res)
    except ValidationError:
        return http_res.json()
```

---

## Files Modified

| File | Change Type |
|------|-------------|
| `models/entities/player_detail.py` | Fix model |
| `models/entities/weekly_game_detail.py` | Fix model |
| `models/responses/draft_response.py` | Fix model |
| `endpoints/pro/players.py` | Update return |
| `endpoints/regular/football/games.py` | Update return |
| `endpoints/regular/football/draft.py` | Update return |
| `tests/test_nfl/test_models/test_*.py` | Add tests |
