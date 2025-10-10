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
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.content_insights.get_season_content_insights(request={
        "season": 2025,
        "limit": 60,
        "tags": [
            models.QueryParamTags.NFL_PRO,
        ],
        "team_id": "3900",
        "nfl_id": "46101",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.GetSeasonContentInsightsRequest](../../models/getseasoncontentinsightsrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[List[models.Insight]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |