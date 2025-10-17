# RushingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carries** | **int** |  | [optional] 
**fumbles** | **int** |  | [optional] 
**long_rush** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**yards_per_carry** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.rushing_stats import RushingStats

# TODO update the JSON string below
json = "{}"
# create an instance of RushingStats from a JSON string
rushing_stats_instance = RushingStats.from_json(json)
# print the JSON string representation of the object
print(RushingStats.to_json())

# convert the object into a dict
rushing_stats_dict = rushing_stats_instance.to_dict()
# create an instance of RushingStats from a dict
rushing_stats_from_dict = RushingStats.from_dict(rushing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


