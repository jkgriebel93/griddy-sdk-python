# BettingOddsFormatAmericanOdds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**examples** | [**List[BettingOddsFormatAmericanOddsExamplesInner]**](BettingOddsFormatAmericanOddsExamplesInner.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.betting_odds_format_american_odds import BettingOddsFormatAmericanOdds

# TODO update the JSON string below
json = "{}"
# create an instance of BettingOddsFormatAmericanOdds from a JSON string
betting_odds_format_american_odds_instance = BettingOddsFormatAmericanOdds.from_json(json)
# print the JSON string representation of the object
print(BettingOddsFormatAmericanOdds.to_json())

# convert the object into a dict
betting_odds_format_american_odds_dict = betting_odds_format_american_odds_instance.to_dict()
# create an instance of BettingOddsFormatAmericanOdds from a dict
betting_odds_format_american_odds_from_dict = BettingOddsFormatAmericanOdds.from_dict(betting_odds_format_american_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


