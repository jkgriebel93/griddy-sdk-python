# GameDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_date** | **str** |  | [optional] 
**game_id** | **int** |  | [optional] 
**game_key** | **int** |  | [optional] 
**game_time** | **datetime** |  | [optional] 
**game_time_eastern** | **str** |  | [optional] 
**game_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**home_display_name** | **str** |  | [optional] 
**home_nickname** | **str** |  | [optional] 
**home_team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**home_team_abbr** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**iso_time** | **int** | Unix timestamp in milliseconds | [optional] 
**network_channel** | **str** |  | [optional] 
**ngs_game** | **bool** |  | [optional] 
**released_to_clubs** | **bool** |  | [optional] 
**score** | [**GameScore**](GameScore.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**site** | [**Site**](Site.md) |  | [optional] 
**smart_id** | **str** |  | [optional] 
**validated** | **bool** |  | [optional] 
**visitor_display_name** | **str** |  | [optional] 
**visitor_nickname** | **str** |  | [optional] 
**visitor_team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**visitor_team_abbr** | **str** |  | [optional] 
**visitor_team_id** | **str** |  | [optional] 
**week** | **int** |  | [optional] 
**week_name_abbr** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_detail import GameDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GameDetail from a JSON string
game_detail_instance = GameDetail.from_json(json)
# print the JSON string representation of the object
print(GameDetail.to_json())

# convert the object into a dict
game_detail_dict = game_detail_instance.to_dict()
# create an instance of GameDetail from a dict
game_detail_from_dict = GameDetail.from_dict(game_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


