# NFLBroadcastInfoStreamingNetworksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_network** | **str** | Primary streaming network | [optional] 
**networks** | **List[str]** | Available streaming networks | [optional] 

## Example

```python
from nfl.models.nfl_broadcast_info_streaming_networks_inner import NFLBroadcastInfoStreamingNetworksInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBroadcastInfoStreamingNetworksInner from a JSON string
nfl_broadcast_info_streaming_networks_inner_instance = NFLBroadcastInfoStreamingNetworksInner.from_json(json)
# print the JSON string representation of the object
print(NFLBroadcastInfoStreamingNetworksInner.to_json())

# convert the object into a dict
nfl_broadcast_info_streaming_networks_inner_dict = nfl_broadcast_info_streaming_networks_inner_instance.to_dict()
# create an instance of NFLBroadcastInfoStreamingNetworksInner from a dict
nfl_broadcast_info_streaming_networks_inner_from_dict = NFLBroadcastInfoStreamingNetworksInner.from_dict(nfl_broadcast_info_streaming_networks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


