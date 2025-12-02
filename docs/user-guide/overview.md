# User Guide Overview

This guide provides comprehensive information about using the Griddy SDK to access NFL data.

## SDK Architecture

The Griddy SDK is organized into a hierarchical structure:

```
griddy/
├── core/           # Shared base functionality
│   ├── BaseClient  # HTTP client with rate limiting
│   ├── exceptions  # Custom exception classes
│   └── models      # Base Pydantic models
│
└── nfl/            # NFL-specific SDK
    ├── GriddyNFL   # Main entry point
    ├── endpoints/  # API endpoint implementations
    │   ├── regular/    # NFL.com public API
    │   ├── pro/        # NFL Pro API (advanced stats)
    │   └── ngs/        # Next Gen Stats API
    └── models/     # NFL data models
```

## Key Concepts

### Lazy Loading

Sub-SDKs are loaded on demand to minimize startup time:

```python
from griddy.nfl import GriddyNFL

nfl = GriddyNFL(nfl_auth=auth_info)

# 'games' sub-SDK is loaded only when first accessed
games = nfl.games.get_games(season=2024)

# Subsequent accesses reuse the loaded instance
more_games = nfl.games.get_games(season=2023)
```

### Pydantic Models

All API responses are validated and parsed into Pydantic models:

```python
# Response data is automatically validated
games = nfl.games.get_games(season=2024)

# Access typed attributes
for game in games.games:
    print(game.home_team.abbreviation)  # str
    print(game.game_time)               # datetime
    print(game.week)                    # int
```

### Sync and Async APIs

Most endpoints support both synchronous and asynchronous calls:

```python
# Synchronous
games = nfl.games.get_games(season=2024)

# Asynchronous
games = await nfl.games.get_games_async(season=2024)
```

## API Structure

The NFL SDK provides access to three main API categories:

### Regular API

Public NFL.com endpoints:

- **games** - Game schedules, scores, and details
- **rosters** - Team rosters and player assignments
- **standings** - Division and conference standings
- **football_teams** - Team information
- **venues** - Stadium details
- **weeks** - Season week information
- **combine** - NFL Combine data
- **draft** - Draft picks and information

### Pro API

NFL Pro subscription endpoints with advanced data:

- **stats** - Aggregated statistics (passing, rushing, receiving, etc.)
- **players** - Detailed player profiles and projections
- **pro_games** - Advanced game data
- **schedules** - Matchup rankings and injury reports
- **betting** - Odds and betting lines
- **content** - Game previews and film cards
- **teams** - Pro team information
- **transactions** - Player transactions

### Next Gen Stats (NGS)

Player tracking and advanced analytics:

- **ngs.league** - League-wide schedules and data
- **ngs.games** - Game center and live data
- **ngs.stats** - Player tracking statistics
- **ngs.leaders** - Leaderboards
- **ngs.content** - Charts and highlights
- **ngs.news** - Articles and videos

## Common Patterns

### Filtering by Season and Week

Most endpoints accept `season` and `week` parameters:

```python
# Get data for a specific week
games = nfl.games.get_games(season=2024, week=1, season_type="REG")

# Get data for entire season
season_stats = nfl.stats.passing.get_passing_stats(season=2024)
```

### Season Types

Use the `season_type` parameter to specify:

| Value | Description |
|-------|-------------|
| `"PRE"` | Preseason |
| `"REG"` | Regular season |
| `"POST"` | Postseason/Playoffs |

### Pagination

Some endpoints return paginated results:

```python
# First page
results = nfl.players.get_players(limit=50, offset=0)

# Next page
more_results = nfl.players.get_players(limit=50, offset=50)
```

## Best Practices

### Use Context Managers

Ensure proper resource cleanup:

```python
with GriddyNFL(nfl_auth=auth_info) as nfl:
    games = nfl.games.get_games(season=2024)
# HTTP clients are automatically closed
```

### Handle Errors Gracefully

Always implement error handling:

```python
from griddy import GriddyError, RateLimitError
import time

try:
    games = nfl.games.get_games(season=2024)
except RateLimitError as e:
    time.sleep(e.retry_after or 60)
    games = nfl.games.get_games(season=2024)
except GriddyError as e:
    logger.error(f"API error: {e.message}")
```

### Cache Responses

For frequently accessed data, implement caching:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_team_info(team_abbr: str):
    return nfl.football_teams.get_team(team_abbr)
```

### Respect Rate Limits

Don't overwhelm the API with requests:

```python
import time

for week in range(1, 18):
    games = nfl.games.get_games(season=2024, week=week)
    time.sleep(1)  # Wait between requests
```

## What's Next

- [NFL Data Guide](nfl.md) - Detailed NFL endpoint documentation
- [Error Handling](error-handling.md) - Comprehensive error handling
- [Configuration](configuration.md) - SDK configuration options
- [API Reference](../api/index.md) - Complete API documentation
