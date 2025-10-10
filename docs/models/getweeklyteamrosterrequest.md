# GetWeeklyTeamRosterRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `team_id`                                            | *str*                                                | :heavy_check_mark:                                   | Team identifier (4-digit string)                     | 3900                                                 |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number within the season                        | 3                                                    |