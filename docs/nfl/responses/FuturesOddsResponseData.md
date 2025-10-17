# FuturesOddsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**List[FuturesMarket]**](FuturesMarket.md) |  | [optional] 
**division** | [**List[FuturesMarket]**](FuturesMarket.md) |  | [optional] 
**super_bowl** | [**List[FuturesMarket]**](FuturesMarket.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.futures_odds_response_data import FuturesOddsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesOddsResponseData from a JSON string
futures_odds_response_data_instance = FuturesOddsResponseData.from_json(json)
# print the JSON string representation of the object
print(FuturesOddsResponseData.to_json())

# convert the object into a dict
futures_odds_response_data_dict = futures_odds_response_data_instance.to_dict()
# create an instance of FuturesOddsResponseData from a dict
futures_odds_response_data_from_dict = FuturesOddsResponseData.from_dict(futures_odds_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


