# SDK Integration Tests

## Overview

The `test_sdk_integration.py` file contains comprehensive unit tests that verify the GriddyNFL SDK properly integrates with all sub-SDK classes from the `griddy.nfl.endpoints` package.

## Test Coverage

### Total Tests: 51

The test suite is organized into 6 test classes covering different aspects of SDK integration:

## Test Classes

### 1. TestEndpointsSubSDKAccess (24 tests)

Verifies that all 12 endpoint sub-SDKs can be properly accessed from a GriddyNFL instance.

**Sub-SDKs Tested:**
- `combine` - Combine information (Regular API)
- `draft` - Draft information (Regular API)
- `games` - Game information (Regular API)
- `rosters` - Team rosters (Regular API)
- `standings` - Standings information (Regular API)
- `football_teams` - Team information (Regular API)
- `weeks` - Weekly information (Regular API)
- `content` - Game previews, film cards, and insights (Pro API)
- `players` - Player information and statistics (Pro API)
- `pro_games` - Game information and statistics (Pro API)
- `schedules` - Game schedules and rankings (Pro API)
- `teams` - Team rosters and schedules (Pro API)

**Tests:**
- `test_sub_sdk_accessible[{sdk_name}]` - Verifies each sub-SDK:
  - Can be accessed as an attribute
  - Returns the correct class type
  - Comes from the expected module path
- `test_sub_sdk_can_be_accessed_multiple_times[{sdk_name}]` - Verifies:
  - Multiple accesses return the same instance (lazy loading works correctly)

### 2. TestEndpointsMethodAccessibility (12 tests)

Verifies that specific methods exist on each sub-SDK and are callable.

**Tests for each sub-SDK:**
- Checks for existence of sync methods (e.g., `get_profiles()`)
- Checks for existence of async methods (e.g., `get_profiles_async()`)
- Verifies methods are callable

**Example methods tested:**
- `combine.get_profiles()`, `combine.get_rankings()`
- `draft.get_picks_report()`, `draft.get_teamneeds()`
- `games.get_games()`, `games.get_box_score()`, `games.get_play_by_play()`
- `content.get_home_film_cards()`, `content.get_coaches_film_videos()`
- `players.get_player()`, `players.search_players()`
- And many more...

### 3. TestStatsEndpointsMethodAccessibility (6 tests)

Verifies that stats-related endpoints sub-SDKs are accessible.

**Stats Sub-SDKs Tested:**
- `player_passing_stats` - Player passing statistics
- `player_receiving_stats` - Player receiving statistics (with fallback handling)
- `player_rushing_stats` - Player rushing statistics
- `player_defense_stats` - Player defense statistics
- `team_offense_stats` - Team offensive statistics
- `team_defense_stats` - Team defensive statistics

### 4. TestMethodSignatures (5 tests)

Verifies that methods have appropriate signatures with standard parameters.

**Tests:**
- `test_sync_methods_accept_required_parameters` - Sync methods accept request parameters
- `test_async_methods_accept_required_parameters` - Async methods accept request parameters
- `test_methods_accept_retry_config` - Methods accept `retries` parameter
- `test_methods_accept_server_url_override` - Methods accept `server_url` parameter
- `test_methods_accept_timeout_override` - Methods accept `timeout_ms` parameter

### 5. TestSubSDKInheritance (3 tests)

Verifies proper inheritance hierarchy of sub-SDKs.

**Tests:**
- `test_regular_endpoints_inherit_from_base_sdk` - Regular API endpoints inherit from `BaseSDK`
- `test_pro_endpoints_inherit_from_pro_sdk` - Pro API endpoints inherit from `ProSDK`
- `test_pro_sdk_inherits_from_base_sdk` - `ProSDK` itself inherits from `BaseSDK`

### 6. TestMixinMethods (1 test)

Verifies that mixin methods are properly accessible on sub-SDKs.

**Tests:**
- `test_pro_games_has_mixin_methods` - ProGames has methods from:
  - `GameContentMixin` (e.g., `get_game_preview()`, `get_game_insights()`)
  - `GameScheduleMixin` (e.g., `get_scheduled_game()`, `get_game_matchup_rankings()`)

## Running the Tests

### Run all integration tests:
```bash
pytest tests/test_nfl/unit/test_sdk_integration.py -v
```

### Run a specific test class:
```bash
pytest tests/test_nfl/unit/test_sdk_integration.py::TestEndpointsSubSDKAccess -v
```

### Run a specific test:
```bash
pytest tests/test_nfl/unit/test_sdk_integration.py::TestEndpointsSubSDKAccess::test_sub_sdk_accessible -v
```

## Test Fixtures

### `nfl_sdk`

Creates a properly configured GriddyNFL instance for testing with:
- Mock NFL API credentials
- Mock authentication tokens
- No actual network calls

## What These Tests Verify

✅ **Sub-SDK Registration** - All endpoint sub-SDKs are properly registered in `_sub_sdk_map`

✅ **Lazy Loading** - Sub-SDKs are loaded on first access and cached for subsequent accesses

✅ **Type Correctness** - Each sub-SDK is the correct class type from the correct module

✅ **Method Accessibility** - All expected methods exist on sub-SDKs and are callable

✅ **Dual Execution** - Both sync and async methods are available

✅ **Standard Parameters** - Methods accept retry config, server URL override, and timeout settings

✅ **Inheritance Hierarchy** - Sub-SDKs properly inherit from base classes

✅ **Mixin Composition** - Mixin methods are properly accessible on sub-SDKs

## Benefits

1. **Catches Breaking Changes** - Detects if sub-SDKs are accidentally removed or renamed
2. **Verifies SDK Structure** - Ensures the SDK maintains its expected API surface
3. **Documents SDK Usage** - Serves as documentation for what sub-SDKs and methods are available
4. **Prevents Regressions** - Catches issues when refactoring sub-SDK registration or lazy loading
5. **Fast Execution** - All tests are unit tests with no network calls (runs in ~5 seconds)

## Maintenance

When adding new endpoint sub-SDKs:

1. Add the sub-SDK to the `ENDPOINTS_SUB_SDKS` dictionary in `TestEndpointsSubSDKAccess`
2. Add a corresponding test method in `TestEndpointsMethodAccessibility`
3. If it's a stats endpoint, add it to `TestStatsEndpointsMethodAccessibility`

## Test Results

All 51 tests pass successfully, verifying complete integration between GriddyNFL and the endpoints package.

```
51 passed, 1 warning in 4.67s
```

---

**Created**: 2025-11-13
**SDK Version**: 0.4.0
