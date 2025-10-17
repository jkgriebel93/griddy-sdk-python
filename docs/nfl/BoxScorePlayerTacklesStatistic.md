# BoxScorePlayerTacklesStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_id** | **int** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**count** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**sacks** | **float** |  | [optional] 
**sack_yards** | **int** |  | [optional] 
**qb_hits** | **int** |  | [optional] 
**safeties** | **int** |  | [optional] 
**tackles_for_loss** | **int** |  | [optional] 
**tackles_for_loss_yards** | **int** |  | [optional] 
**special_teams_tackles** | **int** |  | [optional] 
**special_teams_assists** | **int** |  | [optional] 
**special_teams_blocks** | **int** |  | [optional] 
**miscellaneous_tackles** | **int** |  | [optional] 
**miscellaneous_assists** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_tackles_statistic import BoxScorePlayerTacklesStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerTacklesStatistic from a JSON string
box_score_player_tackles_statistic_instance = BoxScorePlayerTacklesStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerTacklesStatistic.to_json())

# convert the object into a dict
box_score_player_tackles_statistic_dict = box_score_player_tackles_statistic_instance.to_dict()
# create an instance of BoxScorePlayerTacklesStatistic from a dict
box_score_player_tackles_statistic_from_dict = BoxScorePlayerTacklesStatistic.from_dict(box_score_player_tackles_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


