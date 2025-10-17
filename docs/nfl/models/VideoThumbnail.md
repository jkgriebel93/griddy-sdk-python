# VideoThumbnail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_url** | **str** | Video thumbnail image URL | [optional] 

## Example

```python
from src.griddy.nfl.models.video_thumbnail import VideoThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of VideoThumbnail from a JSON string
video_thumbnail_instance = VideoThumbnail.from_json(json)
# print the JSON string representation of the object
print(VideoThumbnail.to_json())

# convert the object into a dict
video_thumbnail_dict = video_thumbnail_instance.to_dict()
# create an instance of VideoThumbnail from a dict
video_thumbnail_from_dict = VideoThumbnail.from_dict(video_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


