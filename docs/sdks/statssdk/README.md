# StatsSDK
(*stats*)

## Overview

Comprehensive game and team statistics endpoints

### Available Operations

* [get_stats_boxscore](#get_stats_boxscore) - Get Game Boxscore (Stats API)
* [get_game_team_rankings](#get_game_team_rankings) - Get Team Rankings for Game
* [get_gamecenter](#get_gamecenter) - Get Gamecenter Statistics
* [get_multiple_rankings_all_teams](#get_multiple_rankings_all_teams) - Get Multiple Rankings for All Teams

## get_stats_boxscore

Retrieves comprehensive boxscore data for a specific game including team statistics,
individual player statistics, and scoring summary. Returns empty arrays for future games.


### Example Usage

<!-- UsageSnippet language="python" operationID="getStatsBoxscore" method="get" path="/api/stats/boxscore" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.stats.get_stats_boxscore(game_id="2025092800")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (10-digit format YYYYMMDDNN)                        | 2025092800                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.TeamBoxScore](../../models/teamboxscore.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_game_team_rankings

Retrieves comprehensive statistical rankings for both teams in a specific game.
Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


### Example Usage

<!-- UsageSnippet language="python" operationID="getGameTeamRankings" method="get" path="/api/stats/game/team-rankings" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.stats.get_game_team_rankings(season=2025, season_type="REG", away_team_id="10403000-5851-f9d5-da45-78365a05b6b0", home_team_id="10403900-8251-6892-d81c-4348525c2d47", week=4)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `away_team_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Away team UUID                                                      | 10403000-5851-f9d5-da45-78365a05b6b0                                |
| `home_team_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Home team UUID                                                      | 10403900-8251-6892-d81c-4348525c2d47                                |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.TeamRankingsResponse](../../models/teamrankingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_gamecenter

Retrieves advanced game statistics including passer zones, receiver separation,
pass rush metrics, and performance leaders for a specific game.


### Example Usage

<!-- UsageSnippet language="python" operationID="getGamecenter" method="get" path="/api/stats/gamecenter" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.stats.get_gamecenter(game_id="2025092800")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier                                                     | 2025092800                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.GamecenterResponse](../../models/gamecenterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_multiple_rankings_all_teams

Retrieves rankings for all 32 NFL teams across multiple specified statistical categories.
Allows comparison of teams across up to 5 different statistics simultaneously.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMultipleRankingsAllTeams" method="get" path="/api/stats/multiple-rankings/all-teams" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.stats.get_multiple_rankings_all_teams(season=2025, season_type="REG", stat0="scoring-averagePointsScored", stat1="offense-yardsPerGame", stat2="offense-rushYardsPerGame", stat3="offense-passYardsPerGame", stat4="misc-netTurnovers")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `stat0`                                                             | *str*                                                               | :heavy_check_mark:                                                  | First statistical category                                          | scoring-averagePointsScored                                         |
| `stat1`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Second statistical category                                         | offense-yardsPerGame                                                |
| `stat2`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Third statistical category                                          | offense-rushYardsPerGame                                            |
| `stat3`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Fourth statistical category                                         | offense-passYardsPerGame                                            |
| `stat4`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Fifth statistical category                                          | misc-netTurnovers                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[List[models.MultipleRankingsCategory]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |