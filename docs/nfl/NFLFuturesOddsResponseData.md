# NFLFuturesOddsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**List[NFLNFLFuturesMarket]**](NFLFuturesMarket.md) |  | [optional] 
**division** | [**List[NFLNFLFuturesMarket]**](NFLFuturesMarket.md) |  | [optional] 
**super_bowl** | [**List[NFLNFLFuturesMarket]**](NFLFuturesMarket.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_futures_odds_response_data import NFLFuturesOddsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFuturesOddsResponseData from a JSON string
nfl_futures_odds_response_data_instance = NFLFuturesOddsResponseData.from_json(json)
# print the JSON string representation of the object
print(NFLFuturesOddsResponseData.to_json())

# convert the object into a dict
nfl_futures_odds_response_data_dict = nfl_futures_odds_response_data_instance.to_dict()
# create an instance of NFLFuturesOddsResponseData from a dict
nfl_futures_odds_response_data_from_dict = NFLFuturesOddsResponseData.from_dict(nfl_futures_odds_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


