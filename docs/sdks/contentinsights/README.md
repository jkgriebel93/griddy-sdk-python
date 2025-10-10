# ContentInsights
(*content_insights*)

## Overview

Editorial insights and analytics content about NFL players and games

### Available Operations

* [get_season_content_insights](#get_season_content_insights) - Get Season Content Insights

## get_season_content_insights

Retrieves curated editorial insights and analytics content for NFL players during
a specified season. Returns expert commentary combining Next Gen Stats data with
editorial analysis, including pregame previews, postgame breakdowns, fantasy insights,
and evergreen content. Supports filtering by player, team, content tags, and publication
limits for targeted content discovery.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSeasonContentInsights" method="get" path="/api/content/insights/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content_insights.get_season_content_insights(season=2025, limit=60, tags=[
        models.QueryParamTags.NFL_PRO,
    ], team_id="3900", nfl_id="46101")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of insights to return                                | 60                                                                  |
| `tags`                                                              | List[[models.QueryParamTags](../../models/queryparamtags.md)]       | :heavy_minus_sign:                                                  | Content tags to filter by (supports multiple comma-separated tags)  | [<br/>"nfl-pro"<br/>]                                               |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by specific team identifier                                  | 3900                                                                |
| `nfl_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by specific player NFL identifier                            | 46101                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[List[models.Insight]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |