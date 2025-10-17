# ReceiverStatsAllOfReceptionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_air_yards** | **float** |  | [optional] 
**avg_cushion** | **float** |  | [optional] 
**avg_separation** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.receiver_stats_all_of_reception_info import ReceiverStatsAllOfReceptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiverStatsAllOfReceptionInfo from a JSON string
receiver_stats_all_of_reception_info_instance = ReceiverStatsAllOfReceptionInfo.from_json(json)
# print the JSON string representation of the object
print(ReceiverStatsAllOfReceptionInfo.to_json())

# convert the object into a dict
receiver_stats_all_of_reception_info_dict = receiver_stats_all_of_reception_info_instance.to_dict()
# create an instance of ReceiverStatsAllOfReceptionInfo from a dict
receiver_stats_all_of_reception_info_from_dict = ReceiverStatsAllOfReceptionInfo.from_dict(receiver_stats_all_of_reception_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


