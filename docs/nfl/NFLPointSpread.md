# NFLPointSpread

Point spread betting odds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_handicap** | **str** | Away team point spread | [optional] 
**away_price** | **str** | Away team spread odds (American format) | [optional] 
**home_handicap** | **str** | Home team point spread | [optional] 
**home_price** | **str** | Home team spread odds (American format) | [optional] 

## Example

```python
from nfl.models.nfl_point_spread import NFLPointSpread

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPointSpread from a JSON string
nfl_point_spread_instance = NFLPointSpread.from_json(json)
# print the JSON string representation of the object
print(NFLPointSpread.to_json())

# convert the object into a dict
nfl_point_spread_dict = nfl_point_spread_instance.to_dict()
# create an instance of NFLPointSpread from a dict
nfl_point_spread_from_dict = NFLPointSpread.from_dict(nfl_point_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


