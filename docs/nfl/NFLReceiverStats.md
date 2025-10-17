# NFLReceiverStats


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
**position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**rec_yards** | **int** |  | [optional] 
**targets** | **int** |  | [optional] 
**receptions** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**reception_info** | [**NFLNFLReceiverStatsAllOfReceptionInfo**](NFLReceiverStatsAllOfReceptionInfo.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_receiver_stats import NFLReceiverStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReceiverStats from a JSON string
nfl_receiver_stats_instance = NFLReceiverStats.from_json(json)
# print the JSON string representation of the object
print(NFLReceiverStats.to_json())

# convert the object into a dict
nfl_receiver_stats_dict = nfl_receiver_stats_instance.to_dict()
# create an instance of NFLReceiverStats from a dict
nfl_receiver_stats_from_dict = NFLReceiverStats.from_dict(nfl_receiver_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


