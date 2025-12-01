---
tags:
  - ngs
  - stats
---
[[Stats]]

## /api/statboard/passing
## Query Params

| Name       | Value |
| ---------- | ----- |
| season     | 2025  |
| seasonType | REG   |
| week       | 4     |
|            |       |
### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "filter": "ALL",
    "threshold": 98,
    "stats": [
        {
            "aggressiveness": 13.253012048192772,
            "attempts": 332,
            "avgAirDistance": 21.5480662008494,
            "avgAirYardsDifferential": -2.970877951446626,
            "avgAirYardsToSticks": -1.2490322580645163,
            "avgCompletedAirYards": 5.17041237113402,
            "avgIntendedAirYards": 8.141290322580646,
            "avgTimeToThrow": 2.931358662613982,
            "completionPercentage": 58.43373493975904,
            "completionPercentageAboveExpectation": -3.7745180722891476,
            "completions": 194,
            "expectedCompletionPercentage": 62.20825301204819,
            "gamesPlayed": 10,
            "interceptions": 6,
            "maxAirDistance": 58.350467007557015,
            "maxCompletedAirDistance": 50.494887860059656,
            "passTouchdowns": 6,
            "passYards": 1954,
            "passerRating": 73.79518072289159,
            "playerName": "Cam Ward",
            "season": 2025,
            "seasonType": "REG",
            "player": {
                "season": 2025,
                "currentTeamId": "2100",
                "displayName": "Cam Ward",
                "esbId": "WAR065305",
                "firstName": "Cameron",
                "footballName": "Cameron",
                "gsisId": "00-0040676",
                "gsisItId": 58203,
                "jerseyNumber": 1,
                "lastName": "Ward",
                "position": "QB",
                "positionGroup": "QB",
                "shortName": "C.Ward",
                "status": "ACT",
                "uniformNumber": "01",
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/viadutkbvligsopnd2qn",
                "smartId": "32005741-5206-5305-364b-76c1f988f45e",
                "ngsPosition": "QB",
                "ngsPositionGroup": "QB"
            },
            "position": "QB",
            "teamId": "2100"
        }
    ]
}
```