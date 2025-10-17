# NFLRushingMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outside_right** | [**NFLNFLRushLocationMapEntry**](NFLRushLocationMapEntry.md) |  | [optional] 
**outside_left** | [**NFLNFLRushLocationMapEntry**](NFLRushLocationMapEntry.md) |  | [optional] 
**inside_left** | [**NFLNFLRushLocationMapEntry**](NFLRushLocationMapEntry.md) |  | [optional] 
**inside_right** | [**NFLNFLRushLocationMapEntry**](NFLRushLocationMapEntry.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_rushing_map import NFLRushingMap

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRushingMap from a JSON string
nfl_rushing_map_instance = NFLRushingMap.from_json(json)
# print the JSON string representation of the object
print(NFLRushingMap.to_json())

# convert the object into a dict
nfl_rushing_map_dict = nfl_rushing_map_instance.to_dict()
# create an instance of NFLRushingMap from a dict
nfl_rushing_map_from_dict = NFLRushingMap.from_dict(nfl_rushing_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


