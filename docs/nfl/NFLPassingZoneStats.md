# NFLPassingZoneStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**line_of_scrimmage_distance** | [**NFLNFLLineOfScrimmageDistanceEnum**](NFLLineOfScrimmageDistanceEnum.md) |  | [optional] 
**section** | [**NFLNFLPassingSectionEnum**](NFLPassingSectionEnum.md) |  | [optional] 
**attempts** | **int** |  | [optional] 
**completion_pct** | **float** |  | [optional] 
**completions** | **int** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**qb_rating** | **float** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**qb_rating_success_level** | [**NFLNFLSuccessLevelEnum**](NFLSuccessLevelEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_passing_zone_stats import NFLPassingZoneStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassingZoneStats from a JSON string
nfl_passing_zone_stats_instance = NFLPassingZoneStats.from_json(json)
# print the JSON string representation of the object
print(NFLPassingZoneStats.to_json())

# convert the object into a dict
nfl_passing_zone_stats_dict = nfl_passing_zone_stats_instance.to_dict()
# create an instance of NFLPassingZoneStats from a dict
nfl_passing_zone_stats_from_dict = NFLPassingZoneStats.from_dict(nfl_passing_zone_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


