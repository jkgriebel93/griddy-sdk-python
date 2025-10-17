# NFLFilmroomPlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense_team_id** | **str** | Defensive team identifier | [optional] 
**down** | **int** | Down number | [optional] 
**fapi_game_id** | **str** | Football API game identifier | [optional] 
**game_clock** | **str** | Game clock time when play occurred | [optional] 
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**home_team_abbr** | **str** | Home team abbreviation | [optional] 
**home_team_id** | **str** | Home team identifier | [optional] 
**play_description** | **str** | Detailed description of the play | [optional] 
**play_id** | **int** | Unique play identifier within the game | [optional] 
**play_type** | [**NFLNFLPlayTypeEnum**](NFLPlayTypeEnum.md) |  | [optional] 
**possession_team_id** | **str** | Team with possession of the ball | [optional] 
**quarter** | **int** | Quarter of the play | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**selected_param_values** | **Dict[str, object]** | Selected parameter values for the play filter | [optional] 
**sequence** | **int** | Play sequence number | [optional] 
**visitor_team_abbr** | **str** | Visiting team abbreviation | [optional] 
**visitor_team_id** | **str** | Visiting team identifier | [optional] 
**week** | **int** | Week number | [optional] 
**week_slug** | [**NFLNFLWeekSlugEnum**](NFLWeekSlugEnum.md) |  | [optional] 
**yardline** | **str** | Field position where play occurred | [optional] 
**yards_to_go** | **int** | Yards needed for first down | [optional] 

## Example

```python
from nfl.models.nfl_filmroom_play import NFLFilmroomPlay

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFilmroomPlay from a JSON string
nfl_filmroom_play_instance = NFLFilmroomPlay.from_json(json)
# print the JSON string representation of the object
print(NFLFilmroomPlay.to_json())

# convert the object into a dict
nfl_filmroom_play_dict = nfl_filmroom_play_instance.to_dict()
# create an instance of NFLFilmroomPlay from a dict
nfl_filmroom_play_from_dict = NFLFilmroomPlay.from_dict(nfl_filmroom_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


