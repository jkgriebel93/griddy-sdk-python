# Griddy SDK

A Python SDK for accessing NFL data from multiple sources including NFL.com, with other sources to come.

See the full documentation [here](https://jkgriebel93.github.io/griddy-docs/).

## Features

- **Unified API**: Single interface for multiple NFL data sources
- **Type Safety**: Full type hints with Pydantic models
- **Async Support**: Both sync and async methods for all endpoints
- **Lazy Loading**: Sub-SDKs load on demand for fast startup
- **Comprehensive Data**: Player stats, game schedules, rosters, Next Gen Stats, and more

## Requirements

- Python 3.14+

## Installation

```bash
pip install griddy
```

For development:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from griddy.nfl import GriddyNFL

# Initialize with authentication
nfl = GriddyNFL(
    login_email="your_email@example.com",
    login_password="your_password"
)

# Or use an existing auth token
nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})

# Get game schedules
games = nfl.games.get_games(season=2024, week=1)

# Get player passing stats
passing_stats = nfl.stats.passing.get_passing_stats_by_season(season=2024)

# Get Next Gen Stats
ngs_passing = nfl.ngs.stats.get_passing_stats(season=2024, season_type="REG")
```

## API Categories

### Regular API

Public NFL.com endpoints for core football data:

```python
# Games and schedules
games = nfl.games.get_games(season=2024, week=1)

# Team rosters
rosters = nfl.rosters.get_rosters(team_id="SF", season=2024)

# Standings
standings = nfl.standings.get_standings(season=2024)

# NFL Draft
draft_picks = nfl.draft.get_draft_picks(season=2024)

# NFL Combine
combine_results = nfl.combine.get_combine_results(season=2024)
```

### Pro API

Advanced statistics and analytics:

```python
# Player statistics
passing = nfl.stats.passing.get_passing_stats_by_season(season=2024)
rushing = nfl.stats.rushing.get_rushing_stats_by_season(season=2024)
receiving = nfl.stats.receiving.get_receiving_stats_by_season(season=2024)
defense = nfl.stats.defense.get_defensive_stats_by_season(season=2024)

# Team statistics
team_offense = nfl.stats.team_offense.get_team_offense_stats_by_season(season=2024)
team_defense = nfl.stats.team_defense.get_team_defense_stats_by_season(season=2024)

# Betting odds
betting = nfl.betting.get_odds(game_id="2024091500")

# Player information
player = nfl.players.get_player(player_id="46101")

# Transactions
transactions = nfl.transactions.get_transactions(season=2024)
```

### Next Gen Stats (NGS)

Player tracking data and advanced analytics:

```python
# Stats
passing = nfl.ngs.stats.get_passing_stats(season=2024, season_type="REG")
rushing = nfl.ngs.stats.get_rushing_stats(season=2024, season_type="REG")
receiving = nfl.ngs.stats.get_receiving_stats(season=2024, season_type="REG")

# Weekly stats
weekly_passing = nfl.ngs.stats.get_passing_stats(
    season=2024, season_type="REG", week=12
)

# Leaders
fastest_carriers = nfl.ngs.leaders.get_fastest_ball_carriers(
    season=2024, season_type="REG", limit=10
)
longest_plays = nfl.ngs.leaders.get_longest_plays(
    season=2024, season_type="REG", limit=10
)

# League info
schedule = nfl.ngs.league.get_schedule(season=2024)
teams = nfl.ngs.league.get_teams()

# Content
charts = nfl.ngs.content.get_charts(season=2024)
highlights = nfl.ngs.content.get_highlights(season=2024)
```

## Async Support

All endpoints have async versions:

```python
import asyncio
from griddy.nfl import GriddyNFL

async def main():
    nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})

    # Use async methods
    games = await nfl.games.get_games_async(season=2024, week=1)
    stats = await nfl.ngs.stats.get_passing_stats_async(
        season=2024, season_type="REG"
    )

asyncio.run(main())
```

## Context Manager

Use as a context manager for automatic resource cleanup:

```python
with GriddyNFL(nfl_auth=auth) as nfl:
    games = nfl.games.get_games(season=2024)
# Resources automatically cleaned up
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/jkgriebel93/griddy-sdk-python.git
cd griddy-sdk-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/griddy --cov-report=html

# Run specific tests
pytest tests/test_nfl/test_endpoints/
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

### Documentation

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Documentation

Full documentation is available at [https://jkgriebel93.github.io/griddy-sdk-python](https://jkgriebel93.github.io/griddy-sdk-python)


## Contact

John Griebel - john@thistlegrow.com

## Disclaimer

This software is intended for personal, non-commercial use only. Users are responsible for ensuring their use complies with all applicable terms of service and laws. Do not use this software for any malicious, harmful, or unauthorized purposes.

This project is not affiliated with, endorsed by, or officially connected to the National Football League (NFL), NFL Enterprises LLC, or any of their subsidiaries or affiliates. All NFL-related trademarks, logos, and data are the property of their respective owners.
