# BoxScoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game** | [**Game**](Game.md) |  | [optional] 
**player_stats** | [**BoxScoreResponsePlayerStats**](BoxScoreResponsePlayerStats.md) |  | [optional] 
**scoring_summary** | [**List[ScoringPlay]**](ScoringPlay.md) |  | [optional] 
**team_stats** | [**BoxScoreResponseTeamStats**](BoxScoreResponseTeamStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_response import BoxScoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScoreResponse from a JSON string
box_score_response_instance = BoxScoreResponse.from_json(json)
# print the JSON string representation of the object
print(BoxScoreResponse.to_json())

# convert the object into a dict
box_score_response_dict = box_score_response_instance.to_dict()
# create an instance of BoxScoreResponse from a dict
box_score_response_from_dict = BoxScoreResponse.from_dict(box_score_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


