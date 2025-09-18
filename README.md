# Griddy SDK

A Python SDK for accessing sports data from multiple sources including NFL.com, Pro Football Reference, ESPN, and Pro Football Focus.

## Features

- 🏈 **NFL.com Integration** - Access current season data, live scores, and player information
- 📊 **Pro Football Reference** - Historical statistics, career data, and advanced metrics
- 📺 **ESPN Integration** - Live scores, news, team rosters, and real-time updates
- 🎯 **Pro Football Focus** - Advanced player grades, analytics, and performance metrics
- 🔧 **Unified Interface** - Consistent API across all data sources
- ⚡ **Rate Limiting** - Built-in request throttling to respect API limits
- 🛡️ **Error Handling** - Comprehensive exception handling and retry logic
- 📝 **Type Safety** - Full type hints and Pydantic models for data validation

## Requirements

- Python 3.13 or higher

## Installation

```bash
pip install griddy
```

### Development Installation

```bash
git clone https://github.com/jkgriebel93/griddy-sdk.git
cd griddy-sdk
pip install -e ".[dev]"
```

## Quick Start

### NFL.com Data

```python
from griddy import nfl

# Initialize client
client = nfl.Client()

# Get games for current week
games = client.get_games(season=2024, week=1)
for game in games:
    print(f"{game.away_team} @ {game.home_team}: {game.status}")

# Get team information
teams = client.get_teams()
for team in teams[:5]:
    print(f"{team.name} ({team.abbreviation})")

# Get player statistics
stats = client.get_player_stats("player_id", season=2024, week=1)
for stat in stats:
    print(f"Week {stat.week}: {stat.passing_yards} passing yards")
```

### Pro Football Reference Data

```python
from griddy import pfr

# Initialize client
client = pfr.Client()

# Search for players
players = client.search_players("Brady", position="QB")
for player in players:
    print(f"{player.name} - {player.position}")

# Get career statistics
career_stats = client.get_player_career_stats("player_id")
if career_stats:
    print(f"Career passing yards: {career_stats.career_totals.pass_yards}")

# Get draft information
draft_picks = client.get_draft_class(2023)
first_round = [p for p in draft_picks if p.round == 1]
for pick in first_round[:5]:
    print(f"{pick.pick}. {pick.player_name} - {pick.team}")
```

### ESPN Data

```python
from griddy import espn

# Initialize client
client = espn.Client()

# Get current scoreboard
scoreboard = client.get_scoreboard()
print(f"Games on {scoreboard.date}: {len(scoreboard.games)}")

# Get live scores
live_games = client.get_live_scores()
for game in live_games:
    print(f"{game.away_team} {game.away_score} - {game.home_score} {game.home_team}")

# Get team roster
roster = client.get_team_roster("team_id")
quarterbacks = [p for p in roster if p.position == "QB"]
for qb in quarterbacks:
    print(f"#{qb.jersey_number} {qb.name}")

# Get news
news = client.get_news(limit=5)
for article in news:
    print(f"{article.headline} - {article.published}")
```

### Pro Football Focus Data

```python
from griddy import pff

# Initialize client (with optional API key)
client = pff.Client(api_key="your_pff_api_key")

# Get player grades
grades = client.get_player_grades("player_id", season=2024, week=1)
print(f"Overall Grade: {grades.overall_grade}")
print(f"Pass Rush Grade: {grades.defense.pass_rush_grade}")

# Get position rankings
qb_rankings = client.get_position_rankings("QB", season=2024, limit=10)
for i, qb in enumerate(qb_rankings, 1):
    print(f"{i}. {qb.player_id}: {qb.overall_grade}")

# Get team grades
team_grades = client.get_team_grades("KC", season=2024)
print(f"Offense: {team_grades.overall_offense_grade}")
print(f"Defense: {team_grades.overall_defense_grade}")

# Get draft prospects
prospects = client.get_draft_board(2024, limit=10)
for prospect in prospects:
    print(f"{prospect.name} - {prospect.position} ({prospect.pff_grade})")
```

## Module Overview

### Core Module (`griddy.core`)

The core module provides shared functionality:

- **BaseClient**: HTTP client with rate limiting and error handling
- **Exceptions**: Custom exception classes for different error types
- **Models**: Base data models and common structures
- **Utils**: Utility functions for data parsing and validation

### NFL Module (`griddy.nfl`)

Access NFL.com data:

- Current season games and scores
- Team information and rosters
- Player statistics and profiles
- Schedule and standings
- News and updates

### PFR Module (`griddy.pfr`)

Access Pro Football Reference data:

- Historical player statistics
- Career summaries and advanced metrics
- Draft information and analysis
- Team statistics by season
- Hall of Fame data

### ESPN Module (`griddy.espn`)

Access ESPN data:

- Live scores and real-time updates
- Team rosters and player profiles
- News articles and analysis
- Detailed game information
- Standings and schedules

### PFF Module (`griddy.pff`)

Access Pro Football Focus data:

- Player grades and rankings by position
- Advanced analytics and metrics
- Team performance evaluations
- Draft prospect analysis and rankings
- Injury reports and analysis
- All-Pro teams and awards
- Pass rush and coverage statistics

## Configuration

### Rate Limiting

All clients support rate limiting configuration:

```python
from griddy import nfl

client = nfl.Client(
    rate_limit_delay=2.0,  # 2 second delay between requests
    max_retries=5,         # Retry failed requests up to 5 times
    timeout=60             # 60 second request timeout
)
```

### Custom Headers

Add custom headers to requests:

```python
from griddy import espn

client = espn.Client(
    headers={
        "Custom-Header": "custom-value",
        "User-Agent": "My App/1.0"
    }
)
```

## Error Handling

The SDK provides comprehensive error handling:

```python
from griddy import nfl
from griddy.core.exceptions import GriddyError, RateLimitError, NotFoundError

client = nfl.Client()

try:
    games = client.get_games(season=2024, week=1)
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after} seconds")
except NotFoundError as e:
    print(f"Resource not found: {e.message}")
except GriddyError as e:
    print(f"API error: {e.message} (Status: {e.status_code})")
```

## Data Models

All data is returned as typed Pydantic models:

```python
from griddy.nfl.models import NFLGame

# Games have structured data
game: NFLGame = client.get_games(season=2024, week=1)[0]

# Access with full type safety
print(game.home_team)      # str
print(game.home_score)     # Optional[int]
print(game.start_time)     # Optional[datetime]
print(game.status)         # str
```

## Examples

Check the `examples/` directory for comprehensive usage examples:

- `examples/nfl_example.py` - NFL.com data access
- `examples/pfr_example.py` - Pro Football Reference usage
- `examples/espn_example.py` - ESPN data integration
- `examples/pff_example.py` - Pro Football Focus analytics

Run examples:

```bash
python examples/nfl_example.py
python examples/pfr_example.py
python examples/espn_example.py
python examples/pff_example.py
```

## Development

### Setup

```bash
git clone https://github.com/jkgriebel93/griddy-sdk.git
cd griddy-sdk
pip install -e ".[dev]"
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/griddy --cov-report=html

# Run specific module tests
pytest tests/test_nfl/
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

## API Limitations

### NFL.com
- No official public API - implementation would require web scraping
- Rate limiting recommended for respectful usage
- Data availability may vary

### Pro Football Reference
- No official API - requires web scraping
- Respectful rate limiting is essential
- Historical data coverage is extensive

### ESPN
- Public API available for some endpoints
- Rate limits apply
- Live data may require special access

### Pro Football Focus
- Premium subscription-based API
- API key required for authenticated requests
- Advanced analytics and proprietary grades
- Comprehensive draft and player evaluation data

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`pytest`)
6. Run code quality checks (`black`, `isort`, `flake8`, `mypy`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This SDK is for educational and personal use. When accessing data from sports websites:

- Respect robots.txt and terms of service
- Implement appropriate rate limiting
- Don't overload servers with requests
- Consider the ethical implications of web scraping
- Some data sources may require permission for commercial use

The authors are not responsible for how this SDK is used. Always verify that your usage complies with the terms of service of the data sources you're accessing.

## Support

- 📖 [Documentation](https://github.com/jkgriebel93/griddy-sdk/wiki)
- 🐛 [Issue Tracker](https://github.com/jkgriebel93/griddy-sdk/issues)
- 💬 [Discussions](https://github.com/jkgriebel93/griddy-sdk/discussions)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.