# BroadcastInfoStreamingNetworksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_network** | **str** | Primary streaming network | [optional] 
**networks** | **List[str]** | Available streaming networks | [optional] 

## Example

```python
from src.griddy.nfl.models.broadcast_info_streaming_networks_inner import BroadcastInfoStreamingNetworksInner

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastInfoStreamingNetworksInner from a JSON string
broadcast_info_streaming_networks_inner_instance = BroadcastInfoStreamingNetworksInner.from_json(json)
# print the JSON string representation of the object
print(BroadcastInfoStreamingNetworksInner.to_json())

# convert the object into a dict
broadcast_info_streaming_networks_inner_dict = broadcast_info_streaming_networks_inner_instance.to_dict()
# create an instance of BroadcastInfoStreamingNetworksInner from a dict
broadcast_info_streaming_networks_inner_from_dict = BroadcastInfoStreamingNetworksInner.from_dict(broadcast_info_streaming_networks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


