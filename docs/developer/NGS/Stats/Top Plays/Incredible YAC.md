---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]
## /api/leaders/expectation/yac/season

### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "yacLeaders": [
        {
            "leader": {
                "esbId": "SAM338622",
                "firstName": "Dylan",
                "gsisId": "00-0040162",
                "jerseyNumber": 22,
                "lastName": "Sampson",
                "playerName": "Dylan Sampson",
                "position": "RB",
                "positionGroup": "RB",
                "recYards": 66,
                "shortName": "D.Sampson",
                "teamAbbr": "CLE",
                "teamId": "1050",
                "week": 12,
                "yardsAfterCatch": 71.9,
                "airYards": -5.900000000000006,
                "isTouchdown": true,
                "expectedYardsAfterCatch": 13.177782910439419,
                "yardsAfterCatchOverExpectation": 58.72221708956059,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/den1hzzomdxfcsgk88o5"
            },
            "play": {
                "gameId": 2025112308,
                "playId": 3501,
                "sequence": 3501,
                "down": 3,
                "gameClock": "08:29",
                "gameKey": 60016,
                "health": null,
                "homeScore": 3,
                "isBigPlay": true,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": false,
                "isScoring": true,
                "playDescription": "(8:29) (Shotgun) S.Sanders pass short right to D.Sampson for 66 yards, TOUCHDOWN.",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "playId": 3501,
                        "clubCode": "CLV",
                        "statId": 4,
                        "yards": 0
                    },
                    {
                        "playId": 3501,
                        "clubCode": "CLV",
                        "statId": 6,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0040668",
                        "playId": 3501,
                        "clubCode": "CLV",
                        "playerName": "S.Sanders",
                        "statId": 16,
                        "yards": 66
                    },
                    {
                        "gsisId": "00-0040668",
                        "playId": 3501,
                        "clubCode": "CLV",
                        "playerName": "S.Sanders",
                        "statId": 111,
                        "yards": -5
                    },
                    {
                        "gsisId": "00-0040162",
                        "playId": 3501,
                        "clubCode": "CLV",
                        "playerName": "D.Sampson",
                        "statId": 22,
                        "yards": 66
                    },
                    {
                        "gsisId": "00-0040162",
                        "playId": 3501,
                        "clubCode": "CLV",
                        "playerName": "D.Sampson",
                        "statId": 115,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0040162",
                        "playId": 3501,
                        "clubCode": "CLV",
                        "playerName": "D.Sampson",
                        "statId": 113,
                        "yards": 71
                    }
                ],
                "playType": "play_type_pass",
                "playTypeCode": 2,
                "possessionTeamId": "1050",
                "preSnapHomeScore": 3,
                "preSnapVisitorScore": 17,
                "quarter": 4,
                "timeOfDayUTC": "2025-11-23T23:43:33.000Z",
                "visitorScore": 23,
                "week": 12,
                "yardline": "CLE 34",
                "yardlineNumber": 34,
                "yardlineSide": "CLE",
                "yardsToGo": 9,
                "absoluteYardlineNumber": 76,
                "actualYardlineForFirstDown": 67.32,
                "actualYardsToGo": 9.15,
                "endGameClock": "8:19",
                "isChangeOfPossession": false,
                "playDirection": "left",
                "startGameClock": "8:30"
            }
        }
    ]
}
```