# Quick Start Guide

Get up and running with Griddy SDK in minutes.

## Prerequisites

Before you begin, ensure you have:

1. Python 3.13+ installed
2. Griddy SDK installed (`pip install griddy`)
3. NFL.com authentication credentials (see [Authentication](authentication.md))

## Basic Usage

### Initialize the NFL Client

```python
from griddy.nfl import GriddyNFL

# Option 1: With pre-obtained auth token
auth_info = {
    "accessToken": "your_access_token_here"
}
nfl = GriddyNFL(nfl_auth=auth_info)

# Option 2: With email/password (uses browser authentication)
nfl = GriddyNFL(
    login_email="your_email@example.com",
    login_password="your_password",
    headless_login=True  # Run browser in headless mode
)
```

### Get Games

```python
# Get all games for a specific week
games_response = nfl.games.get_games(
    season=2024,
    season_type="REG",  # Regular season
    week=1
)

for game in games_response.games:
    print(f"{game.away_team.abbreviation} @ {game.home_team.abbreviation}")
```

### Get Team Information

```python
# Get all NFL teams
teams_response = nfl.football_teams.get_teams(season=2024)

for team in teams_response.teams:
    print(f"{team.full_name} ({team.abbreviation})")
```

### Access Player Statistics

```python
# Get passing statistics via the Pro API
passing_stats = nfl.stats.passing.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1
)

for stat in passing_stats.stats:
    print(f"{stat.player_display_name}: {stat.passing_yards} yards")
```

### Access Next Gen Stats

```python
# Get Next Gen Stats passing data
ngs_passing = nfl.ngs.stats.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1
)

for player in ngs_passing:
    print(f"{player.player_display_name}: {player.avg_time_to_throw}s avg time to throw")
```

## Using Context Managers

The SDK supports context managers for automatic resource cleanup:

```python
from griddy.nfl import GriddyNFL

with GriddyNFL(nfl_auth=auth_info) as nfl:
    games = nfl.games.get_games(season=2024)
    # Resources are automatically cleaned up when exiting the context
```

## Async Support

Many endpoints support async operations:

```python
import asyncio
from griddy.nfl import GriddyNFL

async def get_games_async():
    async with GriddyNFL(nfl_auth=auth_info) as nfl:
        games = await nfl.games.get_games_async(season=2024)
        return games

# Run the async function
games = asyncio.run(get_games_async())
```

## Available Sub-SDKs

The `GriddyNFL` client provides access to multiple sub-SDKs:

### Regular API Endpoints

| Sub-SDK | Description | Example |
|---------|-------------|---------|
| `games` | Game schedules and information | `nfl.games.get_games()` |
| `rosters` | Team rosters | `nfl.rosters.get_roster()` |
| `standings` | League standings | `nfl.standings.get_standings()` |
| `football_teams` | Team information | `nfl.football_teams.get_teams()` |
| `venues` | Stadium information | `nfl.venues.get_venues()` |
| `weeks` | Week information | `nfl.weeks.get_weeks()` |
| `combine` | NFL Combine data | `nfl.combine.get_combine_data()` |
| `draft` | Draft information | `nfl.draft.get_draft()` |

### Pro API Endpoints

| Sub-SDK | Description | Example |
|---------|-------------|---------|
| `stats` | Player/team statistics | `nfl.stats.passing.get_passing_stats()` |
| `players` | Player information | `nfl.players.get_player()` |
| `pro_games` | Pro game data | `nfl.pro_games.get_game()` |
| `schedules` | Matchup rankings | `nfl.schedules.get_matchup_rankings()` |
| `betting` | Betting odds | `nfl.betting.get_odds()` |
| `content` | Game previews | `nfl.content.get_preview()` |
| `teams` | Pro team info | `nfl.teams.get_team()` |
| `transactions` | Player transactions | `nfl.transactions.get_transactions()` |

### Next Gen Stats

| Sub-SDK | Description | Example |
|---------|-------------|---------|
| `ngs.league` | League schedules | `nfl.ngs.league.get_schedule()` |
| `ngs.games` | Game center data | `nfl.ngs.games.get_overview()` |
| `ngs.stats` | Player tracking stats | `nfl.ngs.stats.get_passing_stats()` |
| `ngs.leaders` | Leaderboards | `nfl.ngs.leaders.get_leaders()` |
| `ngs.content` | Charts/highlights | `nfl.ngs.content.get_charts()` |
| `ngs.news` | Articles/videos | `nfl.ngs.news.get_articles()` |

## Error Handling

Always wrap API calls in try/except blocks:

```python
from griddy import GriddyError, RateLimitError, NotFoundError

try:
    games = nfl.games.get_games(season=2024, week=1)
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after} seconds")
except NotFoundError as e:
    print(f"Resource not found: {e.message}")
except GriddyError as e:
    print(f"API error: {e.message} (Status: {e.status_code})")
```

## Next Steps

- [Authentication Guide](authentication.md) - Learn about authentication options
- [NFL Data Guide](../user-guide/nfl.md) - Deep dive into NFL endpoints
- [Error Handling](../user-guide/error-handling.md) - Handle errors gracefully
- [API Reference](../api/nfl.md) - Complete API documentation
