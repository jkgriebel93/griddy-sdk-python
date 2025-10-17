# BoxscoreScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_team_score** | [**TeamScore**](TeamScore.md) |  | [optional] 
**phase** | **str** | Game phase (P&#x3D;Pregame, 1-4&#x3D;Quarter, F&#x3D;Final) | [optional] 
**visitor_team_score** | [**TeamScore**](TeamScore.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.boxscore_score import BoxscoreScore

# TODO update the JSON string below
json = "{}"
# create an instance of BoxscoreScore from a JSON string
boxscore_score_instance = BoxscoreScore.from_json(json)
# print the JSON string representation of the object
print(BoxscoreScore.to_json())

# convert the object into a dict
boxscore_score_dict = boxscore_score_instance.to_dict()
# create an instance of BoxscoreScore from a dict
boxscore_score_from_dict = BoxscoreScore.from_dict(boxscore_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


