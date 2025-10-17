# RushingMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outside_right** | [**RushLocationMapEntry**](RushLocationMapEntry.md) |  | [optional] 
**outside_left** | [**RushLocationMapEntry**](RushLocationMapEntry.md) |  | [optional] 
**inside_left** | [**RushLocationMapEntry**](RushLocationMapEntry.md) |  | [optional] 
**inside_right** | [**RushLocationMapEntry**](RushLocationMapEntry.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.rushing_map import RushingMap

# TODO update the JSON string below
json = "{}"
# create an instance of RushingMap from a JSON string
rushing_map_instance = RushingMap.from_json(json)
# print the JSON string representation of the object
print(RushingMap.to_json())

# convert the object into a dict
rushing_map_dict = rushing_map_instance.to_dict()
# create an instance of RushingMap from a dict
rushing_map_from_dict = RushingMap.from_dict(rushing_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


