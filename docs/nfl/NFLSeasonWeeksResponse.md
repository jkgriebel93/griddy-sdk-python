# NFLSeasonWeeksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**weeks** | [**List[NFLNFLWeek]**](NFLWeek.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_season_weeks_response import NFLSeasonWeeksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLSeasonWeeksResponse from a JSON string
nfl_season_weeks_response_instance = NFLSeasonWeeksResponse.from_json(json)
# print the JSON string representation of the object
print(NFLSeasonWeeksResponse.to_json())

# convert the object into a dict
nfl_season_weeks_response_dict = nfl_season_weeks_response_instance.to_dict()
# create an instance of NFLSeasonWeeksResponse from a dict
nfl_season_weeks_response_from_dict = NFLSeasonWeeksResponse.from_dict(nfl_season_weeks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


