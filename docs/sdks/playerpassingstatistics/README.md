# PlayerPassingStatistics
(*player_passing_statistics*)

## Overview

Individual player passing statistics and analytics by week

### Available Operations

* [get_player_passing_stats_by_week](#get_player_passing_stats_by_week) - Get Player Passing Statistics by Week

## get_player_passing_stats_by_week

Retrieves comprehensive passing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and game-specific context.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerPassingStatsByWeek" method="get" path="/api/secured/stats/players-offense/passing/week" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.player_passing_statistics.get_player_passing_stats_by_week(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "week": models.WeekSlugEnum.WEEK_10,
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
| `request`                                                                                       | [models.GetPlayerPassingStatsByWeekRequest](../../models/getplayerpassingstatsbyweekrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.WeeklyPassingStatsResponse](../../models/weeklypassingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |