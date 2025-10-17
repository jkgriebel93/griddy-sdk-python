# NFLCurrentGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team** | [**NFLNFLGameTeam**](NFLGameTeam.md) |  | [optional] 
**broadcast_info** | [**NFLNFLBroadcastInfo**](NFLBroadcastInfo.md) |  | [optional] 
**category** | [**NFLNFLPrimetimeGameCategoryEnum**](NFLPrimetimeGameCategoryEnum.md) |  | [optional] 
**var_date** | **date** | Game date (YYYY-MM-DD) | [optional] 
**date_am_pm** | [**NFLNFLMeridiemEnum**](NFLMeridiemEnum.md) |  | [optional] 
**date_day** | **str** | Day of week (full) | [optional] 
**date_day_month** | **str** | Date in M/D format | [optional] 
**date_day_short** | **str** | Day of week (abbreviated) | [optional] 
**date_time** | **str** | Time without AM/PM | [optional] 
**date_time_am_pm** | **str** | Time with AM/PM | [optional] 
**extensions** | **List[object]** |  | [optional] 
**external_ids** | [**List[NFLNFLExternalId]**](NFLExternalId.md) |  | [optional] 
**game_type** | **str** | Type of game | [optional] 
**home_team** | [**NFLNFLGameTeam**](NFLGameTeam.md) |  | [optional] 
**id** | **str** | Unique game identifier | [optional] 
**international** | **bool** | Whether game is played internationally | [optional] 
**neutral_site** | **bool** | Whether game is at neutral venue | [optional] 
**phase** | **str** | Game phase (e.g., PREGAME, FINAL) | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**status** | [**NFLNFLGameStatusEnum**](NFLGameStatusEnum.md) |  | [optional] 
**ticket_url** | **str** |  | [optional] 
**ticket_vendors** | [**List[NFLNFLTicketVendor]**](NFLTicketVendor.md) |  | [optional] 
**time** | **datetime** | Game time in UTC | [optional] 
**venue** | [**NFLNFLVenue**](NFLVenue.md) |  | [optional] 
**version** | **int** |  | [optional] 
**week** | **int** |  | [optional] 
**week_type** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_current_game import NFLCurrentGame

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCurrentGame from a JSON string
nfl_current_game_instance = NFLCurrentGame.from_json(json)
# print the JSON string representation of the object
print(NFLCurrentGame.to_json())

# convert the object into a dict
nfl_current_game_dict = nfl_current_game_instance.to_dict()
# create an instance of NFLCurrentGame from a dict
nfl_current_game_from_dict = NFLCurrentGame.from_dict(nfl_current_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


