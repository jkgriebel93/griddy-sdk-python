# PlayerStatistics
(*player_statistics*)

## Overview

Individual player passing statistics and analytics

### Available Operations

* [get_player_passing_stats_by_season](#get_player_passing_stats_by_season) - Get Player Passing Statistics by Season

## get_player_passing_stats_by_season

Retrieves comprehensive passing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers only, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and situational statistics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerPassingStatsBySeason" method="get" path="/api/secured/stats/players-offense/passing/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.player_statistics.get_player_passing_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
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
| `request`                                                                                           | [models.GetPlayerPassingStatsBySeasonRequest](../../models/getplayerpassingstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.PassingStatsResponse](../../models/passingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |