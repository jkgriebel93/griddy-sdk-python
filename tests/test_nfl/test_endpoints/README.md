# NFL SDK Endpoint Tests

This directory contains unit tests for all NFL SDK endpoint modules, created as part of GitHub issue #25.

## Test Structure

The tests are organized by category:

```
test_endpoints/
├── conftest.py              # Shared fixtures and utilities
├── player_stats/           # Player statistics endpoints (#26-#30)
├── team_stats/             # Team statistics endpoints (#31-#36)
├── defensive_stats/        # Defensive statistics endpoints (#37-#39)
├── schedules_scores/       # Schedule and score endpoints (#40-#43)
├── game_data/              # Game data endpoints (#44-#46)
├── content_media/          # Content and media endpoints (#47-#50)
└── other/                  # Other endpoints (#51-#55)
```

## Current Status

✅ **Completed:**
- Created test skeleton files for all 30 endpoint modules
- Set up comprehensive fixture system in conftest.py
- Configured pytest with appropriate markers (endpoint, unit, asyncio)
- All synchronous test cases pass (using TODO placeholders)
- Tests can be collected and run successfully

⚠️ **Known Issues:**
- Async tests are currently failing due to pytest-asyncio plugin not loading correctly
- This appears to be a configuration issue that needs further investigation
- Synchronous tests work fine and can be used as the primary testing approach

## Running Tests

### Run all tests (without coverage)
```bash
pytest tests/test_nfl/test_endpoints/ -o addopts=""
```

### Run specific category
```bash
pytest tests/test_nfl/test_endpoints/player_stats/ -o addopts=""
```

### Run specific test file
```bash
pytest tests/test_nfl/test_endpoints/player_stats/test_player_statistics.py -o addopts=""
```

### Collect tests without running
```bash
pytest tests/test_nfl/test_endpoints/ --collect-only -o addopts=""
```

## Test Implementation Guide

Each test file contains skeleton tests with TODO comments. To implement:

1. Import the actual endpoint module
2. Review the endpoint's methods in the source code
3. Replace TODO comments with actual test logic
4. Use the fixtures from conftest.py for mocking
5. Follow the patterns established in test_player_statistics.py

## Fixtures Available

The `conftest.py` file provides extensive fixtures:

- **SDK Configuration:** `mock_sdk_configuration`, `mock_base_sdk`
- **HTTP Responses:** `mock_http_response`, `mock_error_response`, `mock_not_found_response`, `mock_rate_limit_response`
- **Sample Data:** Various sample data fixtures for each endpoint category
- **Helpers:** `mock_response_factory`, `assertion_helpers`

## Next Steps

1. Fix async test configuration issue
2. Implement actual test logic for each endpoint
3. Add integration tests for real API calls (marked with @pytest.mark.integration)
4. Add performance tests for critical endpoints (marked with @pytest.mark.slow)

## Related Issues

- Main issue: #25 - Implement comprehensive endpoint tests
- Sub-issues: #26-#55 - Individual module test implementation