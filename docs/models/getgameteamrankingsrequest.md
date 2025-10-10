# GetGameTeamRankingsRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `away_team_id`                                       | *str*                                                | :heavy_check_mark:                                   | Away team UUID                                       | 10403000-5851-f9d5-da45-78365a05b6b0                 |
| `home_team_id`                                       | *str*                                                | :heavy_check_mark:                                   | Home team UUID                                       | 10403900-8251-6892-d81c-4348525c2d47                 |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number                                          | 4                                                    |