# PassingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** |  | [optional] 
**completion_pct** | **float** |  | [optional] 
**completions** | **int** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**rating** | **float** |  | [optional] 
**sack_yards** | **int** |  | [optional] 
**sacks** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.passing_stats import PassingStats

# TODO update the JSON string below
json = "{}"
# create an instance of PassingStats from a JSON string
passing_stats_instance = PassingStats.from_json(json)
# print the JSON string representation of the object
print(PassingStats.to_json())

# convert the object into a dict
passing_stats_dict = passing_stats_instance.to_dict()
# create an instance of PassingStats from a dict
passing_stats_from_dict = PassingStats.from_dict(passing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


