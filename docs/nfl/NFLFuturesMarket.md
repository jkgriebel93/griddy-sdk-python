# NFLFuturesMarket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixture** | **object** | Associated fixture information | [optional] 
**fixture_id** | **str** | Associated fixture ID if applicable | [optional] 
**hierarchy** | **str** | Full betting hierarchy path | [optional] 
**is_available** | **bool** | Whether market is currently available | [optional] 
**is_suspended** | **bool** | Whether market is currently suspended | [optional] 
**name** | **str** | Market name (e.g., \&quot;Winner\&quot;, \&quot;Division Winner\&quot;) | [optional] 
**selections** | [**List[NFLNFLOddsSelection]**](NFLOddsSelection.md) |  | [optional] 
**source_id** | **str** | Source identifier for the market | [optional] 

## Example

```python
from nfl.models.nfl_futures_market import NFLFuturesMarket

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFuturesMarket from a JSON string
nfl_futures_market_instance = NFLFuturesMarket.from_json(json)
# print the JSON string representation of the object
print(NFLFuturesMarket.to_json())

# convert the object into a dict
nfl_futures_market_dict = nfl_futures_market_instance.to_dict()
# create an instance of NFLFuturesMarket from a dict
nfl_futures_market_from_dict = NFLFuturesMarket.from_dict(nfl_futures_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


