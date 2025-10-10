# Teams
(*teams*)

## Overview

Team information, rosters, and schedules

### Available Operations

* [get_all_teams](#get_all_teams) - Get All Teams
* [get_team_roster](#get_team_roster) - Get Team Roster
* [get_weekly_team_roster](#get_weekly_team_roster) - Get Weekly Team Roster
* [get_team_schedule](#get_team_schedule) - Get Team Schedule

## get_all_teams

Retrieves information for all NFL teams including regular teams and Pro Bowl teams.
Returns comprehensive team data including colors, logos, stadiums, and contact information.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAllTeams" method="get" path="/api/teams/all" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.teams.get_all_teams()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[List[models.ProTeam]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_team_roster

Retrieves the complete roster for a specific team and season.
Returns detailed player information including physical attributes, college info, and experience.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamRoster" method="get" path="/api/teams/roster" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.teams.get_team_roster(team_id="3000", season=2025)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team identifier (4-digit string)                                    | 3000                                                                |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.TeamRosterResponse](../../models/teamrosterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_weekly_team_roster

Retrieves the roster for a specific team, season, season type, and week.
Returns player information with weekly status and availability.


### Example Usage

<!-- UsageSnippet language="python" operationID="getWeeklyTeamRoster" method="get" path="/api/teams/rosterWeek" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.teams.get_weekly_team_roster(team_id="3900", season=2025, season_type="REG", week=3)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team identifier (4-digit string)                                    | 3900                                                                |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 3                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.WeeklyRosterResponse](../../models/weeklyrosterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_team_schedule

Retrieves the complete schedule for a specific team and season.
Returns all games including preseason, regular season, and postseason with scores for completed games.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamSchedule" method="get" path="/api/teams/schedule" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.teams.get_team_schedule(team_id="3000", season=2025)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Team identifier (4-digit string)                                    | 3000                                                                |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[List[models.ScheduledGame]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |