# SeasonStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defensive** | [**DefensiveStats**](DefensiveStats.md) |  | [optional] 
**games** | **int** |  | [optional] 
**kicking** | [**KickingStats**](KickingStats.md) |  | [optional] 
**passing** | [**PassingStats**](PassingStats.md) |  | [optional] 
**receiving** | [**ReceivingStats**](ReceivingStats.md) |  | [optional] 
**rushing** | [**RushingStats**](RushingStats.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**starts** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.season_stats import SeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonStats from a JSON string
season_stats_instance = SeasonStats.from_json(json)
# print the JSON string representation of the object
print(SeasonStats.to_json())

# convert the object into a dict
season_stats_dict = season_stats_instance.to_dict()
# create an instance of SeasonStats from a dict
season_stats_from_dict = SeasonStats.from_dict(season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


