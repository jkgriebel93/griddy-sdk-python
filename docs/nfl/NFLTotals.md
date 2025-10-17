# NFLTotals

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
from nfl.models.nfl_totals import NFLTotals

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTotals from a JSON string
nfl_totals_instance = NFLTotals.from_json(json)
# print the JSON string representation of the object
print(NFLTotals.to_json())

# convert the object into a dict
nfl_totals_dict = nfl_totals_instance.to_dict()
# create an instance of NFLTotals from a dict
nfl_totals_from_dict = NFLTotals.from_dict(nfl_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


