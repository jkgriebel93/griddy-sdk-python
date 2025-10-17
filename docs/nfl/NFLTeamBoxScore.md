# NFLTeamBoxScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**NFLNFLTeamBoxscore**](NFLTeamBoxscore.md) |  | [optional] 
**game_id** | **str** | Game identifier | [optional] 
**home** | [**NFLNFLTeamBoxscore**](NFLTeamBoxscore.md) |  | [optional] 
**schedule** | [**NFLNFLBoxscoreSchedule**](NFLBoxscoreSchedule.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_box_score import NFLTeamBoxScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamBoxScore from a JSON string
nfl_team_box_score_instance = NFLTeamBoxScore.from_json(json)
# print the JSON string representation of the object
print(NFLTeamBoxScore.to_json())

# convert the object into a dict
nfl_team_box_score_dict = nfl_team_box_score_instance.to_dict()
# create an instance of NFLTeamBoxScore from a dict
nfl_team_box_score_from_dict = NFLTeamBoxScore.from_dict(nfl_team_box_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


