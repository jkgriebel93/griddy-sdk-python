# ReceiverStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_id** | **int** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**rec_yards** | **int** |  | [optional] 
**targets** | **int** |  | [optional] 
**receptions** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**reception_info** | [**ReceiverStatsAllOfReceptionInfo**](ReceiverStatsAllOfReceptionInfo.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.receiver_stats import ReceiverStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiverStats from a JSON string
receiver_stats_instance = ReceiverStats.from_json(json)
# print the JSON string representation of the object
print(ReceiverStats.to_json())

# convert the object into a dict
receiver_stats_dict = receiver_stats_instance.to_dict()
# create an instance of ReceiverStats from a dict
receiver_stats_from_dict = ReceiverStats.from_dict(receiver_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


