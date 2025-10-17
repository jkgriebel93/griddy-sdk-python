# NFLPlayWinProbability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down** | **int** | Down number (0 for kickoffs and special plays, 1-4 for regular plays) | [optional] 
**home_score** | **int** | Home team score after the play | [optional] 
**home_team_win_probability_added** | **float** | Win Probability Added (WPA) for home team on this play | [optional] 
**home_timeouts_left** | **int** | Number of timeouts remaining for home team | [optional] 
**play_description** | **str** | Detailed description of the play or game event | [optional] 
**play_id** | **int** | Unique play identifier | [optional] 
**possession_team_id** | **str** | Team ID with possession (4-digit string) | [optional] 
**post_play_home_team_win_probability** | **float** | Home team win probability after the play (0-1) | [optional] 
**post_play_visitor_team_win_probability** | **float** | Visiting team win probability after the play (0-1) | [optional] 
**pre_snap_home_score** | **int** | Home team score before the play | [optional] 
**pre_snap_home_team_win_probability** | **float** | Home team win probability before the play (0-1, null for game start) | [optional] 
**pre_snap_visitor_score** | **int** | Visitor team score before the play | [optional] 
**pre_snap_visitor_team_win_probability** | **float** | Visitor team win probability before the play (0-1, null for game start) | [optional] 
**quarter** | **int** | Quarter number (1-4, or 5 for overtime) | [optional] 
**sequence** | **float** | Play sequence number (can be decimal for special plays) | [optional] 
**visitor_score** | **int** | Visitor team score after the play | [optional] 
**visitor_team_win_probability_added** | **float** | Win Probability Added (WPA) for visitor team on this play (negative of home WPA) | [optional] 
**visitor_timeouts_left** | **int** | Number of timeouts remaining for visitor team | [optional] 
**yardline** | **str** | Field position description (e.g., \&quot;NE 27\&quot; or empty for special plays) | [optional] 
**yardline_number** | **int** | Yard line number (null for special plays) | [optional] 
**yardline_side** | **str** | Side of field (team abbreviation or null for midfield/special plays) | [optional] 
**yards_to_go** | **int** | Yards needed for first down | [optional] 

## Example

```python
from nfl.models.nfl_play_win_probability import NFLPlayWinProbability

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayWinProbability from a JSON string
nfl_play_win_probability_instance = NFLPlayWinProbability.from_json(json)
# print the JSON string representation of the object
print(NFLPlayWinProbability.to_json())

# convert the object into a dict
nfl_play_win_probability_dict = nfl_play_win_probability_instance.to_dict()
# create an instance of NFLPlayWinProbability from a dict
nfl_play_win_probability_from_dict = NFLPlayWinProbability.from_dict(nfl_play_win_probability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


