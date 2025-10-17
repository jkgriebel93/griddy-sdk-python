# NFLWeeklyOddsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[NFLNFLGameOdds]**](NFLGameOdds.md) |  | [optional] 
**season** | **str** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**week** | **str** | Week number | [optional] 

## Example

```python
from nfl.models.nfl_weekly_odds_response import NFLWeeklyOddsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyOddsResponse from a JSON string
nfl_weekly_odds_response_instance = NFLWeeklyOddsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyOddsResponse.to_json())

# convert the object into a dict
nfl_weekly_odds_response_dict = nfl_weekly_odds_response_instance.to_dict()
# create an instance of NFLWeeklyOddsResponse from a dict
nfl_weekly_odds_response_from_dict = NFLWeeklyOddsResponse.from_dict(nfl_weekly_odds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


