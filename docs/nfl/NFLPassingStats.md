# NFLPassingStats


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
from nfl.models.nfl_passing_stats import NFLPassingStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassingStats from a JSON string
nfl_passing_stats_instance = NFLPassingStats.from_json(json)
# print the JSON string representation of the object
print(NFLPassingStats.to_json())

# convert the object into a dict
nfl_passing_stats_dict = nfl_passing_stats_instance.to_dict()
# create an instance of NFLPassingStats from a dict
nfl_passing_stats_from_dict = NFLPassingStats.from_dict(nfl_passing_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


