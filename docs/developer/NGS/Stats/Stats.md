---
tags:
  - ngs
  - stats
---
Belongs to [[Next Gen Stats]]

## /api/league/schedule/current
### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "week": 13,
    "games": [
        {
            "gameKey": 60035,
            "gameDate": "11/30/2025",
            "gameId": 2025113010,
            "gameTime": "2025-12-01T01:20:00Z",
            "gameTimeEastern": "20:20:00",
            "gameType": "REG",
            "homeDisplayName": "Washington Commanders",
            "homeNickname": "Commanders",
            "homeTeam": {
                "teamId": "5110",
                "smartId": "10405110-ec3c-669e-2614-db3dc1736e95",
                "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/WAS",
                "abbr": "WAS",
                "cityState": "Washington",
                "fullName": "Washington Commanders",
                "nick": "Commanders",
                "teamType": "TEAM",
                "conferenceAbbr": "NFC",
                "divisionAbbr": "NCE"
            },
            "homeTeamAbbr": "WAS",
            "homeTeamId": "5110",
            "isoTime": 1764552000000,
            "networkChannel": "NBC",
            "ngsGame": true,
            "season": 2025,
            "seasonType": "REG",
            "site": {
                "smartId": "00082389-5f81-bc7b-7280-78260ea1be2a",
                "siteId": 2389,
                "siteFullName": "Northwest Stadium",
                "siteCity": "Landover",
                "siteState": "MD",
                "postalCode": "20785",
                "roofType": "OUTDOOR"
            },
            "smartId": "f877d570-311e-11f0-b670-ae1250fadad1",
            "visitorDisplayName": "Denver Broncos",
            "visitorNickname": "Broncos",
            "visitorTeam": {
                "teamId": "1400",
                "smartId": "10401400-b89b-96e5-55d1-caa7e18de3d8",
                "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/DEN",
                "abbr": "DEN",
                "cityState": "Denver",
                "fullName": "Denver Broncos",
                "nick": "Broncos",
                "teamType": "TEAM",
                "conferenceAbbr": "AFC",
                "divisionAbbr": "ACW"
            },
            "visitorTeamAbbr": "DEN",
            "visitorTeamId": "1400",
            "week": 13,
            "weekNameAbbr": "Week 13",
            "score": {
                "time": "00:00",
                "phase": "FINAL OVERTIME",
                "visitorTeamScore": {
                    "pointTotal": 27,
                    "pointQ1": 3,
                    "pointQ2": 10,
                    "pointQ3": 7,
                    "pointQ4": 0,
                    "pointOT": 7,
                    "timeoutsRemaining": 0
                },
                "homeTeamScore": {
                    "pointTotal": 26,
                    "pointQ1": 0,
                    "pointQ2": 7,
                    "pointQ3": 7,
                    "pointQ4": 6,
                    "pointOT": 6,
                    "timeoutsRemaining": 1
                }
            },
            "releasedToClubs": true,
            "validated": true
        }
    ]
}
```

## /api/league/teams
### Response
```json
[
    {
        "abbr": "AFC",
        "cityState": "AFC",
        "conference": {
            "id": "0011",
            "abbr": "AFC",
            "fullName": "American Football Conference"
        },
        "conferenceAbbr": "AFC",
        "fullName": "AFC Pro Bowl Team",
        "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/APR",
        "nick": "AFC",
        "season": 2025,
        "smartId": "10408600-77a1-8b0f-8f54-99b7e0a7d1b2",
        "stadiumName": "Allegiant Stadium",
        "teamId": "8600",
        "teamSiteTicketUrl": null,
        "teamSiteUrl": null,
        "teamType": "PRO",
        "ticketPhoneNumber": null,
        "yearFound": 2020,
        "division": {}
    },
    {
        "abbr": "ARI",
        "cityState": "Arizona",
        "conference": {
            "id": "0015",
            "abbr": "NFC",
            "fullName": "National Football Conference"
        },
        "conferenceAbbr": "NFC",
        "fullName": "Arizona Cardinals",
        "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/ARI",
        "nick": "Cardinals",
        "season": 2025,
        "smartId": "10403800-517c-7b8c-65a3-c61b95d86123",
        "stadiumName": "State Farm Stadium",
        "teamId": "3800",
        "teamSiteTicketUrl": "http://www.azcardinals.com/tickets/",
        "teamSiteUrl": "http://www.azcardinals.com/",
        "teamType": "TEAM",
        "ticketPhoneNumber": "602-379-0102",
        "yearFound": 1920,
        "division": {
            "id": "0018",
            "abbr": "NCW",
            "fullName": "NFC West Division"
        }
    },
    {
        "abbr": "ATL",
        "cityState": "Atlanta",
        "conference": {
            "id": "0015",
            "abbr": "NFC",
            "fullName": "National Football Conference"
        },
        "conferenceAbbr": "NFC",
        "fullName": "Atlanta Falcons",
        "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/ATL",
        "nick": "Falcons",
        "season": 2025,
        "smartId": "10400200-f401-4e53-5175-0974e4f16cf7",
        "stadiumName": "Mercedes-Benz Stadium",
        "teamId": "0200",
        "teamSiteTicketUrl": "http://www.atlantafalcons.com/tickets/",
        "teamSiteUrl": "http://www.atlantafalcons.com/",
        "teamType": "TEAM",
        "ticketPhoneNumber": "470-341-4500",
        "yearFound": 1966,
        "division": {
            "id": "0020",
            "abbr": "NCS",
            "fullName": "NFC South Division"
        }
    },
    {
        "abbr": "BAL",
        "cityState": "Baltimore",
        "conference": {
            "id": "0011",
            "abbr": "AFC",
            "fullName": "American Football Conference"
        },
        "conferenceAbbr": "AFC",
        "fullName": "Baltimore Ravens",
        "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/BAL",
        "nick": "Ravens",
        "season": 2025,
        "smartId": "10400325-48de-3d6a-be29-8f829437f4c8",
        "stadiumName": "M&T Bank Stadium",
        "teamId": "0325",
        "teamSiteTicketUrl": "http://www.baltimoreravens.com/tickets/",
        "teamSiteUrl": "http://www.baltimoreravens.com/",
        "teamType": "TEAM",
        "ticketPhoneNumber": "410-261-RAVE (7283)",
        "yearFound": 1996,
        "division": {
            "id": "0013",
            "abbr": "ACN",
            "fullName": "AFC North Division"
        }
    },
    {
        "abbr": "BUF",
        "cityState": "Buffalo",
        "conference": {
            "id": "0011",
            "abbr": "AFC",
            "fullName": "American Football Conference"
        },
        "conferenceAbbr": "AFC",
        "fullName": "Buffalo Bills",
        "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/BUF",
        "nick": "Bills",
        "season": 2025,
        "smartId": "10400610-c40e-a673-1743-2ce2a5d5d731",
        "stadiumName": "Highmark Stadium",
        "teamId": "0610",
        "teamSiteTicketUrl": "http://www.buffalobills.com/tickets/",
        "teamSiteUrl": "http://www.buffalobills.com/",
        "teamType": "TEAM",
        "ticketPhoneNumber": "877-BB-TICKS",
        "yearFound": 1960,
        "division": {
            "id": "0012",
            "abbr": "ACE",
            "fullName": "AFC East Division"
        }
    }
]
```


## /api/league/schedule
### Query Params

| Name   | Value |
| ------ | ----- |
| season | 2025  |
### Response
```json
[
    {
        "gameKey": 60115,
        "gameDate": "07/31/2025",
        "gameId": 2025073151,
        "gameTime": "2025-08-01T00:00:00Z",
        "gameTimeEastern": "20:00:00",
        "gameType": "PRE",
        "homeDisplayName": "Detroit Lions",
        "homeNickname": "Lions",
        "homeTeam": {
            "teamId": "1540",
            "smartId": "10401540-f97c-2d19-6fcd-fac6490a48b7",
            "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/DET",
            "abbr": "DET",
            "cityState": "Detroit",
            "fullName": "Detroit Lions",
            "nick": "Lions",
            "teamType": "TEAM",
            "conferenceAbbr": "NFC",
            "divisionAbbr": "NCN"
        },
        "homeTeamAbbr": "DET",
        "homeTeamId": "1540",
        "isoTime": 1754006400000,
        "networkChannel": "NBC",
        "ngsGame": true,
        "season": 2025,
        "seasonType": "PRE",
        "site": {
            "smartId": "00081900-1285-0ec1-ea76-77f3ea190274",
            "siteId": 1900,
            "siteFullName": "Tom Benson Hall of Fame Stadium",
            "siteCity": "Canton",
            "siteState": "OH",
            "postalCode": "44708",
            "roofType": "OUTDOOR"
        },
        "smartId": "7af5a3a2-3ca3-11f0-b670-ae1250fadad1",
        "visitorDisplayName": "Los Angeles Chargers",
        "visitorNickname": "Chargers",
        "visitorTeam": {
            "teamId": "4400",
            "smartId": "10404400-3b35-073f-197e-194bb8240723",
            "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/LAC",
            "abbr": "LAC",
            "cityState": "Los Angeles",
            "fullName": "Los Angeles Chargers",
            "nick": "Chargers",
            "teamType": "TEAM",
            "conferenceAbbr": "AFC",
            "divisionAbbr": "ACW"
        },
        "visitorTeamAbbr": "LAC",
        "visitorTeamId": "4400",
        "week": 0,
        "weekNameAbbr": "HOF",
        "score": {
            "time": "00:00",
            "phase": "FINAL",
            "visitorTeamScore": {
                "pointTotal": 34,
                "pointQ1": 14,
                "pointQ2": 7,
                "pointQ3": 6,
                "pointQ4": 7,
                "pointOT": 0,
                "timeoutsRemaining": 3
            },
            "homeTeamScore": {
                "pointTotal": 7,
                "pointQ1": 0,
                "pointQ2": 7,
                "pointQ3": 0,
                "pointQ4": 0,
                "pointOT": 0,
                "timeoutsRemaining": 2
            }
        },
        "releasedToClubs": true,
        "validated": true
    }
]
```


