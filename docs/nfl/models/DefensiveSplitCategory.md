# DefensiveSplitCategory

Definition of defensive situation categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Split category name | [optional] 
**description** | **str** | Category description | [optional] 
**situation_type** | [**DefensiveSituationTypeEnum**](DefensiveSituationTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_split_category import DefensiveSplitCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveSplitCategory from a JSON string
defensive_split_category_instance = DefensiveSplitCategory.from_json(json)
# print the JSON string representation of the object
print(DefensiveSplitCategory.to_json())

# convert the object into a dict
defensive_split_category_dict = defensive_split_category_instance.to_dict()
# create an instance of DefensiveSplitCategory from a dict
defensive_split_category_from_dict = DefensiveSplitCategory.from_dict(defensive_split_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


