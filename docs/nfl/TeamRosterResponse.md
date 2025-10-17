# TeamRosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** | Season year | [optional] 
**team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**team_players** | [**List[Player]**](Player.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_roster_response import TeamRosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRosterResponse from a JSON string
team_roster_response_instance = TeamRosterResponse.from_json(json)
# print the JSON string representation of the object
print(TeamRosterResponse.to_json())

# convert the object into a dict
team_roster_response_dict = team_roster_response_instance.to_dict()
# create an instance of TeamRosterResponse from a dict
team_roster_response_from_dict = TeamRosterResponse.from_dict(team_roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


