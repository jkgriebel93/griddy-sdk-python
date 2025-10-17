# Week

NFL week information including schedule dates and bye teams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bye_teams** | [**List[Team]**](Team.md) | Teams on bye this week (empty array if no bye teams) | [optional] 
**date_begin** | **date** | First day of the week | [optional] 
**date_end** | **date** | Last day of the week | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**season_type_week** | **str** | Combined season type and week identifier | [optional] 
**text** | **str** | Human-readable week description | [optional] 
**week** | **int** | Week number (0 for Hall of Fame game) | [optional] 
**week_slug** | [**WeekSlugEnum**](WeekSlugEnum.md) |  | [optional] 
**week_type** | [**WeekTypeEnum**](WeekTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.week import Week

# TODO update the JSON string below
json = "{}"
# create an instance of Week from a JSON string
week_instance = Week.from_json(json)
# print the JSON string representation of the object
print(Week.to_json())

# convert the object into a dict
week_dict = week_instance.to_dict()
# create an instance of Week from a dict
week_from_dict = Week.from_dict(week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


