# NFLGamecenterResponseLeadersSpeedLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLSpeedLeaderEntry]**](NFLSpeedLeaderEntry.md) |  | [optional] 
**visitor** | [**List[NFLNFLSpeedLeaderEntry]**](NFLSpeedLeaderEntry.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_leaders_speed_leaders import NFLGamecenterResponseLeadersSpeedLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseLeadersSpeedLeaders from a JSON string
nfl_gamecenter_response_leaders_speed_leaders_instance = NFLGamecenterResponseLeadersSpeedLeaders.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseLeadersSpeedLeaders.to_json())

# convert the object into a dict
nfl_gamecenter_response_leaders_speed_leaders_dict = nfl_gamecenter_response_leaders_speed_leaders_instance.to_dict()
# create an instance of NFLGamecenterResponseLeadersSpeedLeaders from a dict
nfl_gamecenter_response_leaders_speed_leaders_from_dict = NFLGamecenterResponseLeadersSpeedLeaders.from_dict(nfl_gamecenter_response_leaders_speed_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


