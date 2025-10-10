# SchedulesExtended
(*schedules_extended*)

## Overview

Current games, standings, and betting futures

### Available Operations

* [get_current_week_games](#get_current_week_games) - Get Current Week Games
* [get_future_betting_odds](#get_future_betting_odds) - Get Future Betting Odds
* [get_team_standings](#get_team_standings) - Get Team Standings

## get_current_week_games

Retrieves all games for the current week of the NFL season.
Returns comprehensive game data including teams, venues, broadcast information,
scores (for completed games), and ticket details. The endpoint automatically
determines the current week based on the current date.


### Example Usage

<!-- UsageSnippet language="python" operationID="getCurrentWeekGames" method="get" path="/api/schedules/current" -->
```python
from griddy.nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules_extended.get_current_week_games()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.CurrentGamesResponse](../../models/currentgamesresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_future_betting_odds

Retrieves comprehensive betting futures data including Super Bowl odds,
conference championship odds, and division winner odds for all teams.
Returns decimal odds for each selection along with availability status.
This endpoint provides futures market data across multiple betting hierarchies.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFutureBettingOdds" method="get" path="/api/schedules/genius/future/odds" -->
```python
from griddy.nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules_extended.get_future_betting_odds()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.FuturesOddsResponse](../../models/futuresoddsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_team_standings

Retrieves comprehensive team standings for a specific season, season type, and week.
Returns detailed standings information including division, conference, home/away records,
win percentages, points for/against, current streaks, and clinching scenarios.
Standings are calculated through the specified week.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamStandings" method="get" path="/api/schedules/standings" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules_extended.get_team_standings(season=2025, season_type=models.SeasonTypeEnum.REG, week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.StandingsResponse](../../models/standingsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |