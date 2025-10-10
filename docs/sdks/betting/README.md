# Betting
(*betting*)

## Overview

Game betting odds and lines

### Available Operations

* [get_weekly_betting_odds](#get_weekly_betting_odds) - Get Weekly Betting Odds

## get_weekly_betting_odds

Retrieves comprehensive betting odds for all games in a specified week.
Returns point spreads, money lines, and totals (over/under) for each game
with the latest odds updates from betting markets.


### Example Usage

<!-- UsageSnippet language="python" operationID="getWeeklyBettingOdds" method="get" path="/api/schedules/week/odds" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.betting.get_weekly_betting_odds(season=2025, season_type=models.SeasonTypeEnum.REG, week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WeeklyOddsResponse](../../models/weeklyoddsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |