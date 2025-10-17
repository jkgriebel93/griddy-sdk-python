# NFLFantasyPlayerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Player&#39;s full name | [optional] 
**fp_half_ppr** | **float** | Fantasy points (half-PPR scoring) | [optional] 
**fp_ppr** | **float** | Fantasy points (PPR scoring) | [optional] 
**fp_ppr_pg** | **float** | Fantasy points per game (PPR) | [optional] 
**fp_std** | **float** | Fantasy points (standard scoring) | [optional] 
**fp_std_pg** | **float** | Fantasy points per game (standard) | [optional] 
**gp** | **int** | Games played | [optional] 
**gs** | **int** | Games started | [optional] 
**headshot** | **str** | URL to player headshot image | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**pass_int** | **int** | Passing interceptions | [optional] 
**pass_td** | **int** | Passing touchdowns | [optional] 
**pass_yds** | **int** | Passing yards | [optional] 
**pass_yds_pg** | **float** | Passing yards per game | [optional] 
**position** | [**NFLNFLFantasyPlayerPositionEnum**](NFLFantasyPlayerPositionEnum.md) |  | [optional] 
**position_group** | [**NFLNFLFantasyPositionGroupEnum**](NFLFantasyPositionGroupEnum.md) |  | [optional] 
**rec** | **int** | Receptions | [optional] 
**rec_pg** | **float** | Receptions per game | [optional] 
**rec_td** | **int** | Receiving touchdowns | [optional] 
**rec_yds** | **int** | Receiving yards | [optional] 
**red_zone_targets** | **int** | Targets inside the red zone | [optional] 
**rush_td** | **int** | Rushing touchdowns | [optional] 
**rush_yds** | **int** | Rushing yards | [optional] 
**rush_yds_pg** | **float** | Rushing yards per game | [optional] 
**short_name** | **str** | Abbreviated player name | [optional] 
**snap_pct** | **float** | Percentage of offensive snaps played (0-1) | [optional] 
**target_share** | **float** | Percentage of team targets (0-1) | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**tgt** | **int** | Targets | [optional] 

## Example

```python
from nfl.models.nfl_fantasy_player_stats import NFLFantasyPlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFantasyPlayerStats from a JSON string
nfl_fantasy_player_stats_instance = NFLFantasyPlayerStats.from_json(json)
# print the JSON string representation of the object
print(NFLFantasyPlayerStats.to_json())

# convert the object into a dict
nfl_fantasy_player_stats_dict = nfl_fantasy_player_stats_instance.to_dict()
# create an instance of NFLFantasyPlayerStats from a dict
nfl_fantasy_player_stats_from_dict = NFLFantasyPlayerStats.from_dict(nfl_fantasy_player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


