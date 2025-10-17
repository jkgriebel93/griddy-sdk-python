# GamecenterResponsePassers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**PasserStats**](PasserStats.md) |  | [optional] 
**visitor** | [**PasserStats**](PasserStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.gamecenter_response_passers import GamecenterResponsePassers

# TODO update the JSON string below
json = "{}"
# create an instance of GamecenterResponsePassers from a JSON string
gamecenter_response_passers_instance = GamecenterResponsePassers.from_json(json)
# print the JSON string representation of the object
print(GamecenterResponsePassers.to_json())

# convert the object into a dict
gamecenter_response_passers_dict = gamecenter_response_passers_instance.to_dict()
# create an instance of GamecenterResponsePassers from a dict
gamecenter_response_passers_from_dict = GamecenterResponsePassers.from_dict(gamecenter_response_passers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


