# NFLGameSummaryTeamTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining** | **int** |  | [optional] 
**used** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_game_summary_team_timeouts import NFLGameSummaryTeamTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameSummaryTeamTimeouts from a JSON string
nfl_game_summary_team_timeouts_instance = NFLGameSummaryTeamTimeouts.from_json(json)
# print the JSON string representation of the object
print(NFLGameSummaryTeamTimeouts.to_json())

# convert the object into a dict
nfl_game_summary_team_timeouts_dict = nfl_game_summary_team_timeouts_instance.to_dict()
# create an instance of NFLGameSummaryTeamTimeouts from a dict
nfl_game_summary_team_timeouts_from_dict = NFLGameSummaryTeamTimeouts.from_dict(nfl_game_summary_team_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


