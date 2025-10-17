# NFLLiveGameAwayTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** |  | [optional] 
**score** | **int** |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_live_game_away_team import NFLLiveGameAwayTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLLiveGameAwayTeam from a JSON string
nfl_live_game_away_team_instance = NFLLiveGameAwayTeam.from_json(json)
# print the JSON string representation of the object
print(NFLLiveGameAwayTeam.to_json())

# convert the object into a dict
nfl_live_game_away_team_dict = nfl_live_game_away_team_instance.to_dict()
# create an instance of NFLLiveGameAwayTeam from a dict
nfl_live_game_away_team_from_dict = NFLLiveGameAwayTeam.from_dict(nfl_live_game_away_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


