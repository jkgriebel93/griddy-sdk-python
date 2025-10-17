# NFLBroadcastInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_network_channels** | **List[str]** | Networks broadcasting in away market | [optional] 
**home_network_channels** | **List[str]** | Networks broadcasting in home market | [optional] 
**international_watch_options** | [**List[NFLNFLBroadcastInfoInternationalWatchOptionsInner]**](NFLBroadcastInfoInternationalWatchOptionsInner.md) | International viewing options | [optional] 
**streaming_networks** | [**List[NFLNFLBroadcastInfoStreamingNetworksInner]**](NFLBroadcastInfoStreamingNetworksInner.md) |  | [optional] 
**territory** | **str** | Broadcast territory scope | [optional] 

## Example

```python
from nfl.models.nfl_broadcast_info import NFLBroadcastInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBroadcastInfo from a JSON string
nfl_broadcast_info_instance = NFLBroadcastInfo.from_json(json)
# print the JSON string representation of the object
print(NFLBroadcastInfo.to_json())

# convert the object into a dict
nfl_broadcast_info_dict = nfl_broadcast_info_instance.to_dict()
# create an instance of NFLBroadcastInfo from a dict
nfl_broadcast_info_from_dict = NFLBroadcastInfo.from_dict(nfl_broadcast_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


