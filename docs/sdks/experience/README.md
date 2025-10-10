# Experience
(*experience*)

## Overview

Experience API endpoints for games and teams

### Available Operations

* [get_experience_games](#get_experience_games) - Get Games by Season and Week
* [get_experience_teams](#get_experience_teams) - Get All Teams

## get_experience_games

Retrieves game information for a specific season, season type, and week.
Returns comprehensive game data including teams, venues, broadcast information, and ticket details.


### Example Usage

<!-- UsageSnippet language="python" operationID="getExperienceGames" method="get" path="/experience/v1/games" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.experience.get_experience_games(season=2025, season_type=models.SeasonTypeEnum.REG, week=4)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year (e.g., 2025)                                            | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number within the season                                       | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ExperienceGamesResponse](../../models/experiencegamesresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_experience_teams

Retrieves information for all NFL teams including Pro Bowl teams.
Returns comprehensive team data including logos, colors, venues, and social media links.


### Example Usage

<!-- UsageSnippet language="python" operationID="getExperienceTeams" method="get" path="/experience/v1/teams" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.experience.get_experience_teams(season=2025, allteams=True)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `allteams`                                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include all teams including special teams                           | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ExperienceTeamsResponse](../../models/experienceteamsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |