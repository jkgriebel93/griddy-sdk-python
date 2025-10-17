# NFLVideoGamePlayIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team_id** | **str** | Away team UUID | [optional] 
**game_id** | **str** | Game UUID | [optional] 
**home_team_id** | **str** | Home team UUID | [optional] 
**play_id** | **str** | Play identifier | [optional] 

## Example

```python
from nfl.models.nfl_video_game_play_ids import NFLVideoGamePlayIds

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVideoGamePlayIds from a JSON string
nfl_video_game_play_ids_instance = NFLVideoGamePlayIds.from_json(json)
# print the JSON string representation of the object
print(NFLVideoGamePlayIds.to_json())

# convert the object into a dict
nfl_video_game_play_ids_dict = nfl_video_game_play_ids_instance.to_dict()
# create an instance of NFLVideoGamePlayIds from a dict
nfl_video_game_play_ids_from_dict = NFLVideoGamePlayIds.from_dict(nfl_video_game_play_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


