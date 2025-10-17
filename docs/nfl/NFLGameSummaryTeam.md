# NFLGameSummaryTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | [optional] 
**has_possession** | **bool** |  | [optional] 
**score** | [**NFLNFLGameSummaryTeamScore**](NFLGameSummaryTeamScore.md) |  | [optional] 
**timeouts** | [**NFLNFLGameSummaryTeamTimeouts**](NFLGameSummaryTeamTimeouts.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_game_summary_team import NFLGameSummaryTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameSummaryTeam from a JSON string
nfl_game_summary_team_instance = NFLGameSummaryTeam.from_json(json)
# print the JSON string representation of the object
print(NFLGameSummaryTeam.to_json())

# convert the object into a dict
nfl_game_summary_team_dict = nfl_game_summary_team_instance.to_dict()
# create an instance of NFLGameSummaryTeam from a dict
nfl_game_summary_team_from_dict = NFLGameSummaryTeam.from_dict(nfl_game_summary_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


