# BettingOddsFormatFractionalOdds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.betting_odds_format_fractional_odds import BettingOddsFormatFractionalOdds

# TODO update the JSON string below
json = "{}"
# create an instance of BettingOddsFormatFractionalOdds from a JSON string
betting_odds_format_fractional_odds_instance = BettingOddsFormatFractionalOdds.from_json(json)
# print the JSON string representation of the object
print(BettingOddsFormatFractionalOdds.to_json())

# convert the object into a dict
betting_odds_format_fractional_odds_dict = betting_odds_format_fractional_odds_instance.to_dict()
# create an instance of BettingOddsFormatFractionalOdds from a dict
betting_odds_format_fractional_odds_from_dict = BettingOddsFormatFractionalOdds.from_dict(betting_odds_format_fractional_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


