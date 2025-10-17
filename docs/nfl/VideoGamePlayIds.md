# VideoGamePlayIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team_id** | **str** | Away team UUID | [optional] 
**game_id** | **str** | Game UUID | [optional] 
**home_team_id** | **str** | Home team UUID | [optional] 
**play_id** | **str** | Play identifier | [optional] 

## Example

```python
from src.griddy.nfl.models.video_game_play_ids import VideoGamePlayIds

# TODO update the JSON string below
json = "{}"
# create an instance of VideoGamePlayIds from a JSON string
video_game_play_ids_instance = VideoGamePlayIds.from_json(json)
# print the JSON string representation of the object
print(VideoGamePlayIds.to_json())

# convert the object into a dict
video_game_play_ids_dict = video_game_play_ids_instance.to_dict()
# create an instance of VideoGamePlayIds from a dict
video_game_play_ids_from_dict = VideoGamePlayIds.from_dict(video_game_play_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


