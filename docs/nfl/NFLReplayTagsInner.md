# NFLReplayTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** |  | [optional] 
**season** | **str** |  | [optional] 
**season_type** | **str** |  | [optional] 
**week** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_replay_tags_inner import NFLReplayTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReplayTagsInner from a JSON string
nfl_replay_tags_inner_instance = NFLReplayTagsInner.from_json(json)
# print the JSON string representation of the object
print(NFLReplayTagsInner.to_json())

# convert the object into a dict
nfl_replay_tags_inner_dict = nfl_replay_tags_inner_instance.to_dict()
# create an instance of NFLReplayTagsInner from a dict
nfl_replay_tags_inner_from_dict = NFLReplayTagsInner.from_dict(nfl_replay_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


