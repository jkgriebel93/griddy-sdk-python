# PlayerSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** | Player&#39;s birth date | [optional] 
**college_conference** | **str** | Player&#39;s college conference | [optional] 
**college_name** | **str** | Player&#39;s college | [optional] 
**current_team_id** | **str** | Current team identifier | [optional] 
**display_name** | **str** | Player&#39;s display name | [optional] 
**draft_club** | **str** | Team that drafted the player | [optional] 
**draft_number** | **int** | Overall draft pick number | [optional] 
**draftround** | **int** | Draft round | [optional] 
**entry_year** | **int** | Year player entered the league | [optional] 
**esb_id** | **str** | ESB identifier | [optional] 
**first_name** | **str** | Player&#39;s first name | [optional] 
**football_name** | **str** | Player&#39;s football name (nickname) | [optional] 
**gsis_id** | **str** | GSIS identifier | [optional] 
**gsis_it_id** | **int** | GSIS IT identifier | [optional] 
**headshot** | **str** | URL to player headshot image | [optional] 
**height** | **str** | Player height (format is feet-inches) | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**last_name** | **str** | Player&#39;s last name | [optional] 
**nfl_id** | **int** | NFL player identifier | [optional] 
**ngs_position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**ngs_position_group** | [**NextGenStatsPositionGroupEnum**](NextGenStatsPositionGroupEnum.md) |  | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**position_group** | [**NextGenStatsPositionGroupEnum**](NextGenStatsPositionGroupEnum.md) |  | [optional] 
**rookie_year** | **int** | Player&#39;s rookie year | [optional] 
**season** | **int** | Current season | [optional] 
**short_name** | **str** | Shortened player name | [optional] 
**smart_id** | **str** | Smart identifier for the player | [optional] 
**status** | **str** | Player status code | [optional] 
**status_description_abbr** | **str** | Abbreviated status description | [optional] 
**status_short_description** | **str** | Short status description | [optional] 
**team_abbr** | **str** | Current team abbreviation | [optional] 
**uniform_number** | **str** | Player&#39;s uniform number (formatted) | [optional] 
**weight** | **int** | Player weight in pounds | [optional] 
**years_of_experience** | **int** | Years of NFL experience | [optional] 
**awards** | [**List[Award]**](Award.md) |  | [optional] 
**biography** | **str** | Player biography | [optional] 
**career_stats** | [**CareerStats**](CareerStats.md) |  | [optional] 
**contract_info** | [**ContractInfo**](ContractInfo.md) |  | [optional] 
**current_season_stats** | [**SeasonStats**](SeasonStats.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_search_result import PlayerSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSearchResult from a JSON string
player_search_result_instance = PlayerSearchResult.from_json(json)
# print the JSON string representation of the object
print(PlayerSearchResult.to_json())

# convert the object into a dict
player_search_result_dict = player_search_result_instance.to_dict()
# create an instance of PlayerSearchResult from a dict
player_search_result_from_dict = PlayerSearchResult.from_dict(player_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


