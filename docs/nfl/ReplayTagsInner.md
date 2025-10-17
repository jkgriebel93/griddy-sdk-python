# ReplayTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** |  | [optional] 
**season** | **str** |  | [optional] 
**season_type** | **str** |  | [optional] 
**week** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.replay_tags_inner import ReplayTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayTagsInner from a JSON string
replay_tags_inner_instance = ReplayTagsInner.from_json(json)
# print the JSON string representation of the object
print(ReplayTagsInner.to_json())

# convert the object into a dict
replay_tags_inner_dict = replay_tags_inner_instance.to_dict()
# create an instance of ReplayTagsInner from a dict
replay_tags_inner_from_dict = ReplayTagsInner.from_dict(replay_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


