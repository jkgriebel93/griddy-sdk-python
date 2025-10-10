# TeamDefenseStatistics
(*team_defense_statistics*)

## Overview

Comprehensive team defensive statistics and situational analytics

### Available Operations

* [get_team_defense_stats_by_season](#get_team_defense_stats_by_season) - Get Team Defense Statistics by Season

## get_team_defense_stats_by_season

Retrieves comprehensive defensive statistics for NFL teams during a specified season. Returns detailed metrics including traditional defensive stats, advanced analytics like EPA and RYOE, Next Gen Stats data, and situational performance breakdowns. Supports filtering by various defensive situations including personnel packages (Base, Nickel, Dime), game situations (leading, trailing, tied), field positions (red zone, goal-to-go), and offensive formations faced (shotgun, under center, pistol, motion).

### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamDefenseStatsBySeason" method="get" path="/api/secured/stats/team-defense/overview/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.team_defense_statistics.get_team_defense_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
        "split": [
            models.Split.TEAM_DEFENSE_NICKEL,
            models.Split.TEAM_DEFENSE_RED_ZONE,
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.GetTeamDefenseStatsBySeasonRequest](../../models/getteamdefensestatsbyseasonrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |
| `server_url`                                                                                    | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | An optional server URL to use.                                                                  |

### Response

**[models.TeamDefenseStatsResponse](../../models/teamdefensestatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |