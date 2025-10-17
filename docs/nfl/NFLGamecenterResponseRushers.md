# NFLGamecenterResponseRushers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**List[NFLNFLRusherStats]**](NFLRusherStats.md) |  | [optional] 
**visitor** | [**List[NFLNFLRusherStats]**](NFLRusherStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_rushers import NFLGamecenterResponseRushers

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponseRushers from a JSON string
nfl_gamecenter_response_rushers_instance = NFLGamecenterResponseRushers.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponseRushers.to_json())

# convert the object into a dict
nfl_gamecenter_response_rushers_dict = nfl_gamecenter_response_rushers_instance.to_dict()
# create an instance of NFLGamecenterResponseRushers from a dict
nfl_gamecenter_response_rushers_from_dict = NFLGamecenterResponseRushers.from_dict(nfl_gamecenter_response_rushers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


