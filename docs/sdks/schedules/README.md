# Schedules
(*schedules*)

## Overview

Game schedules, matchup rankings, and injury reports

### Available Operations

* [get_scheduled_game](#get_scheduled_game) - Get Single Game Details
* [get_game_matchup_rankings](#get_game_matchup_rankings) - Get Game Matchup Rankings
* [get_team_injuries](#get_team_injuries) - Get Team Injuries for Game Week
* [get_scheduled_games](#get_scheduled_games) - Get Games by Week

## get_scheduled_game

Retrieves detailed information for a specific game by its ID.
Returns comprehensive game data including teams, score, venue, broadcast information,
and current game status.


### Example Usage

<!-- UsageSnippet language="python" operationID="getScheduledGame" method="get" path="/api/schedules/game" -->
```python
from griddy.nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules.get_scheduled_game(game_id="f665fc10-311e-11f0-b670-ae1250fadad1")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (UUID format)                                       | f665fc10-311e-11f0-b670-ae1250fadad1                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.GameDetail](../../models/gamedetail.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_game_matchup_rankings

Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
for various statistical categories.


### Example Usage

<!-- UsageSnippet language="python" operationID="getGameMatchupRankings" method="get" path="/api/schedules/game/matchup/rankings" -->
```python
from griddy.nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules.get_game_matchup_rankings(game_id="2025092500")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (10-digit format YYYYMMDDNN)                        | 2025092500                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.MatchupRankingsResponse](../../models/matchuprankingsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_team_injuries

Retrieves injury report information for a specific team in a given week.
Returns player injury status and details for the specified team and week.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamInjuries" method="get" path="/api/schedules/game/team/injuries" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules.get_team_injuries(season=2025, season_type=models.SeasonTypeEnum.REG, team_id="10403000-5851-f9d5-da45-78365a05b6b0", week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team identifier (UUID format)                                       | 10403000-5851-f9d5-da45-78365a05b6b0                                |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.InjuryReportResponse](../../models/injuryreportresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_scheduled_games

Retrieves all games for a specific season, season type, and week.
Returns comprehensive game data including teams, venues, broadcast information,
and ticket details for all games in the specified week.


### Example Usage

<!-- UsageSnippet language="python" operationID="getScheduledGames" method="get" path="/api/schedules/games" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.schedules.get_scheduled_games(season=2025, season_type=models.SeasonTypeEnum.REG, week=3)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 3                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.GamesResponse](../../models/gamesresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |