# CareerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_stats** | [**List[SeasonStats]**](SeasonStats.md) |  | [optional] 
**total_games** | **int** |  | [optional] 
**total_starts** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.career_stats import CareerStats

# TODO update the JSON string below
json = "{}"
# create an instance of CareerStats from a JSON string
career_stats_instance = CareerStats.from_json(json)
# print the JSON string representation of the object
print(CareerStats.to_json())

# convert the object into a dict
career_stats_dict = career_stats_instance.to_dict()
# create an instance of CareerStats from a dict
career_stats_from_dict = CareerStats.from_dict(career_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


