# PlayerRushingStatistics
(*player_rushing_statistics*)

## Overview

Individual player rushing statistics and analytics

### Available Operations

* [get_player_rushing_stats_by_season](#get_player_rushing_stats_by_season) - Get Player Rushing Statistics by Season
* [get_player_rushing_stats_by_week](#get_player_rushing_stats_by_week) - Get Player Rushing Statistics by Week

## get_player_rushing_stats_by_season

Retrieves comprehensive rushing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and situational breakdowns.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerRushingStatsBySeason" method="get" path="/api/secured/stats/players-offense/rushing/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.player_rushing_statistics.get_player_rushing_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "limit": 3,
        "sort_value": models.SortOrderEnum.DESC,
        "team_offense": [
            "3000",
            "3900",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.GetPlayerRushingStatsBySeasonRequest](../../models/getplayerrushingstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.RushingStatsResponse](../../models/rushingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_player_rushing_stats_by_week

Retrieves comprehensive rushing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and game-specific context.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerRushingStatsByWeek" method="get" path="/api/secured/stats/players-offense/rushing/week" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.player_rushing_statistics.get_player_rushing_stats_by_week(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "week": models.WeekSlugEnum.WEEK_4,
        "sort_value": models.SortOrderEnum.DESC,
        "team_offense": [
            "3900",
            "3200",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.GetPlayerRushingStatsByWeekRequest](../../models/getplayerrushingstatsbyweekrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.WeeklyRushingStatsResponse](../../models/weeklyrushingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |