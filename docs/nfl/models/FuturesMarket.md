# FuturesMarket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixture** | **object** | Associated fixture information | [optional] 
**fixture_id** | **str** | Associated fixture ID if applicable | [optional] 
**hierarchy** | **str** | Full betting hierarchy path | [optional] 
**is_available** | **bool** | Whether market is currently available | [optional] 
**is_suspended** | **bool** | Whether market is currently suspended | [optional] 
**name** | **str** | Market name (e.g., \&quot;Winner\&quot;, \&quot;Division Winner\&quot;) | [optional] 
**selections** | [**List[OddsSelection]**](OddsSelection.md) |  | [optional] 
**source_id** | **str** | Source identifier for the market | [optional] 

## Example

```python
from src.griddy.nfl.models.futures_market import FuturesMarket

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesMarket from a JSON string
futures_market_instance = FuturesMarket.from_json(json)
# print the JSON string representation of the object
print(FuturesMarket.to_json())

# convert the object into a dict
futures_market_dict = futures_market_instance.to_dict()
# create an instance of FuturesMarket from a dict
futures_market_from_dict = FuturesMarket.from_dict(futures_market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


