# NFLVideoTag

Video tag information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **str** | Game identifier (for game tags) | [optional] 
**person_id** | **str** | Person identifier (for player tags) | [optional] 
**season** | **str** | Season year (for game tags) | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**slug** | **str** | URL-friendly tag identifier | [optional] 
**team_id** | **str** | Team identifier (for team tags) | [optional] 
**title** | **str** | Tag title | [optional] 
**week** | **str** | Week number (for game tags) | [optional] 

## Example

```python
from nfl.models.nfl_video_tag import NFLVideoTag

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVideoTag from a JSON string
nfl_video_tag_instance = NFLVideoTag.from_json(json)
# print the JSON string representation of the object
print(NFLVideoTag.to_json())

# convert the object into a dict
nfl_video_tag_dict = nfl_video_tag_instance.to_dict()
# create an instance of NFLVideoTag from a dict
nfl_video_tag_from_dict = NFLVideoTag.from_dict(nfl_video_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


