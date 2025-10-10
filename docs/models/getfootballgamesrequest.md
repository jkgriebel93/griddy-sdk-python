# GetFootballGamesRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number                                          | 4                                                    |
| `with_external_ids`                                  | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Include external IDs in response                     |                                                      |