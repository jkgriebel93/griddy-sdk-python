# SeasonSchedule
(*season_schedule*)

## Overview

Season weeks and bye information

### Available Operations

* [get_schedule_season_weeks](#get_schedule_season_weeks) - Get Season Weeks

## get_schedule_season_weeks

Retrieves all weeks for a specific season including preseason, regular season, and postseason weeks. Returns week dates, types, and teams on bye for each week. This endpoint provides a comprehensive season calendar with all scheduling information.

### Example Usage

<!-- UsageSnippet language="python" operationID="getScheduleSeasonWeeks" method="get" path="/api/schedules/weeks" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.season_schedule.get_schedule_season_weeks(season=2025)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.SeasonWeeksResponse](../../models/seasonweeksresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |