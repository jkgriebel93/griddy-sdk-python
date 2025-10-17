# NFLRushingStats


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
from nfl.models.nfl_rushing_stats import NFLRushingStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRushingStats from a JSON string
nfl_rushing_stats_instance = NFLRushingStats.from_json(json)
# print the JSON string representation of the object
print(NFLRushingStats.to_json())

# convert the object into a dict
nfl_rushing_stats_dict = nfl_rushing_stats_instance.to_dict()
# create an instance of NFLRushingStats from a dict
nfl_rushing_stats_from_dict = NFLRushingStats.from_dict(nfl_rushing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


