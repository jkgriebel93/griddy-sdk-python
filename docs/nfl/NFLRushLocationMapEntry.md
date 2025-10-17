# NFLRushLocationMapEntry


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
from nfl.models.nfl_rush_location_map_entry import NFLRushLocationMapEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRushLocationMapEntry from a JSON string
nfl_rush_location_map_entry_instance = NFLRushLocationMapEntry.from_json(json)
# print the JSON string representation of the object
print(NFLRushLocationMapEntry.to_json())

# convert the object into a dict
nfl_rush_location_map_entry_dict = nfl_rush_location_map_entry_instance.to_dict()
# create an instance of NFLRushLocationMapEntry from a dict
nfl_rush_location_map_entry_from_dict = NFLRushLocationMapEntry.from_dict(nfl_rush_location_map_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


