# GamecenterResponseLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_distance_leaders** | [**GamecenterResponseLeadersPassDistanceLeaders**](GamecenterResponseLeadersPassDistanceLeaders.md) |  | [optional] 
**speed_leaders** | [**GamecenterResponseLeadersSpeedLeaders**](GamecenterResponseLeadersSpeedLeaders.md) |  | [optional] 
**time_to_sack_leaders** | [**GamecenterResponseLeadersTimeToSackLeaders**](GamecenterResponseLeadersTimeToSackLeaders.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_leaders import GamecenterResponseLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponseLeaders from a JSON string
gamecenter_response_leaders_instance = GamecenterResponseLeaders.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponseLeaders.to_json())

# convert the object into a dict
gamecenter_response_leaders_dict = gamecenter_response_leaders_instance.to_dict()
# create an instance of GamecenterResponseLeaders from a dict
gamecenter_response_leaders_from_dict = GamecenterResponseLeaders.from_dict(gamecenter_response_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


