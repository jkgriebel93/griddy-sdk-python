# NFLGamecenterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaders** | [**NFLNFLGamecenterResponseLeaders**](NFLGamecenterResponseLeaders.md) |  | [optional] 
**pass_rushers** | [**NFLNFLGamecenterResponsePassRushers**](NFLGamecenterResponsePassRushers.md) |  | [optional] 
**passers** | [**NFLNFLGamecenterResponsePassers**](NFLGamecenterResponsePassers.md) |  | [optional] 
**receivers** | [**NFLNFLGamecenterResponseReceivers**](NFLGamecenterResponseReceivers.md) |  | [optional] 
**rushers** | [**NFLNFLGamecenterResponseRushers**](NFLGamecenterResponseRushers.md) |  | [optional] 
**schedule** | [**NFLNFLGamecenterSchedule**](NFLGamecenterSchedule.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response import NFLGamecenterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponse from a JSON string
nfl_gamecenter_response_instance = NFLGamecenterResponse.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponse.to_json())

# convert the object into a dict
nfl_gamecenter_response_dict = nfl_gamecenter_response_instance.to_dict()
# create an instance of NFLGamecenterResponse from a dict
nfl_gamecenter_response_from_dict = NFLGamecenterResponse.from_dict(nfl_gamecenter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


