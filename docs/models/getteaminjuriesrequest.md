# GetTeamInjuriesRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `team_id`                                            | *str*                                                | :heavy_check_mark:                                   | Team identifier (UUID format)                        | 10403000-5851-f9d5-da45-78365a05b6b0                 |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number within the season                        | 4                                                    |