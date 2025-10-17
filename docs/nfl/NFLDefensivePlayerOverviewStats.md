# NFLDefensivePlayerOverviewStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Player&#39;s full name | 
**game_snap** | **int** | Defensive snaps played in games | [optional] 
**gp** | **int** | Games played | 
**gs** | **int** | Games started | 
**h_stop** | **int** | Hard stops (tackles for loss or no gain) | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**int** | **int** | Interceptions | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | 
**ngs_position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**NFLNFLDefensivePositionGroupEnum**](NFLDefensivePositionGroupEnum.md) |  | [optional] 
**pass_rating_nd** | **float** | Passer rating allowed when targeted (no data excluded) | [optional] 
**position** | [**NFLNFLDefensivePositionEnum**](NFLDefensivePositionEnum.md) |  | 
**position_group** | [**NFLNFLDefensivePositionGroupEnum**](NFLDefensivePositionGroupEnum.md) |  | [optional] 
**pr** | **int** | Pass rush snaps | [optional] 
**qbp** | **int** | Quarterback pressures | [optional] 
**qbp_r** | **float** | Quarterback pressure rate (0-1) | [optional] 
**qd** | **bool** | Qualified defender status | [optional] 
**rd** | **int** | Run defense snaps | [optional] 
**rec_nd** | **int** | Receptions allowed (no data excluded) | [optional] 
**rec_td_nd** | **int** | Receiving touchdowns allowed (no data excluded) | [optional] 
**rec_yds_nd** | **int** | Receiving yards allowed (no data excluded) | [optional] 
**sack** | **int** | Sacks | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**snap** | **int** | Total defensive snaps played | 
**snap_pct** | **float** | Percentage of team snaps played (0-1) | [optional] 
**t_stop** | **int** | Tackle stops (successful tackles) | [optional] 
**tck** | **int** | Total tackles | [optional] 
**team_id** | **str** | Team identifier | 
**team_snap** | **int** | Total team defensive snaps | [optional] 
**tg** | **int** | Team games for player | [optional] 
**tgt_nd** | **int** | Times targeted in coverage (no data excluded) | [optional] 
**total_tg** | **int** | Total team games in period | [optional] 

## Example

```python
from nfl.models.nfl_defensive_player_overview_stats import NFLDefensivePlayerOverviewStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensivePlayerOverviewStats from a JSON string
nfl_defensive_player_overview_stats_instance = NFLDefensivePlayerOverviewStats.from_json(json)
# print the JSON string representation of the object
print(NFLDefensivePlayerOverviewStats.to_json())

# convert the object into a dict
nfl_defensive_player_overview_stats_dict = nfl_defensive_player_overview_stats_instance.to_dict()
# create an instance of NFLDefensivePlayerOverviewStats from a dict
nfl_defensive_player_overview_stats_from_dict = NFLDefensivePlayerOverviewStats.from_dict(nfl_defensive_player_overview_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


