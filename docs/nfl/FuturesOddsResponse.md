# FuturesOddsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FuturesOddsResponseData**](FuturesOddsResponseData.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.futures_odds_response import FuturesOddsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesOddsResponse from a JSON string
futures_odds_response_instance = FuturesOddsResponse.from_json(json)
# print the JSON string representation of the object
print(FuturesOddsResponse.to_json())

# convert the object into a dict
futures_odds_response_dict = futures_odds_response_instance.to_dict()
# create an instance of FuturesOddsResponse from a dict
futures_odds_response_from_dict = FuturesOddsResponse.from_dict(futures_odds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


