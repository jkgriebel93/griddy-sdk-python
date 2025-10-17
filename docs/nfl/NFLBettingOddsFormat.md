# NFLBettingOddsFormat

Information about betting odds formats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**american_odds** | [**NFLNFLBettingOddsFormatAmericanOdds**](NFLBettingOddsFormatAmericanOdds.md) |  | [optional] 
**decimal_odds** | [**NFLNFLBettingOddsFormatDecimalOdds**](NFLBettingOddsFormatDecimalOdds.md) |  | [optional] 
**fractional_odds** | [**NFLNFLBettingOddsFormatFractionalOdds**](NFLBettingOddsFormatFractionalOdds.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_betting_odds_format import NFLBettingOddsFormat

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBettingOddsFormat from a JSON string
nfl_betting_odds_format_instance = NFLBettingOddsFormat.from_json(json)
# print the JSON string representation of the object
print(NFLBettingOddsFormat.to_json())

# convert the object into a dict
nfl_betting_odds_format_dict = nfl_betting_odds_format_instance.to_dict()
# create an instance of NFLBettingOddsFormat from a dict
nfl_betting_odds_format_from_dict = NFLBettingOddsFormat.from_dict(nfl_betting_odds_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


