# NFLFuturesOddsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NFLNFLFuturesOddsResponseData**](NFLFuturesOddsResponseData.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_futures_odds_response import NFLFuturesOddsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFuturesOddsResponse from a JSON string
nfl_futures_odds_response_instance = NFLFuturesOddsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLFuturesOddsResponse.to_json())

# convert the object into a dict
nfl_futures_odds_response_dict = nfl_futures_odds_response_instance.to_dict()
# create an instance of NFLFuturesOddsResponse from a dict
nfl_futures_odds_response_from_dict = NFLFuturesOddsResponse.from_dict(nfl_futures_odds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


