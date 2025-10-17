# NFLSeasonStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defensive** | [**NFLNFLDefensiveStats**](NFLDefensiveStats.md) |  | [optional] 
**games** | **int** |  | [optional] 
**kicking** | [**NFLNFLKickingStats**](NFLKickingStats.md) |  | [optional] 
**passing** | [**NFLNFLPassingStats**](NFLPassingStats.md) |  | [optional] 
**receiving** | [**NFLNFLReceivingStats**](NFLReceivingStats.md) |  | [optional] 
**rushing** | [**NFLNFLRushingStats**](NFLRushingStats.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**starts** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_season_stats import NFLSeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLSeasonStats from a JSON string
nfl_season_stats_instance = NFLSeasonStats.from_json(json)
# print the JSON string representation of the object
print(NFLSeasonStats.to_json())

# convert the object into a dict
nfl_season_stats_dict = nfl_season_stats_instance.to_dict()
# create an instance of NFLSeasonStats from a dict
nfl_season_stats_from_dict = NFLSeasonStats.from_dict(nfl_season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


