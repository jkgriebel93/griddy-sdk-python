# BoxScoreResponseTeamStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**TeamGameStats**](TeamGameStats.md) |  | [optional] 
**home** | [**TeamGameStats**](TeamGameStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_response_team_stats import BoxScoreResponseTeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScoreResponseTeamStats from a JSON string
box_score_response_team_stats_instance = BoxScoreResponseTeamStats.from_json(json)
# print the JSON string representation of the object
print(BoxScoreResponseTeamStats.to_json())

# convert the object into a dict
box_score_response_team_stats_dict = box_score_response_team_stats_instance.to_dict()
# create an instance of BoxScoreResponseTeamStats from a dict
box_score_response_team_stats_from_dict = BoxScoreResponseTeamStats.from_dict(box_score_response_team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


