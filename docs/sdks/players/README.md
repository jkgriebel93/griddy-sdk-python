# Players
(*players*)

## Overview

Player information, statistics, and projections

### Available Operations

* [get_player](#get_player) - Get Player Details
* [get_projected_stats](#get_projected_stats) - Get Projected Player Statistics
* [search_players](#search_players) - Search Players

## get_player

Retrieves detailed information about a specific NFL player including physical attributes,
team information, draft details, and current status.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayer" method="get" path="/api/players/player" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.players.get_player(nfl_id=54517)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `nfl_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | NFL player identifier                                               | 54517                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlayerDetail](../../models/playerdetail.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_projected_stats

Retrieves projected fantasy statistics for players based on team, season, and week.
Returns data in JSON:API format with relationships between players and their projected stats.


### Example Usage

<!-- UsageSnippet language="python" operationID="getProjectedStats" method="get" path="/api/players/projectedStats" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.players.get_projected_stats(season=2025, week=4, filter_nfl_team_id="10403000-5851-f9d5-da45-78365a05b6b0", page_size=20)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 4                                                                   |
| `filter_nfl_team_id`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter by NFL team ID (UUID format)                                 | 10403000-5851-f9d5-da45-78365a05b6b0                                |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results per page                                          |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProjectedStatsResponse](../../models/projectedstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## search_players

Searches for NFL players by name or term. Returns a list of players matching the search criteria
including both active and retired players.


### Example Usage

<!-- UsageSnippet language="python" operationID="searchPlayers" method="get" path="/api/players/search" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.players.search_players(term="Pickens")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `term`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Search term for player name (first or last name)                    | Pickens                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlayerSearchResponse](../../models/playersearchresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |