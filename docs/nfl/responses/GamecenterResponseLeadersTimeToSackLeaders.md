# GamecenterResponseLeadersTimeToSackLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[TimeToSackLeaderEntry]**](TimeToSackLeaderEntry.md) |  | [optional] 
**visitor** | [**List[TimeToSackLeaderEntry]**](TimeToSackLeaderEntry.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_leaders_time_to_sack_leaders import GamecenterResponseLeadersTimeToSackLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponseLeadersTimeToSackLeaders from a JSON string
gamecenter_response_leaders_time_to_sack_leaders_instance = GamecenterResponseLeadersTimeToSackLeaders.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponseLeadersTimeToSackLeaders.to_json())

# convert the object into a dict
gamecenter_response_leaders_time_to_sack_leaders_dict = gamecenter_response_leaders_time_to_sack_leaders_instance.to_dict()
# create an instance of GamecenterResponseLeadersTimeToSackLeaders from a dict
gamecenter_response_leaders_time_to_sack_leaders_from_dict = GamecenterResponseLeadersTimeToSackLeaders.from_dict(gamecenter_response_leaders_time_to_sack_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


