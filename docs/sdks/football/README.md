# Football
(*football*)

## Overview

Football API endpoints for games, standings, stats, and venues

### Available Operations

* [get_draft_info](#get_draft_info) - Get Draft Information
* [get_weekly_game_details](#get_weekly_game_details) - Get Weekly Game Details with Standings
* [get_football_games](#get_football_games) - Get Games by Season, Type, and Week
* [get_football_box_score](#get_football_box_score) - Get Game Box Score (Football API)
* [get_play_by_play](#get_play_by_play) - Get Play-by-Play Data
* [get_injury_reports](#get_injury_reports) - Get Injury Reports
* [get_players_team_roster](#get_players_team_roster) - Get Team Roster
* [get_player_details](#get_player_details) - Get Player Details
* [get_standings](#get_standings) - Get Standings
* [get_live_game_stats](#get_live_game_stats) - Get Live Game Statistics
* [get_season_player_stats](#get_season_player_stats) - Get Season Player Statistics
* [get_transactions](#get_transactions) - Get Transactions
* [get_venues](#get_venues) - Get NFL Venues
* [get_season_weeks](#get_season_weeks) - Get Season Weeks

## get_draft_info

Retrieves draft information for a specific year including all rounds,
picks, traded picks, and compensatory selections.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDraftInfo" method="get" path="/football/v2/draft/{year}" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_draft_info(year=2025)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `year`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Draft year                                                          | 2025                                                                |
| `round`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Filter by round                                                     |                                                                     |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by team                                                      |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DraftResponse](../../models/draftresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_weekly_game_details

Retrieves detailed game information for a specific week including team standings,
drive charts, replays, and tagged videos.


### Example Usage

<!-- UsageSnippet language="python" operationID="getWeeklyGameDetails" method="get" path="/football/v2/experience/weekly-game-details" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_weekly_game_details(request={
        "season": 2025,
        "type": models.SeasonTypeEnum.REG,
        "week": 4,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.GetWeeklyGameDetailsRequest](../../models/getweeklygamedetailsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[List[models.WeeklyGameDetail]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_football_games

Retrieves game information for a specific season, season type, and week from the Football API.
This endpoint provides core game data with external IDs.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFootballGames" method="get" path="/football/v2/games/season/{season}/seasonType/{seasonType}/week/{week}" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_football_games(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, with_external_ids=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 4                                                                   |
| `with_external_ids`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include external IDs in response                                    |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FootballGamesResponse](../../models/footballgamesresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_football_box_score

Retrieves comprehensive box score data for a specific game including
team statistics, individual player statistics, and scoring summary.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFootballBoxScore" method="get" path="/football/v2/games/{gameId}/boxscore" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_football_box_score(game_id="ebc07c38-dcb1-4f5e-b7af-7ecdcae7eebe")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (UUID)                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BoxScoreResponse](../../models/boxscoreresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_play_by_play

Retrieves detailed play-by-play data for a specific game including
all plays, drives, scoring events, and key statistics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayByPlay" method="get" path="/football/v2/games/{gameId}/playbyplay" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_play_by_play(game_id="7dac8dbb-0515-45a5-99f8-c1ecc9cdcbba", include_penalties=True, include_formations=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (UUID)                                              |
| `include_penalties`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include penalty details                                             |
| `include_formations`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include offensive/defensive formations                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlayByPlayResponse](../../models/playbyplayresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_injury_reports

Retrieves current injury reports for all teams or specific teams
with injury status, designation, and practice participation.


### Example Usage

<!-- UsageSnippet language="python" operationID="getInjuryReports" method="get" path="/football/v2/injuries" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_injury_reports(season=2025, week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 4                                                                   |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by specific team                                             |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.InjuryReportResponse](../../models/injuryreportresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_players_team_roster

Retrieves the complete roster for a specific team including active, practice squad, and injured reserve players with detailed player information.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayersTeamRoster" method="get" path="/football/v2/players/teams/{teamId}/roster" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_players_team_roster(team_id="10403800-517c-7b8c-65a3-c61b95d86123", season=2025, include_stats=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team identifier (UUID)                                              | 10403800-517c-7b8c-65a3-c61b95d86123                                |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `include_stats`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include current season statistics                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RosterResponse](../../models/rosterresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_player_details

Retrieves detailed information about a specific player including biography,
career statistics, and current season performance.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerDetails" method="get" path="/football/v2/players/{playerId}" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_player_details(player_id="2560726", season=2025)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `player_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Player identifier                                                   | 2560726                                                             |
| `season`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Season for statistics (defaults to current)                         | 2025                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlayerDetail](../../models/playerdetail.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_standings

Retrieves team standings for a specific season, season type, and week.
Includes division, conference, and overall standings with detailed statistics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getStandings" method="get" path="/football/v2/standings" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_standings(season=2025, season_type=models.SeasonTypeEnum.REG, week=3, limit=20)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 3                                                                   |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of results to return                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.StandingsResponse](../../models/standingsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_live_game_stats

Retrieves live game statistics and summaries for games in progress or completed games.
Provides real-time statistical data for specified season, type, and week.


### Example Usage

<!-- UsageSnippet language="python" operationID="getLiveGameStats" method="get" path="/football/v2/stats/live/game-summaries" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_live_game_stats(season=2025, season_type=models.SeasonTypeEnum.REG, week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GameStatsResponse](../../models/gamestatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_season_player_stats

Retrieves aggregated player statistics for a specific season with filtering
options by position, team, and statistical categories.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSeasonPlayerStats" method="get" path="/football/v2/stats/players/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_season_player_stats(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "stat_category": models.StatCategory.PASSING,
        "sort": "passingYards:desc",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.GetSeasonPlayerStatsRequest](../../models/getseasonplayerstatsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.PlayerStatsResponse](../../models/playerstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_transactions

Retrieves recent transactions including trades, signings, releases,
practice squad moves, and injured reserve designations.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTransactions" method="get" path="/football/v2/transactions" -->
```python
from datetime import date
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_transactions(request={
        "start_date": date.fromisoformat("2025-01-01"),
        "end_date": date.fromisoformat("2025-09-24"),
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetTransactionsRequest](../../models/gettransactionsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.TransactionsResponse](../../models/transactionsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_venues

Retrieves information about all NFL stadiums and venues, including international venues.
Provides venue details such as addresses, locations, and territories.


### Example Usage

<!-- UsageSnippet language="python" operationID="getVenues" method="get" path="/football/v2/venues" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_venues(season=2025, limit=20)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of venues to return                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.VenuesResponse](../../models/venuesresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_season_weeks

Retrieves all weeks for a specific season including preseason, regular season, and postseason. Includes bye team information for each week.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSeasonWeeks" method="get" path="/football/v2/weeks/season/{season}" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.football.get_season_weeks(season=2025, limit=20)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of weeks to return                                   |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WeeksResponse](../../models/weeksresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |