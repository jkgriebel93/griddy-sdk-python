# ReplayThumbnail

Video thumbnail information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_url** | **str** | URL to video thumbnail image | [optional] 

## Example

```python
from src.griddy.nfl.models.replay_thumbnail import ReplayThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayThumbnail from a JSON string
replay_thumbnail_instance = ReplayThumbnail.from_json(json)
# print the JSON string representation of the object
print(ReplayThumbnail.to_json())

# convert the object into a dict
replay_thumbnail_dict = replay_thumbnail_instance.to_dict()
# create an instance of ReplayThumbnail from a dict
replay_thumbnail_from_dict = ReplayThumbnail.from_dict(replay_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


