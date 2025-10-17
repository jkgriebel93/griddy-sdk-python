# NFLRushingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**avg_distance** | **float** |  | [optional] 
**avg_time_to_los** | **float** |  | [optional] 
**rush_location_map** | [**NFLNFLRushingMap**](NFLRushingMap.md) |  | [optional] 
**pre_snap_rush_location_map** | [**NFLNFLRushingMap**](NFLRushingMap.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_rushing_info import NFLRushingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRushingInfo from a JSON string
nfl_rushing_info_instance = NFLRushingInfo.from_json(json)
# print the JSON string representation of the object
print(NFLRushingInfo.to_json())

# convert the object into a dict
nfl_rushing_info_dict = nfl_rushing_info_instance.to_dict()
# create an instance of NFLRushingInfo from a dict
nfl_rushing_info_from_dict = NFLRushingInfo.from_dict(nfl_rushing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


