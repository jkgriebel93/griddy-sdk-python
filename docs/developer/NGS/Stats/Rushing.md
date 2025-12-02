---
tags:
  - ngs
  - stats
---
[[Stats]]

## /api/statboard/rushing
### Query Params
Standard

### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "filter": "ALL",
    "threshold": 65,
    "stats": [
        {
            "avgTimeToLos": 2.712445945945946,
            "expectedRushYards": 336.5809147728867,
            "rushAttempts": 78,
            "rushPctOverExpected": 0.42105263157894735,
            "rushTouchdowns": 1,
            "rushYards": 329,
            "rushYardsOverExpected": -13.580914772886672,
            "rushYardsOverExpectedPerAtt": -0.17869624701166673,
            "player": {
                "season": 2025,
                "displayName": "Isiah Pacheco",
                "esbId": "PAC576791",
                "firstName": "Isiah",
                "footballName": "Isiah",
                "gsisId": "00-0037197",
                "gsisItId": 54716,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/tqshteijt4xhgk2ei9sx",
                "jerseyNumber": 10,
                "lastName": "Pacheco",
                "position": "RB",
                "positionGroup": "RB",
                "shortName": "I.Pacheco",
                "smartId": "32005041-4357-6791-9031-d5a8938af2e4",
                "status": "ACT",
                "uniformNumber": "10",
                "currentTeamId": "2310",
                "ngsPosition": "RB",
                "ngsPositionGroup": "RB"
            },
            "teamId": "2310",
            "efficiency": 3.7009118541033437,
            "percentAttemptsGteEightDefenders": 12.82051282051282,
            "avgRushYards": 4.217948717948718
        }
    ]
}
```