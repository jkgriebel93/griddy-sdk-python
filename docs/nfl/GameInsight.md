# GameInsight

Game-specific analytical insight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **int** |  | [optional] 
**nfl_id** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_abbr** | **str** |  | [optional] 
**title** | **str** | A short-ish description of the insight | [optional] 
**sub_note1** | **str** | A longer elaboration of the insight | [optional] 
**var_date** | **date** |  | [optional] 
**evergreen** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **str** | Appears to be the username of the NFL staff that created the insight | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**game_id** | **int** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**tags** | **List[str]** |  | [optional] 
**id** | **str** | Appears to be a UUID with dashes removed | [optional] 

## Example

```python
from src.griddy.nfl.models.game_insight import GameInsight

# TODO update the JSON string below
json = "{}"
# create an instance of GameInsight from a JSON string
game_insight_instance = GameInsight.from_json(json)
# print the JSON string representation of the object
print(GameInsight.to_json())

# convert the object into a dict
game_insight_dict = game_insight_instance.to_dict()
# create an instance of GameInsight from a dict
game_insight_from_dict = GameInsight.from_dict(game_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


