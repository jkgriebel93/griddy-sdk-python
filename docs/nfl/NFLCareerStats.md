# NFLCareerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_stats** | [**List[NFLNFLSeasonStats]**](NFLSeasonStats.md) |  | [optional] 
**total_games** | **int** |  | [optional] 
**total_starts** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_career_stats import NFLCareerStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCareerStats from a JSON string
nfl_career_stats_instance = NFLCareerStats.from_json(json)
# print the JSON string representation of the object
print(NFLCareerStats.to_json())

# convert the object into a dict
nfl_career_stats_dict = nfl_career_stats_instance.to_dict()
# create an instance of NFLCareerStats from a dict
nfl_career_stats_from_dict = NFLCareerStats.from_dict(nfl_career_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


