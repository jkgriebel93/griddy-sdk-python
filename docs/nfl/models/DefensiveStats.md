# DefensiveStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assisted_tackles** | **int** |  | [optional] 
**forced_fumbles** | **int** |  | [optional] 
**fumble_recoveries** | **int** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**passes_defended** | **int** |  | [optional] 
**qb_hits** | **int** |  | [optional] 
**sacks** | **float** |  | [optional] 
**safeties** | **int** |  | [optional] 
**solo_tackles** | **int** |  | [optional] 
**tackles** | **int** |  | [optional] 
**tackles_for_loss** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_stats import DefensiveStats

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveStats from a JSON string
defensive_stats_instance = DefensiveStats.from_json(json)
# print the JSON string representation of the object
print(DefensiveStats.to_json())

# convert the object into a dict
defensive_stats_dict = defensive_stats_instance.to_dict()
# create an instance of DefensiveStats from a dict
defensive_stats_from_dict = DefensiveStats.from_dict(defensive_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


