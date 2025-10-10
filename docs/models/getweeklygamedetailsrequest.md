# GetWeeklyGameDetailsRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `type`                                               | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Season type                                          | REG                                                  |
| `week`                                               | *int*                                                | :heavy_check_mark:                                   | Week number                                          | 4                                                    |
| `include_drive_chart`                                | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Include drive chart data                             |                                                      |
| `include_replays`                                    | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Include replay videos                                |                                                      |
| `include_standings`                                  | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Include team standings                               |                                                      |
| `include_tagged_videos`                              | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Include tagged video content                         |                                                      |