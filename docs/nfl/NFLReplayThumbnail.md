# NFLReplayThumbnail

Video thumbnail information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_url** | **str** | URL to video thumbnail image | [optional] 

## Example

```python
from nfl.models.nfl_replay_thumbnail import NFLReplayThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReplayThumbnail from a JSON string
nfl_replay_thumbnail_instance = NFLReplayThumbnail.from_json(json)
# print the JSON string representation of the object
print(NFLReplayThumbnail.to_json())

# convert the object into a dict
nfl_replay_thumbnail_dict = nfl_replay_thumbnail_instance.to_dict()
# create an instance of NFLReplayThumbnail from a dict
nfl_replay_thumbnail_from_dict = NFLReplayThumbnail.from_dict(nfl_replay_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


