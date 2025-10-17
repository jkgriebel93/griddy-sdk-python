# RushingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**avg_distance** | **float** |  | [optional] 
**avg_time_to_los** | **float** |  | [optional] 
**rush_location_map** | [**RushingMap**](RushingMap.md) |  | [optional] 
**pre_snap_rush_location_map** | [**RushingMap**](RushingMap.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.rushing_info import RushingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RushingInfo from a JSON string
rushing_info_instance = RushingInfo.from_json(json)
# print the JSON string representation of the object
print(RushingInfo.to_json())

# convert the object into a dict
rushing_info_dict = rushing_info_instance.to_dict()
# create an instance of RushingInfo from a dict
rushing_info_from_dict = RushingInfo.from_dict(rushing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


