# GetStandingsRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number                                          | 3                                                    |
| `limit`                                              | *Optional[int]*                                      | :heavy_minus_sign:                                   | Maximum number of results to return                  |                                                      |