# GetPlayersTeamRosterRequest


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `team_id`                            | *str*                                | :heavy_check_mark:                   | Team identifier (UUID)               | 10403800-517c-7b8c-65a3-c61b95d86123 |
| `season`                             | *int*                                | :heavy_check_mark:                   | Season year                          | 2025                                 |
| `include_stats`                      | *Optional[bool]*                     | :heavy_minus_sign:                   | Include current season statistics    |                                      |