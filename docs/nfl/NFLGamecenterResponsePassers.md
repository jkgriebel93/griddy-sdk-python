# NFLGamecenterResponsePassers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**NFLNFLPasserStats**](NFLPasserStats.md) |  | [optional] 
**visitor** | [**NFLNFLPasserStats**](NFLPasserStats.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_gamecenter_response_passers import NFLGamecenterResponsePassers

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGamecenterResponsePassers from a JSON string
nfl_gamecenter_response_passers_instance = NFLGamecenterResponsePassers.from_json(json)
# print the JSON string representation of the object
print(NFLGamecenterResponsePassers.to_json())

# convert the object into a dict
nfl_gamecenter_response_passers_dict = nfl_gamecenter_response_passers_instance.to_dict()
# create an instance of NFLGamecenterResponsePassers from a dict
nfl_gamecenter_response_passers_from_dict = NFLGamecenterResponsePassers.from_dict(nfl_gamecenter_response_passers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


