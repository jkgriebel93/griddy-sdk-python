# PointSpread

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
from src.griddy.nfl.models.point_spread import PointSpread

# TODO update the JSON string below
json = "{}"
# create an instance of PointSpread from a JSON string
point_spread_instance = PointSpread.from_json(json)
# print the JSON string representation of the object
print(PointSpread.to_json())

# convert the object into a dict
point_spread_dict = point_spread_instance.to_dict()
# create an instance of PointSpread from a dict
point_spread_from_dict = PointSpread.from_dict(point_spread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


