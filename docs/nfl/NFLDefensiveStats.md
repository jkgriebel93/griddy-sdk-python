# NFLDefensiveStats


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
from nfl.models.nfl_defensive_stats import NFLDefensiveStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveStats from a JSON string
nfl_defensive_stats_instance = NFLDefensiveStats.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveStats.to_json())

# convert the object into a dict
nfl_defensive_stats_dict = nfl_defensive_stats_instance.to_dict()
# create an instance of NFLDefensiveStats from a dict
nfl_defensive_stats_from_dict = NFLDefensiveStats.from_dict(nfl_defensive_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


