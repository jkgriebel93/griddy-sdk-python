# NFLGamecenterResponseLeadersPassDistanceLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLPassDistanceLeaderEntry]**](NFLPassDistanceLeaderEntry.md) |  | [optional] 
**visitor** | [**List[NFLNFLPassDistanceLeaderEntry]**](NFLPassDistanceLeaderEntry.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_leaders_pass_distance_leaders import NFLGamecenterResponseLeadersPassDistanceLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseLeadersPassDistanceLeaders from a JSON string
nfl_gamecenter_response_leaders_pass_distance_leaders_instance = NFLGamecenterResponseLeadersPassDistanceLeaders.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseLeadersPassDistanceLeaders.to_json())

# convert the object into a dict
nfl_gamecenter_response_leaders_pass_distance_leaders_dict = nfl_gamecenter_response_leaders_pass_distance_leaders_instance.to_dict()
# create an instance of NFLGamecenterResponseLeadersPassDistanceLeaders from a dict
nfl_gamecenter_response_leaders_pass_distance_leaders_from_dict = NFLGamecenterResponseLeadersPassDistanceLeaders.from_dict(nfl_gamecenter_response_leaders_pass_distance_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


