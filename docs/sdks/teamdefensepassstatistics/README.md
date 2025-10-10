# TeamDefensePassStatistics
(*team_defense_pass_statistics*)

## Overview

Comprehensive team defensive pass statistics and situational analytics

### Available Operations

* [get_team_defense_pass_stats_by_season](#get_team_defense_pass_stats_by_season) - Get Team Defense Pass Statistics by Season

## get_team_defense_pass_stats_by_season

Retrieves comprehensive pass defense statistics for NFL teams during a specified season.
Returns detailed metrics including traditional defensive stats, advanced analytics like EPA
and YACOE (Yards After Catch Over Expected), Next Gen Stats data, and situational performance
breakdowns. Supports various sorting options and includes pressure rates, coverage metrics,
quarterback disruption stats, and receiver separation allowed.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamDefensePassStatsBySeason" method="get" path="/api/secured/stats/team-defense/pass/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.team_defense_pass_statistics.get_team_defense_pass_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.GetTeamDefensePassStatsBySeasonRequest](../../models/getteamdefensepassstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.TeamDefensePassStatsResponse](../../models/teamdefensepassstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |