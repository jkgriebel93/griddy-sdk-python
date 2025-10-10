# Stats
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
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.stats.get_stats_boxscore(game_id="2025092800")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (10-digit format YYYYMMDDNN)                        | 2025092800                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TeamBoxScore1](../../models/teamboxscore1.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_game_team_rankings

Retrieves comprehensive statistical rankings for both teams in a specific game.
Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


### Example Usage

<!-- UsageSnippet language="python" operationID="getGameTeamRankings" method="get" path="/api/stats/game/team-rankings" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.stats.get_game_team_rankings(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "away_team_id": "10403000-5851-f9d5-da45-78365a05b6b0",
        "home_team_id": "10403900-8251-6892-d81c-4348525c2d47",
        "week": 4,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.GetGameTeamRankingsRequest](../../models/getgameteamrankingsrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.TeamRankingsResponse](../../models/teamrankingsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_gamecenter

Retrieves advanced game statistics including passer zones, receiver separation,
pass rush metrics, and performance leaders for a specific game.


### Example Usage

<!-- UsageSnippet language="python" operationID="getGamecenter" method="get" path="/api/stats/gamecenter" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.stats.get_gamecenter(game_id="2025092800")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier                                                     | 2025092800                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GamecenterResponse](../../models/gamecenterresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_multiple_rankings_all_teams

Retrieves rankings for all 32 NFL teams across multiple specified statistical categories.
Allows comparison of teams across up to 5 different statistics simultaneously.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMultipleRankingsAllTeams" method="get" path="/api/stats/multiple-rankings/all-teams" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.stats.get_multiple_rankings_all_teams(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "stat0": "scoring-averagePointsScored",
        "stat1": "offense-yardsPerGame",
        "stat2": "offense-rushYardsPerGame",
        "stat3": "offense-passYardsPerGame",
        "stat4": "misc-netTurnovers",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.GetMultipleRankingsAllTeamsRequest](../../models/getmultiplerankingsallteamsrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[List[models.MultipleRankingsCategory]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |