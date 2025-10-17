# Game

NFL game information including teams, scheduling, and venue details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team** | [**Team**](Team.md) |  | [optional] 
**broadcast_info** | [**BroadcastInfo**](BroadcastInfo.md) |  | [optional] 
**category** | [**PrimetimeGameCategoryEnum**](PrimetimeGameCategoryEnum.md) |  | [optional] 
**var_date** | **date** | Game date (YYYY-MM-DD) | [optional] 
**date_am_pm** | [**MeridiemEnum**](MeridiemEnum.md) |  | [optional] 
**date_day** | **str** | Day of week (full) | [optional] 
**date_day_month** | **str** | Date in M/D format | [optional] 
**date_day_short** | **str** | Day of week (abbreviated) | [optional] 
**date_time** | **str** | Time without AM/PM | [optional] 
**date_time_am_pm** | **str** | Time with AM/PM | [optional] 
**extensions** | **List[object]** | Additional game data extensions | [optional] 
**external_ids** | [**List[ExternalId]**](ExternalId.md) |  | [optional] 
**game_type** | **str** | Type of game | [optional] 
**home_team** | [**Team**](Team.md) |  | [optional] 
**id** | **str** | Unique game identifier | [optional] 
**international** | **bool** | Whether game is played internationally | [optional] 
**neutral_site** | **bool** | Whether game is at neutral venue | [optional] 
**phase** | [**GamePhaseEnum**](GamePhaseEnum.md) |  | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**status** | [**GameStatusEnum**](GameStatusEnum.md) |  | [optional] 
**ticket_url** | **str** | Primary ticket purchase URL | [optional] 
**ticket_vendors** | [**List[TicketVendor]**](TicketVendor.md) |  | [optional] 
**time** | **datetime** | Game time in UTC | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**version** | **int** | Data version number | [optional] 
**week** | **int** | Week number | [optional] 
**week_type** | [**WeekTypeEnum**](WeekTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game import Game

# TODO update the JSON string below
json = "{}"
# create an instance of Game from a JSON string
game_instance = Game.from_json(json)
# print the JSON string representation of the object
print(Game.to_json())

# convert the object into a dict
game_dict = game_instance.to_dict()
# create an instance of Game from a dict
game_from_dict = Game.from_dict(game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


