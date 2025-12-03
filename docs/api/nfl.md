# NFL Module API Reference

The `griddy.nfl` module provides comprehensive access to NFL data through multiple API endpoints.

## GriddyNFL

The main client class for accessing NFL data.

::: griddy.nfl.sdk.GriddyNFL
    options:
      show_root_heading: true
      members:
        - __init__
        - __enter__
        - __exit__
        - __aenter__
        - __aexit__

### Quick Start

```python
from griddy.nfl import GriddyNFL

# Initialize with auth token
nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})

# Or with email/password
nfl = GriddyNFL(
    login_email="email@example.com",
    login_password="password",
    headless_login=True,
)
```

### Context Manager Usage

```python
# Synchronous
with GriddyNFL(nfl_auth=auth) as nfl:
    games = nfl.games.get_games(season=2024)

# Asynchronous
async with GriddyNFL(nfl_auth=auth) as nfl:
    games = await nfl.games.get_games_async(season=2024)
```

## Available Sub-SDKs

The `GriddyNFL` client provides lazy-loaded access to the following sub-SDKs:

### Regular API Endpoints

| Attribute | Type | Description |
|-----------|------|-------------|
| `authentication` | `Authentication` | Token generation and refresh |
| `combine` | `Combine` | NFL Combine data |
| `draft` | `Draft` | Draft information |
| `games` | `Games` | Game schedules and scores |
| `rosters` | `Rosters` | Team rosters |
| `standings` | `Standings` | League standings |
| `football_teams` | `FootballTeams` | Team information |
| `venues` | `Venues` | Stadium information |
| `weeks` | `Weeks` | Week information |

### Pro API Endpoints

| Attribute | Type | Description |
|-----------|------|-------------|
| `stats` | `StatsSDK` | Aggregated statistics |
| `players` | `Players` | Player information |
| `pro_games` | `ProGames` | Pro game data |
| `schedules` | `Schedules` | Matchup rankings |
| `betting` | `Betting` | Betting odds |
| `content` | `Content` | Game previews |
| `teams` | `Teams` | Pro team info |
| `transactions` | `Transactions` | Player transactions |

### Next Gen Stats

| Attribute | Type | Description |
|-----------|------|-------------|
| `ngs` | `NextGenStats` | Next Gen Stats data |
| `ngs.league` | `League` | League schedules |
| `ngs.games` | `Games` | Game center data |
| `ngs.stats` | `Stats` | Player tracking stats |
| `ngs.leaders` | `Leaders` | Leaderboards |
| `ngs.content` | `Content` | Charts and highlights |
| `ngs.news` | `News` | Articles and videos |

## Games Endpoint

### Methods

```python
# Get games by season and week
games = nfl.games.get_games(
    season=2024,
    season_type="REG",  # PRE, REG, POST
    week=1,
)

# Async version
games = await nfl.games.get_games_async(season=2024, week=1)
```

## Stats Endpoint

The stats endpoint provides access to various statistical categories:

### Passing Statistics

```python
passing = nfl.stats.passing.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1,  # Optional - omit for full season
)
```

### Rushing Statistics

```python
rushing = nfl.stats.rushing.get_rushing_stats(
    season=2024,
    season_type="REG",
)
```

### Receiving Statistics

```python
receiving = nfl.stats.receiving.get_receiving_stats(
    season=2024,
    season_type="REG",
)
```

## Next Gen Stats Endpoint

### NGS Passing Stats

```python
ngs_passing = nfl.ngs.stats.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1,
)

for stat in ngs_passing:
    print(f"{stat.player_display_name}")
    print(f"  Avg Time to Throw: {stat.avg_time_to_throw}s")
    print(f"  Aggressiveness: {stat.aggressiveness}%")
```

### NGS Rushing Stats

```python
ngs_rushing = nfl.ngs.stats.get_rushing_stats(
    season=2024,
    season_type="REG",
)

for stat in ngs_rushing:
    print(f"{stat.player_display_name}")
    print(f"  Efficiency: {stat.efficiency}")
    print(f"  Yards Over Expected: {stat.rush_yards_over_expected}")
```

### NGS Receiving Stats

```python
ngs_receiving = nfl.ngs.stats.get_receiving_stats(
    season=2024,
    season_type="REG",
)

for stat in ngs_receiving:
    print(f"{stat.player_display_name}")
    print(f"  Avg Separation: {stat.avg_separation}")
    print(f"  Catch %: {stat.catch_percentage}%")
```

### NGS Leaders

```python
leaders = nfl.ngs.leaders.get_leaders(
    season=2024,
    stat_type="passing",
    category="avg_time_to_throw",
)
```

## SDK Configuration

::: griddy.nfl.sdkconfiguration.SDKConfiguration
    options:
      show_root_heading: true
      show_source: false

## Retry Configuration

::: griddy.nfl.utils.retries.RetryConfig
    options:
      show_root_heading: true
      show_source: false

## Models

The NFL module includes numerous Pydantic models for type-safe data access. Key model categories:

### Response Models

- `GamesResponse` - Response from games endpoint
- `TeamsResponse` - Response from teams endpoint
- `StandingsResponse` - Response from standings endpoint

### Entity Models

- `Game` - Individual game data
- `Team` - Team information
- `Player` - Player information
- `PlayerStats` - Player statistics

### Request Models

- Various request body models for POST endpoints

## Error Handling

All endpoints may raise:

- `GriddyError` - Base SDK error
- `APIError` - API request failures
- `RateLimitError` - Rate limit exceeded
- `NotFoundError` - Resource not found
- `AuthenticationError` - Auth failures

See [Exceptions](exceptions.md) for details.
