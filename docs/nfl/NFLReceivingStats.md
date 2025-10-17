# NFLReceivingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drops** | **int** |  | [optional] 
**long_reception** | **int** |  | [optional] 
**receptions** | **int** |  | [optional] 
**targets** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**yards_per_reception** | **float** |  | [optional] 

## Example

```python
from nfl.models.nfl_receiving_stats import NFLReceivingStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReceivingStats from a JSON string
nfl_receiving_stats_instance = NFLReceivingStats.from_json(json)
# print the JSON string representation of the object
print(NFLReceivingStats.to_json())

# convert the object into a dict
nfl_receiving_stats_dict = nfl_receiving_stats_instance.to_dict()
# create an instance of NFLReceivingStats from a dict
nfl_receiving_stats_from_dict = NFLReceivingStats.from_dict(nfl_receiving_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


