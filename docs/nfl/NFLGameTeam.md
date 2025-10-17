# NFLGameTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_logo** | **str** | URL to team logo (may contain formatInstructions placeholder) | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**score** | [**NFLNFLGameTeamScore**](NFLGameTeamScore.md) |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_game_team import NFLGameTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameTeam from a JSON string
nfl_game_team_instance = NFLGameTeam.from_json(json)
# print the JSON string representation of the object
print(NFLGameTeam.to_json())

# convert the object into a dict
nfl_game_team_dict = nfl_game_team_instance.to_dict()
# create an instance of NFLGameTeam from a dict
nfl_game_team_from_dict = NFLGameTeam.from_dict(nfl_game_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


