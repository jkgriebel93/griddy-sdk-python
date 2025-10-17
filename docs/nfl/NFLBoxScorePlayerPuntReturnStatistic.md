# NFLBoxScorePlayerPuntReturnStatistic


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
**count** | **int** |  | [optional] 
**yards** | **int** |  | [optional] 
**avg_yards** | **float** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**longest_return** | **int** |  | [optional] 
**fair_catches** | **int** |  | [optional] 
**longest_td_return** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_box_score_player_punt_return_statistic import NFLBoxScorePlayerPuntReturnStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxScorePlayerPuntReturnStatistic from a JSON string
nfl_box_score_player_punt_return_statistic_instance = NFLBoxScorePlayerPuntReturnStatistic.from_json(json)
# print the JSON string representation of the object
print(NFLBoxScorePlayerPuntReturnStatistic.to_json())

# convert the object into a dict
nfl_box_score_player_punt_return_statistic_dict = nfl_box_score_player_punt_return_statistic_instance.to_dict()
# create an instance of NFLBoxScorePlayerPuntReturnStatistic from a dict
nfl_box_score_player_punt_return_statistic_from_dict = NFLBoxScorePlayerPuntReturnStatistic.from_dict(nfl_box_score_player_punt_return_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


