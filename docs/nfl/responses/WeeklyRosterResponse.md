# WeeklyRosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**team** | [**TeamInfo**](TeamInfo.md) |  | [optional] 
**team_players** | [**List[WeeklyPlayer]**](WeeklyPlayer.md) |  | [optional] 
**week** | **int** | Week number | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_roster_response import WeeklyRosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyRosterResponse from a JSON string
weekly_roster_response_instance = WeeklyRosterResponse.from_json(json)
# print the JSON string representation of the object
print(WeeklyRosterResponse.to_json())

# convert the object into a dict
weekly_roster_response_dict = weekly_roster_response_instance.to_dict()
# create an instance of WeeklyRosterResponse from a dict
weekly_roster_response_from_dict = WeeklyRosterResponse.from_dict(weekly_roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


