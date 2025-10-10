# Content
(*content*)

## Overview

Game previews, film cards, and insights

### Available Operations

* [get_game_preview](#get_game_preview) - Get Game Preview Content
* [get_home_film_cards](#get_home_film_cards) - Get Home Film Cards
* [get_game_insights](#get_game_insights) - Get Game-Specific Insights

## get_game_preview

Retrieves preview content and insights for a specific game based on teams and week. Returns preview information, matchup analysis, and key storylines.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGamePreview" method="get" path="/api/content/game/preview" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.content.get_game_preview(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "week": 4,
        "visitor_display_name": "Minnesota Vikings",
        "home_display_name": "Pittsburgh Steelers",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetGamePreviewRequest](../../models/getgamepreviewrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.GamePreviewResponse](../../models/gamepreviewresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_home_film_cards

Retrieves featured film room content cards for the home page. Returns weekly playlists and featured player film breakdowns.

### Example Usage

<!-- UsageSnippet language="python" operationID="getHomeFilmCards" method="get" path="/api/content/home-film-cards" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.content.get_home_film_cards()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HomeFilmCardsResponse](../../models/homefilmcardsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_game_insights

Retrieves analytical insights and advanced statistics for a specific game. Can filter by tags and exclude specific content types.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGameInsights" method="get" path="/api/content/insights/game" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.content.get_game_insights(request={
        "season": 2025,
        "limit": 100,
        "tags": "pro-preview",
        "exclude_tags": "betting",
        "fapi_game_id": "f688dfde-311e-11f0-b670-ae1250fadad1",
        "away_team_id": "3000",
        "home_team_id": "3900",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetGameInsightsRequest](../../models/getgameinsightsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.GameInsight]](../../models/.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |