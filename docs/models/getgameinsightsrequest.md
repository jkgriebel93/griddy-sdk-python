# GetGameInsightsRequest


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `season`                                  | *int*                                     | :heavy_check_mark:                        | Season year                               | 2025                                      |
| `limit`                                   | *Optional[int]*                           | :heavy_minus_sign:                        | Maximum number of insights to return      | 100                                       |
| `tags`                                    | *Optional[str]*                           | :heavy_minus_sign:                        | Comma-separated list of tags to filter by | pro-preview                               |
| `exclude_tags`                            | *Optional[str]*                           | :heavy_minus_sign:                        | Comma-separated list of tags to exclude   | betting                                   |
| `fapi_game_id`                            | *str*                                     | :heavy_check_mark:                        | FAPI Game identifier (UUID)               | f688dfde-311e-11f0-b670-ae1250fadad1      |
| `away_team_id`                            | *str*                                     | :heavy_check_mark:                        | Away team identifier                      | 3000                                      |
| `home_team_id`                            | *str*                                     | :heavy_check_mark:                        | Home team identifier                      | 3900                                      |