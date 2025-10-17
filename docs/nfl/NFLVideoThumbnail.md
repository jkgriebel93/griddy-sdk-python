# NFLVideoThumbnail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_url** | **str** | Video thumbnail image URL | [optional] 

## Example

```python
from nfl.models.nfl_video_thumbnail import NFLVideoThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVideoThumbnail from a JSON string
nfl_video_thumbnail_instance = NFLVideoThumbnail.from_json(json)
# print the JSON string representation of the object
print(NFLVideoThumbnail.to_json())

# convert the object into a dict
nfl_video_thumbnail_dict = nfl_video_thumbnail_instance.to_dict()
# create an instance of NFLVideoThumbnail from a dict
nfl_video_thumbnail_from_dict = NFLVideoThumbnail.from_dict(nfl_video_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


