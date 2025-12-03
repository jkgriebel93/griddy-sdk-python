# NFL Data Guide

This guide covers all available NFL data endpoints and how to use them effectively.

## Getting Started

```python
from griddy.nfl import GriddyNFL

# Initialize the client
nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})
```

## Regular API Endpoints

These endpoints access NFL.com's public API.

### Games

Access game schedules, scores, and details.

```python
# Get games for a specific week
games = nfl.games.get_games(
    season=2024,
    season_type="REG",
    week=1
)

# Access game details
for game in games.games:
    print(f"Game ID: {game.id}")
    print(f"Matchup: {game.away_team.abbreviation} @ {game.home_team.abbreviation}")
    print(f"Status: {game.game_status}")
    print(f"Score: {game.away_score} - {game.home_score}")
```

#### Available Methods

| Method | Description |
|--------|-------------|
| `get_games()` | Get games by season/week |
| `get_game()` | Get specific game by ID |
| `get_games_async()` | Async version of get_games |

### Rosters

Access team rosters and player assignments.

```python
# Get team roster
roster = nfl.rosters.get_roster(
    team_id="SF",
    season=2024
)

for player in roster.players:
    print(f"#{player.jersey_number} {player.display_name} - {player.position}")
```

### Standings

Get division and conference standings.

```python
# Get current standings
standings = nfl.standings.get_standings(season=2024)

for team in standings.teams:
    print(f"{team.full_name}: {team.wins}-{team.losses}")
```

### Teams

Access team information.

```python
# Get all teams
teams = nfl.football_teams.get_teams(season=2024)

for team in teams.teams:
    print(f"{team.full_name}")
    print(f"  Abbreviation: {team.abbreviation}")
    print(f"  Conference: {team.conference}")
    print(f"  Division: {team.division}")
```

### Venues

Get stadium information.

```python
# Get all venues
venues = nfl.venues.get_venues()

for venue in venues.venues:
    print(f"{venue.name} - {venue.city}, {venue.state}")
```

### Combine

Access NFL Combine data.

```python
# Get combine results
combine = nfl.combine.get_combine_data(season=2024)

for player in combine.players:
    print(f"{player.display_name} - {player.position}")
    print(f"  40-yard dash: {player.forty_yard_dash}")
    print(f"  Vertical: {player.vertical_jump}")
```

### Draft

Access draft information.

```python
# Get draft picks
draft = nfl.draft.get_draft(season=2024)

for pick in draft.picks:
    print(f"Round {pick.round}, Pick {pick.pick}: {pick.player_name}")
    print(f"  Team: {pick.team}")
    print(f"  Position: {pick.position}")
```

## Pro API Endpoints

These endpoints provide advanced statistics and data.

### Statistics

The `stats` sub-SDK provides access to various statistical categories:

```python
# Passing statistics
passing = nfl.stats.passing.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1
)

for stat in passing.stats:
    print(f"{stat.player_display_name}")
    print(f"  Attempts: {stat.attempts}")
    print(f"  Completions: {stat.completions}")
    print(f"  Yards: {stat.passing_yards}")
    print(f"  TDs: {stat.passing_touchdowns}")
```

#### Available Stat Categories

| Sub-SDK | Description |
|---------|-------------|
| `stats.passing` | Quarterback passing statistics |
| `stats.rushing` | Running back rushing statistics |
| `stats.receiving` | Receiver statistics |
| `stats.defense` | Defensive statistics |
| `stats.kicking` | Kicker statistics |

### Players

Access detailed player information.

```python
# Get player details
player = nfl.players.get_player(player_id="00-0033873")

print(f"Name: {player.display_name}")
print(f"Position: {player.position}")
print(f"Team: {player.team}")
print(f"Jersey: #{player.jersey_number}")
```

### Schedules

Get matchup rankings and injury reports.

```python
# Get matchup rankings
matchups = nfl.schedules.get_matchup_rankings(
    season=2024,
    week=1
)

for matchup in matchups.matchups:
    print(f"{matchup.away_team} @ {matchup.home_team}")
    print(f"  Spread: {matchup.spread}")
```

### Betting

Access betting odds and lines.

```python
# Get betting odds
odds = nfl.betting.get_odds(
    season=2024,
    week=1
)

for game in odds.games:
    print(f"{game.away_team} @ {game.home_team}")
    print(f"  Spread: {game.spread}")
    print(f"  Over/Under: {game.over_under}")
```

### Content

Get game previews and analysis.

```python
# Get game preview
preview = nfl.content.get_preview(game_id="game_id_here")

print(f"Title: {preview.title}")
print(f"Summary: {preview.summary}")
```

### Transactions

Track player transactions.

```python
# Get recent transactions
transactions = nfl.transactions.get_transactions(
    season=2024,
    limit=50
)

for tx in transactions.transactions:
    print(f"{tx.player_name}: {tx.transaction_type}")
    print(f"  From: {tx.from_team} To: {tx.to_team}")
```

## Next Gen Stats

Access advanced player tracking statistics.

### League Data

```python
# Get league schedule
schedule = nfl.ngs.league.get_schedule(season=2024)

for week in schedule.weeks:
    print(f"Week {week.week}: {len(week.games)} games")
```

### Game Center

```python
# Get game overview
overview = nfl.ngs.games.get_overview(game_id="game_id_here")

print(f"Score: {overview.away_score} - {overview.home_score}")
print(f"Quarter: {overview.quarter}")
```

### Player Statistics

```python
# Get passing stats with advanced metrics
passing = nfl.ngs.stats.get_passing_stats(
    season=2024,
    season_type="REG",
    week=1
)

for stat in passing:
    print(f"{stat.player_display_name}")
    print(f"  Avg Time to Throw: {stat.avg_time_to_throw}s")
    print(f"  Avg Completed Air Yards: {stat.avg_completed_air_yards}")
    print(f"  Aggressiveness: {stat.aggressiveness}%")

# Get rushing stats
rushing = nfl.ngs.stats.get_rushing_stats(
    season=2024,
    season_type="REG"
)

for stat in rushing:
    print(f"{stat.player_display_name}")
    print(f"  Efficiency: {stat.efficiency}")
    print(f"  Expected Rush Yards: {stat.expected_rush_yards}")

# Get receiving stats
receiving = nfl.ngs.stats.get_receiving_stats(
    season=2024,
    season_type="REG"
)

for stat in receiving:
    print(f"{stat.player_display_name}")
    print(f"  Avg Separation: {stat.avg_separation}")
    print(f"  Catch Percentage: {stat.catch_percentage}%")
```

### Leaderboards

```python
# Get leaders for a stat category
leaders = nfl.ngs.leaders.get_leaders(
    season=2024,
    stat_type="passing",
    category="avg_time_to_throw"
)

for i, leader in enumerate(leaders, 1):
    print(f"{i}. {leader.player_display_name}: {leader.value}")
```

### Content (Charts & Highlights)

```python
# Get player charts
charts = nfl.ngs.content.get_charts(player_id="player_id_here")

for chart in charts:
    print(f"Chart: {chart.title}")
    print(f"URL: {chart.url}")

# Get highlights
highlights = nfl.ngs.content.get_highlights(game_id="game_id_here")

for highlight in highlights:
    print(f"{highlight.title}")
    print(f"  Duration: {highlight.duration}")
```

### News

```python
# Get articles
articles = nfl.ngs.news.get_articles(limit=10)

for article in articles:
    print(f"{article.title}")
    print(f"  Published: {article.published_date}")
    print(f"  URL: {article.url}")

# Get videos
videos = nfl.ngs.news.get_videos(limit=10)

for video in videos:
    print(f"{video.title}")
    print(f"  Duration: {video.duration}")
```

## Working with Responses

### Accessing Raw Data

If you need the raw JSON response:

```python
# Most models expose the raw data
response = nfl.games.get_games(season=2024)

# Access the underlying data
raw_data = response.model_dump()
```

### Type Hints

All responses are fully typed for IDE support:

```python
from griddy.nfl.models import GamesResponse, Game

response: GamesResponse = nfl.games.get_games(season=2024)
game: Game = response.games[0]

# IDE will provide autocomplete for all attributes
home_team: str = game.home_team.abbreviation
```

## Next Steps

- [Error Handling](error-handling.md) - Handle API errors
- [Configuration](configuration.md) - Configure the SDK
- [API Reference](../api/nfl.md) - Complete API docs
