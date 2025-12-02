---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]
## /api/leaders/time/sack
### Query Params
| Name       | Value |
| ---------- | ----- |
| limit      | 20    |
| season     | 2025  |
| seasonType | REG   |
| week       | 2     |
### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "leagueAverage": 4.7670989761092155,
    "leaders": [
        {
            "leader": {
                "nflId": 47802,
                "esbId": "SIM204336",
                "firstName": "Jeffery",
                "gsisId": "00-0035643",
                "jerseyNumber": 98,
                "lastName": "Simmons",
                "playerName": "Jeffery Simmons",
                "position": "DT",
                "positionGroup": "DL",
                "shortName": "J.Simmons",
                "teamAbbr": "TEN",
                "teamId": "2100",
                "week": 4,
                "time": 2.085,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gi2z8wipg8w9vnxwbav0",
                "seasonAvg": 3.731714285714286,
                "teamAvg": 4.285620689655173
            },
            "play": {
                "gameId": 2025092804,
                "playId": 481,
                "sequence": 481,
                "down": 2,
                "gameClock": "06:16",
                "gameKey": 59896,
                "health": null,
                "homeScore": 0,
                "isBigPlay": false,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": false,
                "isScoring": false,
                "playDescription": "(6:16) C.Stroud sacked at TEN 35 for -3 yards (J.Simmons).",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "gsisId": "00-0039163",
                        "playId": 481,
                        "clubCode": "HST",
                        "playerName": "C.Stroud",
                        "statId": 20,
                        "yards": -3
                    },
                    {
                        "gsisId": "00-0035643",
                        "playId": 481,
                        "clubCode": "TEN",
                        "playerName": "J.Simmons",
                        "statId": 83,
                        "yards": -3
                    },
                    {
                        "gsisId": "00-0035643",
                        "playId": 481,
                        "clubCode": "TEN",
                        "playerName": "J.Simmons",
                        "statId": 110,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0035643",
                        "playId": 481,
                        "clubCode": "TEN",
                        "playerName": "J.Simmons",
                        "statId": 79,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0035643",
                        "playId": 481,
                        "clubCode": "TEN",
                        "playerName": "J.Simmons",
                        "statId": 120,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0035643",
                        "playId": 481,
                        "clubCode": "TEN",
                        "playerName": "J.Simmons",
                        "statId": 402,
                        "yards": 3
                    }
                ],
                "playType": "play_type_sack",
                "playTypeCode": 2,
                "possessionTeamId": "2120",
                "preSnapHomeScore": 0,
                "preSnapVisitorScore": 0,
                "quarter": 1,
                "timeOfDayUTC": "2025-09-28T17:19:16.000Z",
                "visitorScore": 0,
                "yardline": "TEN 32",
                "yardlineNumber": 32,
                "yardlineSide": "TEN",
                "yardsToGo": 7,
                "absoluteYardlineNumber": 78,
                "actualYardlineForFirstDown": 84.78,
                "actualYardsToGo": 7.46,
                "endGameClock": "6:14",
                "isChangeOfPossession": false,
                "playDirection": "right",
                "startGameClock": "6:16"
            }
        }
    ]
}
```