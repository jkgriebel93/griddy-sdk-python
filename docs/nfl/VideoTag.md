# VideoTag

Video tag information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** | Game identifier (for game tags) | [optional] 
**person_id** | **str** | Person identifier (for player tags) | [optional] 
**season** | **str** | Season year (for game tags) | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**slug** | **str** | URL-friendly tag identifier | [optional] 
**team_id** | **str** | Team identifier (for team tags) | [optional] 
**title** | **str** | Tag title | [optional] 
**week** | **str** | Week number (for game tags) | [optional] 

## Example

```python
from src.griddy.nfl.models.video_tag import VideoTag

# TODO update the JSON string below
json = "{}"
# create an instance of VideoTag from a JSON string
video_tag_instance = VideoTag.from_json(json)
# print the JSON string representation of the object
print(VideoTag.to_json())

# convert the object into a dict
video_tag_dict = video_tag_instance.to_dict()
# create an instance of VideoTag from a dict
video_tag_from_dict = VideoTag.from_dict(video_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


