# PlayDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_yardline_number** | **int** | Absolute position on 100-yard field | [optional] 
**down** | **int** | Current down (0 for kickoff) | [optional] 
**end_game_clock** | **str** | Game clock at play end | [optional] 
**expected_points** | **float** | Expected points value | [optional] 
**expected_points_added** | **float** | Expected points added on this play | [optional] 
**game_clock** | **str** | Time on game clock | [optional] 
**game_id** | **int** |  | [optional] 
**home_score** | **int** |  | [optional] 
**home_timeouts_left** | **int** | Home team timeouts remaining | [optional] 
**is_big_play** | **bool** |  | [optional] 
**is_change_of_possession** | **bool** |  | [optional] 
**is_end_quarter** | **bool** |  | [optional] 
**is_goal_to_go** | **bool** |  | [optional] 
**is_no_play** | **bool** |  | [optional] 
**is_penalty** | **bool** |  | [optional] 
**is_played_out_play** | **bool** |  | [optional] 
**is_playtime_play** | **bool** |  | [optional] 
**is_redzone_play** | **bool** |  | [optional] 
**is_st_play** | **bool** | Special teams play | [optional] 
**is_scoring** | **bool** |  | [optional] 
**play_description** | **str** | Play description without jersey numbers | [optional] 
**play_description_with_jersey_numbers** | **str** | Play description including jersey numbers | [optional] 
**play_direction** | [**PlayDirectionEnum**](PlayDirectionEnum.md) |  | [optional] 
**play_id** | **int** |  | [optional] 
**play_state** | [**PlayStateEnum**](PlayStateEnum.md) |  | [optional] 
**play_stats** | [**List[PlayStat]**](PlayStat.md) | Individual player statistics for this play | [optional] 
**play_type** | [**PlayTypeEnum**](PlayTypeEnum.md) |  | [optional] 
**play_type_code** | **int** | Numeric code for play type | [optional] 
**possession_team_id** | **str** | Team ID with possession | [optional] 
**post_play_home_team_win_probability** | **float** | Home team win probability after play | [optional] 
**post_play_visitor_team_win_probability** | **float** | Visitor team win probability after play | [optional] 
**pre_snap_home_score** | **int** |  | [optional] 
**pre_snap_home_team_win_probability** | **float** | Home team win probability before play | [optional] 
**pre_snap_visitor_score** | **int** |  | [optional] 
**pre_snap_visitor_team_win_probability** | **float** | Visitor team win probability before play | [optional] 
**quarter** | **int** | Current quarter | [optional] 
**sequence** | **int** | Play sequence number | [optional] 
**start_game_clock** | **str** | Game clock at play start | [optional] 
**time_of_day_utc** | **datetime** | UTC timestamp of play | [optional] 
**visitor_score** | **int** |  | [optional] 
**visitor_timeouts_left** | **int** | Visitor team timeouts remaining | [optional] 
**yardline** | **str** | Field position | [optional] 
**yardline_number** | **int** | Yard line number | [optional] 
**yardline_side** | **str** | Side of field | [optional] 
**yards_to_go** | **int** | Yards needed for first down | [optional] 

## Example

```python
from src.griddy.nfl.models.play_detail import PlayDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PlayDetail from a JSON string
play_detail_instance = PlayDetail.from_json(json)
# print the JSON string representation of the object
print(PlayDetail.to_json())

# convert the object into a dict
play_detail_dict = play_detail_instance.to_dict()
# create an instance of PlayDetail from a dict
play_detail_from_dict = PlayDetail.from_dict(play_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


