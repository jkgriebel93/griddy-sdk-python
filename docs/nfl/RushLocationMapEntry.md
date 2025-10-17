# RushLocationMapEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yards** | **int** |  | [optional] 
**attempts** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**avg_distance** | **float** |  | [optional] 
**avg_time_to_los** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.rush_location_map_entry import RushLocationMapEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RushLocationMapEntry from a JSON string
rush_location_map_entry_instance = RushLocationMapEntry.from_json(json)
# print the JSON string representation of the object
print(RushLocationMapEntry.to_json())

# convert the object into a dict
rush_location_map_entry_dict = rush_location_map_entry_instance.to_dict()
# create an instance of RushLocationMapEntry from a dict
rush_location_map_entry_from_dict = RushLocationMapEntry.from_dict(rush_location_map_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


