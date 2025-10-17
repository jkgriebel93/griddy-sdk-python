# TeamRankingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_rankings** | [**TeamRankings**](TeamRankings.md) |  | [optional] 
**home_rankings** | [**TeamRankings**](TeamRankings.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_rankings_response import TeamRankingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRankingsResponse from a JSON string
team_rankings_response_instance = TeamRankingsResponse.from_json(json)
# print the JSON string representation of the object
print(TeamRankingsResponse.to_json())

# convert the object into a dict
team_rankings_response_dict = team_rankings_response_instance.to_dict()
# create an instance of TeamRankingsResponse from a dict
team_rankings_response_from_dict = TeamRankingsResponse.from_dict(team_rankings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


