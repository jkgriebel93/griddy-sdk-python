---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]
## /api/leaders/expectation/completion/season

### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "completionLeaders": [
        {
            "leader": {
                "esbId": "PRE285723",
                "firstName": "Rayne",
                "gsisId": "00-0033077",
                "jerseyNumber": 4,
                "lastName": "Prescott",
                "passYards": 34,
                "playerName": "Dak Prescott",
                "position": "QB",
                "positionGroup": "QB",
                "shortName": "D.Prescott",
                "teamAbbr": "DAL",
                "teamId": "1200",
                "week": 4,
                "airYards": 35.45,
                "completionProbability": 0.0724,
                "receiver": {
                    "season": 2025,
                    "collegeConference": "Sun Belt Conference",
                    "collegeName": "South Alabama",
                    "displayName": "Jalen Tolbert",
                    "draftClub": "DAL",
                    "draftNumber": 88,
                    "draftround": 3,
                    "entryYear": 2022,
                    "esbId": "TOL148914",
                    "firstName": "Jalen",
                    "footballName": "Jalen",
                    "gsisId": "00-0037666",
                    "gsisItId": 54553,
                    "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/pif5ffxlibkfp90k1sj4",
                    "height": "6-3",
                    "jerseyNumber": 1,
                    "lastName": "Tolbert",
                    "position": "WR",
                    "positionGroup": "WR",
                    "rookieYear": 2022,
                    "shortName": "J.Tolbert",
                    "smartId": "3200544f-4c14-8914-de91-cd54d59de2a2",
                    "status": "ACT",
                    "statusDescriptionAbbr": "A01",
                    "statusShortDescription": "Active",
                    "teamAbbr": "DAL",
                    "uniformNumber": "1",
                    "weight": 195,
                    "currentTeamId": "1200",
                    "yearsOfExperience": 4,
                    "ngsPosition": "WR",
                    "ngsPositionGroup": "WR",
                    "birthDate": "1999-02-27"
                },
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/blixemm3s9sa4gmqk5yn"
            },
            "play": {
                "gameId": 2025092812,
                "playId": 4634,
                "sequence": 4634,
                "down": 2,
                "gameClock": "06:43",
                "gameKey": 59904,
                "health": null,
                "homeScore": 37,
                "isBigPlay": true,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": false,
                "isScoring": false,
                "playDescription": "(6:43) (Shotgun) D.Prescott pass deep right to J.Tolbert ran ob at GB 5 for 34 yards [C.Wooden].",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "playId": 4634,
                        "clubCode": "DAL",
                        "statId": 4,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0033077",
                        "playId": 4634,
                        "clubCode": "DAL",
                        "playerName": "D.Prescott",
                        "statId": 15,
                        "yards": 34
                    },
                    {
                        "gsisId": "00-0033077",
                        "playId": 4634,
                        "clubCode": "DAL",
                        "playerName": "D.Prescott",
                        "statId": 111,
                        "yards": 34
                    },
                    {
                        "gsisId": "00-0037666",
                        "playId": 4634,
                        "clubCode": "DAL",
                        "playerName": "J.Tolbert",
                        "statId": 21,
                        "yards": 34
                    },
                    {
                        "gsisId": "00-0037666",
                        "playId": 4634,
                        "clubCode": "DAL",
                        "playerName": "J.Tolbert",
                        "statId": 115,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0037666",
                        "playId": 4634,
                        "clubCode": "DAL",
                        "playerName": "J.Tolbert",
                        "statId": 113,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0038387",
                        "playId": 4634,
                        "clubCode": "GB",
                        "playerName": "C.Wooden",
                        "statId": 110,
                        "yards": 0
                    }
                ],
                "playType": "play_type_pass",
                "playTypeCode": 2,
                "possessionTeamId": "1200",
                "preSnapHomeScore": 37,
                "preSnapVisitorScore": 37,
                "quarter": 5,
                "timeOfDayUTC": "2025-09-29T03:50:35.000Z",
                "visitorScore": 37,
                "week": 4,
                "yardline": "GB 39",
                "yardlineNumber": 39,
                "yardlineSide": "GB",
                "yardsToGo": 7,
                "absoluteYardlineNumber": 49,
                "actualYardlineForFirstDown": 42.5,
                "actualYardsToGo": 7.13,
                "endGameClock": "6:36",
                "isChangeOfPossession": false,
                "playDirection": "left",
                "startGameClock": "6:45"
            }
        }
    ]
}
```