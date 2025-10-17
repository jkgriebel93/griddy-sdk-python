# SeasonWeeksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**weeks** | [**List[Week]**](Week.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.season_weeks_response import SeasonWeeksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonWeeksResponse from a JSON string
season_weeks_response_instance = SeasonWeeksResponse.from_json(json)
# print the JSON string representation of the object
print(SeasonWeeksResponse.to_json())

# convert the object into a dict
season_weeks_response_dict = season_weeks_response_instance.to_dict()
# create an instance of SeasonWeeksResponse from a dict
season_weeks_response_from_dict = SeasonWeeksResponse.from_dict(season_weeks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


