# GetProjectedStatsRequest


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `filter_nfl_team_id`                 | *Optional[str]*                      | :heavy_minus_sign:                   | Filter by NFL team ID (UUID format)  | 10403000-5851-f9d5-da45-78365a05b6b0 |
| `season`                             | *int*                                | :heavy_check_mark:                   | Season year                          | 2025                                 |
| `week`                               | *int*                                | :heavy_check_mark:                   | Week number within the season        | 4                                    |
| `page_size`                          | *Optional[int]*                      | :heavy_minus_sign:                   | Number of results per page           |                                      |