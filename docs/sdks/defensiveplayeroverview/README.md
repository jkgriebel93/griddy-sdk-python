# DefensivePlayerOverview
(*defensive_player_overview*)

## Overview

Comprehensive individual defensive player statistics and analytics

### Available Operations

* [get_defensive_overview_stats_by_season](#get_defensive_overview_stats_by_season) - Get Defensive Player Overview Statistics by Season

## get_defensive_overview_stats_by_season

Retrieves comprehensive defensive overview statistics for NFL players during a specified season. Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced analytics. Supports filtering by qualified defenders, teams, and various sorting options. Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDefensiveOverviewStatsBySeason" method="get" path="/api/secured/stats/defense/overview/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.defensive_player_overview.get_defensive_overview_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "limit": 3,
        "sort_key": models.QueryParamSortKey.SACK,
        "sort_value": models.SortOrderEnum.DESC,
        "team_defense": [
            "3000",
            "3900",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.GetDefensiveOverviewStatsBySeasonRequest](../../models/getdefensiveoverviewstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.DefensiveOverviewStatsResponse](../../models/defensiveoverviewstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |