# Totals

Over/Under (totals) betting odds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**over_handicap** | **float** | Total points line for over | [optional] 
**over_price** | **int** | Over odds (American format) | [optional] 
**under_handicap** | **float** | Total points line for under | [optional] 
**under_price** | **int** | Under odds (American format) | [optional] 

## Example

```python
from src.griddy.nfl.models.totals import Totals

# TODO update the JSON string below
json = "{}"
# create an instance of Totals from a JSON string
totals_instance = Totals.from_json(json)
# print the JSON string representation of the object
print(Totals.to_json())

# convert the object into a dict
totals_dict = totals_instance.to_dict()
# create an instance of Totals from a dict
totals_from_dict = Totals.from_dict(totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


