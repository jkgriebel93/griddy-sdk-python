# MoneyLine

Money line betting odds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_price** | **str** | Away team money line odds (American format) | [optional] 
**home_price** | **str** | Home team money line odds (American format) | [optional] 

## Example

```python
from src.griddy.nfl.models.money_line import MoneyLine

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyLine from a JSON string
money_line_instance = MoneyLine.from_json(json)
# print the JSON string representation of the object
print(MoneyLine.to_json())

# convert the object into a dict
money_line_dict = money_line_instance.to_dict()
# create an instance of MoneyLine from a dict
money_line_from_dict = MoneyLine.from_dict(money_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


