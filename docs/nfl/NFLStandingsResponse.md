# NFLStandingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 
**season** | **int** |  | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**week** | **int** | Current week for standings | [optional] 
**weeks** | [**List[NFLNFLStandingsResponseWeeksInner]**](NFLStandingsResponseWeeksInner.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_standings_response import NFLStandingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandingsResponse from a JSON string
nfl_standings_response_instance = NFLStandingsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLStandingsResponse.to_json())

# convert the object into a dict
nfl_standings_response_dict = nfl_standings_response_instance.to_dict()
# create an instance of NFLStandingsResponse from a dict
nfl_standings_response_from_dict = NFLStandingsResponse.from_dict(nfl_standings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


