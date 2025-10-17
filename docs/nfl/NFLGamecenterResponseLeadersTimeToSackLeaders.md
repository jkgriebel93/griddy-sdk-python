# NFLGamecenterResponseLeadersTimeToSackLeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLTimeToSackLeaderEntry]**](NFLTimeToSackLeaderEntry.md) |  | [optional] 
**visitor** | [**List[NFLNFLTimeToSackLeaderEntry]**](NFLTimeToSackLeaderEntry.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_leaders_time_to_sack_leaders import NFLGamecenterResponseLeadersTimeToSackLeaders

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseLeadersTimeToSackLeaders from a JSON string
nfl_gamecenter_response_leaders_time_to_sack_leaders_instance = NFLGamecenterResponseLeadersTimeToSackLeaders.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseLeadersTimeToSackLeaders.to_json())

# convert the object into a dict
nfl_gamecenter_response_leaders_time_to_sack_leaders_dict = nfl_gamecenter_response_leaders_time_to_sack_leaders_instance.to_dict()
# create an instance of NFLGamecenterResponseLeadersTimeToSackLeaders from a dict
nfl_gamecenter_response_leaders_time_to_sack_leaders_from_dict = NFLGamecenterResponseLeadersTimeToSackLeaders.from_dict(nfl_gamecenter_response_leaders_time_to_sack_leaders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


