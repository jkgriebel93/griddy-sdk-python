# NFLMoneyLine

Money line betting odds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_price** | **str** | Away team money line odds (American format) | [optional] 
**home_price** | **str** | Home team money line odds (American format) | [optional] 

## Example

```python
from nfl.models.nfl_money_line import NFLMoneyLine

# TODO update the JSON string below
json = "{}"
# create an instance of NFLMoneyLine from a JSON string
nfl_money_line_instance = NFLMoneyLine.from_json(json)
# print the JSON string representation of the object
print(NFLMoneyLine.to_json())

# convert the object into a dict
nfl_money_line_dict = nfl_money_line_instance.to_dict()
# create an instance of NFLMoneyLine from a dict
nfl_money_line_from_dict = NFLMoneyLine.from_dict(nfl_money_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


