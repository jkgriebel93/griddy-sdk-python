# NFLGame

NFL game information including teams, scheduling, and venue details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**broadcast_info** | [**NFLNFLBroadcastInfo**](NFLBroadcastInfo.md) |  | [optional] 
**category** | [**NFLNFLPrimetimeGameCategoryEnum**](NFLPrimetimeGameCategoryEnum.md) |  | [optional] 
**var_date** | **date** | Game date (YYYY-MM-DD) | [optional] 
**date_am_pm** | [**NFLNFLMeridiemEnum**](NFLMeridiemEnum.md) |  | [optional] 
**date_day** | **str** | Day of week (full) | [optional] 
**date_day_month** | **str** | Date in M/D format | [optional] 
**date_day_short** | **str** | Day of week (abbreviated) | [optional] 
**date_time** | **str** | Time without AM/PM | [optional] 
**date_time_am_pm** | **str** | Time with AM/PM | [optional] 
**extensions** | **List[object]** | Additional game data extensions | [optional] 
**external_ids** | [**List[NFLNFLExternalId]**](NFLExternalId.md) |  | [optional] 
**game_type** | **str** | Type of game | [optional] 
**home_team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**id** | **str** | Unique game identifier | [optional] 
**international** | **bool** | Whether game is played internationally | [optional] 
**neutral_site** | **bool** | Whether game is at neutral venue | [optional] 
**phase** | [**NFLNFLGamePhaseEnum**](NFLGamePhaseEnum.md) |  | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**status** | [**NFLNFLGameStatusEnum**](NFLGameStatusEnum.md) |  | [optional] 
**ticket_url** | **str** | Primary ticket purchase URL | [optional] 
**ticket_vendors** | [**List[NFLNFLTicketVendor]**](NFLTicketVendor.md) |  | [optional] 
**time** | **datetime** | Game time in UTC | [optional] 
**venue** | [**NFLNFLVenue**](NFLVenue.md) |  | [optional] 
**version** | **int** | Data version number | [optional] 
**week** | **int** | Week number | [optional] 
**week_type** | [**NFLNFLWeekTypeEnum**](NFLWeekTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_game import NFLGame

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGame from a JSON string
nfl_game_instance = NFLGame.from_json(json)
# print the JSON string representation of the object
print(NFLGame.to_json())

# convert the object into a dict
nfl_game_dict = nfl_game_instance.to_dict()
# create an instance of NFLGame from a dict
nfl_game_from_dict = NFLGame.from_dict(nfl_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


