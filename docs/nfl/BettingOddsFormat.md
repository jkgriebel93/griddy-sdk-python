# BettingOddsFormat

Information about betting odds formats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**american_odds** | [**BettingOddsFormatAmericanOdds**](BettingOddsFormatAmericanOdds.md) |  | [optional] 
**decimal_odds** | [**BettingOddsFormatDecimalOdds**](BettingOddsFormatDecimalOdds.md) |  | [optional] 
**fractional_odds** | [**BettingOddsFormatFractionalOdds**](BettingOddsFormatFractionalOdds.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.betting_odds_format import BettingOddsFormat

# TODO update the JSON string below
json = "{}"
# create an instance of BettingOddsFormat from a JSON string
betting_odds_format_instance = BettingOddsFormat.from_json(json)
# print the JSON string representation of the object
print(BettingOddsFormat.to_json())

# convert the object into a dict
betting_odds_format_dict = betting_odds_format_instance.to_dict()
# create an instance of BettingOddsFormat from a dict
betting_odds_format_from_dict = BettingOddsFormat.from_dict(betting_odds_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


