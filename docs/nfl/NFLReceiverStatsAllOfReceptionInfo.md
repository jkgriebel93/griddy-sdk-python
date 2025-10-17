# NFLReceiverStatsAllOfReceptionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_air_yards** | **float** |  | [optional] 
**avg_cushion** | **float** |  | [optional] 
**avg_separation** | **float** |  | [optional] 

## Example

```python
from nfl.models.nfl_receiver_stats_all_of_reception_info import NFLReceiverStatsAllOfReceptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReceiverStatsAllOfReceptionInfo from a JSON string
nfl_receiver_stats_all_of_reception_info_instance = NFLReceiverStatsAllOfReceptionInfo.from_json(json)
# print the JSON string representation of the object
print(NFLReceiverStatsAllOfReceptionInfo.to_json())

# convert the object into a dict
nfl_receiver_stats_all_of_reception_info_dict = nfl_receiver_stats_all_of_reception_info_instance.to_dict()
# create an instance of NFLReceiverStatsAllOfReceptionInfo from a dict
nfl_receiver_stats_all_of_reception_info_from_dict = NFLReceiverStatsAllOfReceptionInfo.from_dict(nfl_receiver_stats_all_of_reception_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


