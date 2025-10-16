# NFL SDK Endpoint Tests

This directory contains comprehensive endpoint tests for all NFL SDK modules. These tests ensure API functionality, parameter validation, error handling, and response schema validation.

## Overview

This testing suite is part of issue [#25](https://github.com/jkgriebel93/griddy-sdk-python/issues/25) - implementing comprehensive endpoint tests for all 30 NFL SDK endpoint modules.

## Directory Structure

```
test_endpoints/
├── README.md                    # This file
├── conftest.py                  # Shared fixtures and helpers
├── player_stats/                # Player statistics endpoint tests
│   ├── __init__.py
│   ├── test_player_statistics.py
│   ├── test_player_passing_statistics.py
│   ├── test_player_receiving_statistics.py
│   ├── test_player_rushing_statistics.py
│   └── test_players.py
├── team_stats/                  # Team statistics endpoint tests
│   ├── __init__.py
│   ├── test_team_defense_statistics.py
│   ├── test_team_defense_pass_statistics.py
│   ├── test_team_defense_rush_statistics.py
│   ├── test_team_offense_overview_statistics.py
│   ├── test_team_offense_pass_statistics.py
│   └── test_teams.py
├── defensive_stats/             # Defensive statistics endpoint tests
│   ├── __init__.py
│   ├── test_defensive_statistics.py
│   ├── test_defensive_player_overview.py
│   └── test_defensive_pass_rush_statistics.py
├── schedules_scores/            # Schedule and score endpoint tests
│   ├── __init__.py
│   ├── test_schedules.py
│   ├── test_schedules_extended.py
│   ├── test_season_schedule.py
│   └── test_scores.py
├── game_data/                   # Game data endpoint tests
│   ├── __init__.py
│   ├── test_football.py
│   ├── test_plays.py
│   └── test_win_probability.py
├── content_media/               # Content and media endpoint tests
│   ├── __init__.py
│   ├── test_content_sdk.py
│   ├── test_content_insights.py
│   ├── test_filmroom.py
│   └── test_secured_videos.py
└── other/                       # Other endpoint tests
    ├── __init__.py
    ├── test_authentication.py
    ├── test_betting.py
    ├── test_experience.py
    ├── test_fantasy_statistics.py
    └── test_stats_sdk.py
```

## Running Tests

### Run All Endpoint Tests
```bash
pytest tests/test_nfl/test_endpoints/
```

### Run Tests for Specific Category
```bash
# Player statistics tests
pytest tests/test_nfl/test_endpoints/player_stats/

# Team statistics tests
pytest tests/test_nfl/test_endpoints/team_stats/

# Defensive statistics tests
pytest tests/test_nfl/test_endpoints/defensive_stats/
```

### Run Tests for Specific Module
```bash
pytest tests/test_nfl/test_endpoints/player_stats/test_player_statistics.py
```

### Run Tests with Coverage
```bash
pytest tests/test_nfl/test_endpoints/ --cov=src/griddy/nfl --cov-report=html
```

### Run Tests with Markers
```bash
# Run only endpoint tests
pytest -m endpoint

# Run only player stats tests
pytest -m player_stats

# Run only integration tests
pytest -m integration

# Exclude slow tests
pytest -m "not slow"
```

## Writing Endpoint Tests

### Test File Template

Each endpoint test file should follow this structure:

```python
"""
Tests for [ModuleName] endpoint module.
Related to issue #[issue_number].
"""

import pytest
from unittest.mock import Mock, patch
from griddy.nfl.[module_name] import [ClassName]


@pytest.mark.endpoint
@pytest.mark.[category_marker]
class Test[ClassName]:
    """Test suite for [ClassName] endpoint methods."""

    @pytest.fixture
    def [module_instance](self, mock_sdk_configuration):
        """Create a [ClassName] instance with mock configuration."""
        return [ClassName](mock_sdk_configuration)

    def test_initialization(self, [module_instance], mock_sdk_configuration):
        """Test [ClassName] initialization."""
        assert [module_instance].sdk_configuration == mock_sdk_configuration

    @patch('griddy.nfl.[module_name].[ClassName].do_request')
    def test_[method_name]_success(
        self,
        mock_do_request,
        [module_instance],
        mock_http_response
    ):
        """Test successful [method] call."""
        # Arrange
        mock_http_response.json = Mock(return_value=[...])
        mock_do_request.return_value = mock_http_response

        # Act
        result = [module_instance].[method_name](...)

        # Assert
        assert result is not None
        # Add specific assertions
```

### Required Test Cases

Each endpoint module should include tests for:

1. **Initialization**
   - Verify SDK configuration is properly set
   - Check instance attributes

2. **Successful Requests**
   - Test happy path scenarios
   - Verify correct data is returned
   - Validate response structure

3. **Parameter Validation**
   - Test required parameters
   - Test optional parameters
   - Test parameter type validation
   - Test parameter value ranges

4. **Error Handling**
   - Test 4XX errors (client errors)
   - Test 5XX errors (server errors)
   - Test network errors
   - Test timeout scenarios

5. **Response Validation**
   - Verify response schema matches expected models
   - Test data type conversions
   - Test null/empty responses

6. **Authentication**
   - Verify security headers are included
   - Test with valid/invalid credentials

7. **Rate Limiting**
   - Test 429 responses
   - Verify retry logic

8. **Edge Cases**
   - Test boundary values
   - Test special characters in parameters
   - Test pagination edge cases

## Available Fixtures

### Mock Configuration
- `mock_sdk_configuration`: Mocked SDK configuration with client, security, etc.
- `mock_httpx_client`: Mocked httpx client for HTTP requests
- `mock_http_response`: Successful HTTP response mock
- `mock_error_response`: Error HTTP response mock

### Sample Data
- `sample_player_stats`: Example player statistics data
- `sample_team_stats`: Example team statistics data
- `sample_game_schedule`: Example game schedule data
- `sample_defensive_stats`: Example defensive statistics data
- `sample_betting_odds`: Example betting odds data

### Helpers
- `mock_sdk_helper`: Helper class for common mocking patterns
- `create_mock_response()`: Function to create custom mock responses

## Markers

Use pytest markers to categorize tests:

- `@pytest.mark.endpoint`: Mark as endpoint test
- `@pytest.mark.player_stats`: Player statistics tests
- `@pytest.mark.team_stats`: Team statistics tests
- `@pytest.mark.defensive_stats`: Defensive statistics tests
- `@pytest.mark.schedules`: Schedule endpoint tests
- `@pytest.mark.game_data`: Game data tests
- `@pytest.mark.content`: Content/media tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.slow`: Slow-running tests

## Best Practices

1. **Use Descriptive Test Names**
   - Test names should clearly describe what is being tested
   - Use format: `test_[method]_[scenario]`

2. **Follow AAA Pattern**
   - Arrange: Set up test data and mocks
   - Act: Execute the method under test
   - Assert: Verify expected outcomes

3. **Mock External Dependencies**
   - Always mock HTTP requests
   - Mock SDK configuration
   - Don't make real API calls in unit tests

4. **Test One Thing at a Time**
   - Each test should verify a single behavior
   - Keep tests focused and simple

5. **Use Parametrize for Similar Tests**
   - Use `@pytest.mark.parametrize` for testing multiple inputs
   - Reduces code duplication

6. **Document Complex Tests**
   - Add docstrings explaining test purpose
   - Comment non-obvious test setup

7. **Keep Tests Fast**
   - Mock slow operations
   - Use fixtures efficiently
   - Mark slow tests with `@pytest.mark.slow`

## Example Test Implementation

See `player_stats/test_player_statistics.py` for a complete example implementation demonstrating:
- Proper test structure
- Mocking patterns
- Parameter validation
- Error handling
- Async test support

## Related Issues

- [#25](https://github.com/jkgriebel93/griddy-sdk-python/issues/25) - Main epic for endpoint tests
- [#26-#55](https://github.com/jkgriebel93/griddy-sdk-python/issues/) - Individual module test issues

## Contributing

When implementing tests for a new module:

1. Create test file in appropriate subdirectory
2. Follow the template and patterns from example tests
3. Implement all required test cases
4. Run tests locally and ensure they pass
5. Update this README if adding new patterns or fixtures
6. Reference the related issue number in test docstrings

## CI/CD Integration

These tests are automatically run in CI/CD pipeline:
- On every pull request
- Before merging to main branch
- Coverage reports are generated and tracked
- Tests must pass before code can be merged
