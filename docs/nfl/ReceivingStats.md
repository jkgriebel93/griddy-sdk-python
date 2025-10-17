# ReceivingStats


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
from src.griddy.nfl.models.receiving_stats import ReceivingStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingStats from a JSON string
receiving_stats_instance = ReceivingStats.from_json(json)
# print the JSON string representation of the object
print(ReceivingStats.to_json())

# convert the object into a dict
receiving_stats_dict = receiving_stats_instance.to_dict()
# create an instance of ReceivingStats from a dict
receiving_stats_from_dict = ReceivingStats.from_dict(receiving_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


