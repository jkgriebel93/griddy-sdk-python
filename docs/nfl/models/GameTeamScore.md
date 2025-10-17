# GameTeamScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | Total score (empty string for future games) | [optional] 

## Example

```python
from src.griddy.nfl.models.game_team_score import GameTeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of GameTeamScore from a JSON string
game_team_score_instance = GameTeamScore.from_json(json)
# print the JSON string representation of the object
print(GameTeamScore.to_json())

# convert the object into a dict
game_team_score_dict = game_team_score_instance.to_dict()
# create an instance of GameTeamScore from a dict
game_team_score_from_dict = GameTeamScore.from_dict(game_team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


