# NFLGameTeamScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | Total score (empty string for future games) | [optional] 

## Example

```python
from nfl.models.nfl_game_team_score import NFLGameTeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameTeamScore from a JSON string
nfl_game_team_score_instance = NFLGameTeamScore.from_json(json)
# print the JSON string representation of the object
print(NFLGameTeamScore.to_json())

# convert the object into a dict
nfl_game_team_score_dict = nfl_game_team_score_instance.to_dict()
# create an instance of NFLGameTeamScore from a dict
nfl_game_team_score_from_dict = NFLGameTeamScore.from_dict(nfl_game_team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


