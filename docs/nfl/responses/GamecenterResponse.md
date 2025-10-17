# GamecenterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaders** | [**GamecenterResponseLeaders**](GamecenterResponseLeaders.md) |  | [optional] 
**pass_rushers** | [**GamecenterResponsePassRushers**](GamecenterResponsePassRushers.md) |  | [optional] 
**passers** | [**GamecenterResponsePassers**](GamecenterResponsePassers.md) |  | [optional] 
**receivers** | [**GamecenterResponseReceivers**](GamecenterResponseReceivers.md) |  | [optional] 
**rushers** | [**GamecenterResponseRushers**](GamecenterResponseRushers.md) |  | [optional] 
**schedule** | [**GamecenterSchedule**](GamecenterSchedule.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response import GamecenterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponse from a JSON string
gamecenter_response_instance = GamecenterResponse.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponse.to_json())

# convert the object into a dict
gamecenter_response_dict = gamecenter_response_instance.to_dict()
# create an instance of GamecenterResponse from a dict
gamecenter_response_from_dict = GamecenterResponse.from_dict(gamecenter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


