# NFLBoxScorePlayerPuntingStatistic


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
**position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**attempts** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**gross_avg_punt_length** | **int** |  | [optional] 
**blocked_cnt** | **int** |  | [optional] 
**longest_punt** | **int** |  | [optional] 
**touchback_cnts** | **int** |  | [optional] 
**inside20_cnt** | **int** |  | [optional] 
**net_punting_avg** | **int** |  | [optional] 
**return_yards** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_player_punting_statistic import NFLBoxScorePlayerPuntingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScorePlayerPuntingStatistic from a JSON string
nfl_box_score_player_punting_statistic_instance = NFLBoxScorePlayerPuntingStatistic.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScorePlayerPuntingStatistic.to_json())

# convert the object into a dict
nfl_box_score_player_punting_statistic_dict = nfl_box_score_player_punting_statistic_instance.to_dict()
# create an instance of NFLBoxScorePlayerPuntingStatistic from a dict
nfl_box_score_player_punting_statistic_from_dict = NFLBoxScorePlayerPuntingStatistic.from_dict(nfl_box_score_player_punting_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


