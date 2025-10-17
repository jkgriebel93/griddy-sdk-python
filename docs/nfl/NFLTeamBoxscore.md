# NFLTeamBoxscore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_points** | [**List[NFLNFLBoxScorePlayerExtraPointsStatistic]**](NFLBoxScorePlayerExtraPointsStatistic.md) |  | [optional] 
**field_goals** | [**List[NFLNFLBoxScorePlayerFieldGoalsStatistic]**](NFLBoxScorePlayerFieldGoalsStatistic.md) |  | [optional] 
**fumbles** | [**List[NFLNFLBoxScorePlayerFumblesStatistic]**](NFLBoxScorePlayerFumblesStatistic.md) |  | [optional] 
**kick_return** | [**List[NFLNFLBoxScorePlayerKickReturnStatistic]**](NFLBoxScorePlayerKickReturnStatistic.md) |  | [optional] 
**kicking** | [**List[NFLNFLBoxScorePlayerKickingStatistic]**](NFLBoxScorePlayerKickingStatistic.md) |  | [optional] 
**passing** | [**List[NFLNFLBoxScorePlayerPassingStatistic]**](NFLBoxScorePlayerPassingStatistic.md) |  | [optional] 
**punt_return** | [**List[NFLNFLBoxScorePlayerPuntReturnStatistic]**](NFLBoxScorePlayerPuntReturnStatistic.md) |  | [optional] 
**punting** | [**List[NFLNFLBoxScorePlayerPuntingStatistic]**](NFLBoxScorePlayerPuntingStatistic.md) |  | [optional] 
**receiving** | [**List[NFLNFLBoxScorePlayerReceivingStatistic]**](NFLBoxScorePlayerReceivingStatistic.md) |  | [optional] 
**rushing** | [**List[NFLNFLBoxScorePlayerRushingStatistic]**](NFLBoxScorePlayerRushingStatistic.md) |  | [optional] 
**tackles** | [**List[NFLNFLBoxScorePlayerTacklesStatistic]**](NFLBoxScorePlayerTacklesStatistic.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_boxscore import NFLTeamBoxscore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamBoxscore from a JSON string
nfl_team_boxscore_instance = NFLTeamBoxscore.from_json(json)
# print the JSON string representation of the object
print(NFLTeamBoxscore.to_json())

# convert the object into a dict
nfl_team_boxscore_dict = nfl_team_boxscore_instance.to_dict()
# create an instance of NFLTeamBoxscore from a dict
nfl_team_boxscore_from_dict = NFLTeamBoxscore.from_dict(nfl_team_boxscore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


