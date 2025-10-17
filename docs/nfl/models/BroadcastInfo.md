# BroadcastInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_network_channels** | **List[str]** | Networks broadcasting in away market | [optional] 
**home_network_channels** | **List[str]** | Networks broadcasting in home market | [optional] 
**international_watch_options** | [**List[BroadcastInfoInternationalWatchOptionsInner]**](BroadcastInfoInternationalWatchOptionsInner.md) | International viewing options | [optional] 
**streaming_networks** | [**List[BroadcastInfoStreamingNetworksInner]**](BroadcastInfoStreamingNetworksInner.md) |  | [optional] 
**territory** | **str** | Broadcast territory scope | [optional] 

## Example

```python
from src.griddy.nfl.models.broadcast_info import BroadcastInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastInfo from a JSON string
broadcast_info_instance = BroadcastInfo.from_json(json)
# print the JSON string representation of the object
print(BroadcastInfo.to_json())

# convert the object into a dict
broadcast_info_dict = broadcast_info_instance.to_dict()
# create an instance of BroadcastInfo from a dict
broadcast_info_from_dict = BroadcastInfo.from_dict(broadcast_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


