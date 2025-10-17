# BroadcastInfoInternationalWatchOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcasters** | **List[str]** |  | [optional] 
**country_code** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.broadcast_info_international_watch_options_inner import BroadcastInfoInternationalWatchOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastInfoInternationalWatchOptionsInner from a JSON string
broadcast_info_international_watch_options_inner_instance = BroadcastInfoInternationalWatchOptionsInner.from_json(json)
# print the JSON string representation of the object
print(BroadcastInfoInternationalWatchOptionsInner.to_json())

# convert the object into a dict
broadcast_info_international_watch_options_inner_dict = broadcast_info_international_watch_options_inner_instance.to_dict()
# create an instance of BroadcastInfoInternationalWatchOptionsInner from a dict
broadcast_info_international_watch_options_inner_from_dict = BroadcastInfoInternationalWatchOptionsInner.from_dict(broadcast_info_international_watch_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


