# Griddy SDK Documentation

Welcome to the Griddy SDK documentation! Griddy is a Python SDK for accessing NFL data from multiple sources.

## Overview

Griddy SDK provides a unified, type-safe interface for accessing NFL data, including:

- **NFL.com Integration** - Access current season data, live scores, and player information
- **Next Gen Stats** - Advanced player tracking statistics and analytics
- **Pro API** - Betting odds, player projections, and advanced statistics

## Key Features

- **Type Safety** - Full type hints and Pydantic models for data validation
- **Async Support** - Both synchronous and asynchronous APIs
- **Rate Limiting** - Built-in request throttling to respect API limits
- **Error Handling** - Comprehensive exception handling and retry logic
- **Lazy Loading** - Sub-SDKs are loaded on demand for fast startup

## Quick Example

```python
from griddy.nfl import GriddyNFL

# Initialize with authentication
nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})

# Access games data
games = nfl.games.get_games(season=2024, season_type="REG")

# Access Next Gen Stats
passing_stats = nfl.ngs.stats.get_passing_stats(season=2024, week=1)

# Access player statistics
player_stats = nfl.stats.passing.get_passing_stats(season=2024)
```

## Requirements

- Python 3.13 or higher
- NFL.com account for authentication

## Installation

```bash
pip install griddy
```

For development:

```bash
git clone https://github.com/jkgriebel93/griddy-sdk-python.git
cd griddy-sdk-python
pip install -e ".[dev,docs]"
```

## Getting Help

- **Documentation** - You're reading it!
- **Issues** - [GitHub Issues](https://github.com/jkgriebel93/griddy-sdk-python/issues)
- **Source Code** - [GitHub Repository](https://github.com/jkgriebel93/griddy-sdk-python)

## License

This project is licensed under the MIT License.
