# OffensiveSplitCategory

Definition of offensive situation categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Split category name | [optional] 
**description** | **str** | Category description | [optional] 
**situation_type** | [**OffensiveSituationTypeEnum**](OffensiveSituationTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.offensive_split_category import OffensiveSplitCategory

# TODO update the JSON string below
json = "{}"
# create an instance of OffensiveSplitCategory from a JSON string
offensive_split_category_instance = OffensiveSplitCategory.from_json(json)
# print the JSON string representation of the object
print(OffensiveSplitCategory.to_json())

# convert the object into a dict
offensive_split_category_dict = offensive_split_category_instance.to_dict()
# create an instance of OffensiveSplitCategory from a dict
offensive_split_category_from_dict = OffensiveSplitCategory.from_dict(offensive_split_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


