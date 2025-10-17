# PassingZoneStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**line_of_scrimmage_distance** | [**LineOfScrimmageDistanceEnum**](LineOfScrimmageDistanceEnum.md) |  | [optional] 
**section** | [**PassingSectionEnum**](PassingSectionEnum.md) |  | [optional] 
**attempts** | **int** |  | [optional] 
**completion_pct** | **float** |  | [optional] 
**completions** | **int** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**qb_rating** | **float** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**qb_rating_success_level** | [**SuccessLevelEnum**](SuccessLevelEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.passing_zone_stats import PassingZoneStats

# TODO update the JSON string below
json = "{}"
# create an instance of PassingZoneStats from a JSON string
passing_zone_stats_instance = PassingZoneStats.from_json(json)
# print the JSON string representation of the object
print(PassingZoneStats.to_json())

# convert the object into a dict
passing_zone_stats_dict = passing_zone_stats_instance.to_dict()
# create an instance of PassingZoneStats from a dict
passing_zone_stats_from_dict = PassingZoneStats.from_dict(passing_zone_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


