# StandingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**week** | **int** | Current week for standings | [optional] 
**weeks** | [**List[StandingsResponseWeeksInner]**](StandingsResponseWeeksInner.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.standings_response import StandingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsResponse from a JSON string
standings_response_instance = StandingsResponse.from_json(json)
# print the JSON string representation of the object
print(StandingsResponse.to_json())

# convert the object into a dict
standings_response_dict = standings_response_instance.to_dict()
# create an instance of StandingsResponse from a dict
standings_response_from_dict = StandingsResponse.from_dict(standings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


