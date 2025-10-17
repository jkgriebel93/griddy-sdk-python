# NFLGamecenterResponseLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pass_distance_leaders** | [**NFLNFLGamecenterResponseLeadersPassDistanceLeaders**](NFLGamecenterResponseLeadersPassDistanceLeaders.md) |  | [optional] 
**speed_leaders** | [**NFLNFLGamecenterResponseLeadersSpeedLeaders**](NFLGamecenterResponseLeadersSpeedLeaders.md) |  | [optional] 
**time_to_sack_leaders** | [**NFLNFLGamecenterResponseLeadersTimeToSackLeaders**](NFLGamecenterResponseLeadersTimeToSackLeaders.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_leaders import NFLGamecenterResponseLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseLeaders from a JSON string
nfl_gamecenter_response_leaders_instance = NFLGamecenterResponseLeaders.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseLeaders.to_json())

# convert the object into a dict
nfl_gamecenter_response_leaders_dict = nfl_gamecenter_response_leaders_instance.to_dict()
# create an instance of NFLGamecenterResponseLeaders from a dict
nfl_gamecenter_response_leaders_from_dict = NFLGamecenterResponseLeaders.from_dict(nfl_gamecenter_response_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


