# BoxScorePlayerPuntReturnStatistic


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
**yards** | **int** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**longest_return** | **int** |  | [optional] 
**fair_catches** | **int** |  | [optional] 
**longest_td_return** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.box_score_player_punt_return_statistic import BoxScorePlayerPuntReturnStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of BoxScorePlayerPuntReturnStatistic from a JSON string
box_score_player_punt_return_statistic_instance = BoxScorePlayerPuntReturnStatistic.from_json(json)
# print the JSON string representation of the object
print(BoxScorePlayerPuntReturnStatistic.to_json())

# convert the object into a dict
box_score_player_punt_return_statistic_dict = box_score_player_punt_return_statistic_instance.to_dict()
# create an instance of BoxScorePlayerPuntReturnStatistic from a dict
box_score_player_punt_return_statistic_from_dict = BoxScorePlayerPuntReturnStatistic.from_dict(box_score_player_punt_return_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


