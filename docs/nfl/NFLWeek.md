# NFLWeek

NFL week information including schedule dates and bye teams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bye_teams** | [**List[NFLNFLTeam]**](NFLTeam.md) | Teams on bye this week (empty array if no bye teams) | [optional] 
**date_begin** | **date** | First day of the week | [optional] 
**date_end** | **date** | Last day of the week | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**season_type_week** | **str** | Combined season type and week identifier | [optional] 
**text** | **str** | Human-readable week description | [optional] 
**week** | **int** | Week number (0 for Hall of Fame game) | [optional] 
**week_slug** | [**NFLNFLWeekSlugEnum**](NFLWeekSlugEnum.md) |  | [optional] 
**week_type** | [**NFLNFLWeekTypeEnum**](NFLWeekTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_week import NFLWeek

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeek from a JSON string
nfl_week_instance = NFLWeek.from_json(json)
# print the JSON string representation of the object
print(NFLWeek.to_json())

# convert the object into a dict
nfl_week_dict = nfl_week_instance.to_dict()
# create an instance of NFLWeek from a dict
nfl_week_from_dict = NFLWeek.from_dict(nfl_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


