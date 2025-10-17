# WeeklyOddsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[GameOdds]**](GameOdds.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_odds_response import WeeklyOddsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyOddsResponse from a JSON string
weekly_odds_response_instance = WeeklyOddsResponse.from_json(json)
# print the JSON string representation of the object
print(WeeklyOddsResponse.to_json())

# convert the object into a dict
weekly_odds_response_dict = weekly_odds_response_instance.to_dict()
# create an instance of WeeklyOddsResponse from a dict
weekly_odds_response_from_dict = WeeklyOddsResponse.from_dict(weekly_odds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


