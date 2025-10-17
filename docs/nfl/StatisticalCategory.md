# StatisticalCategory

Definition of statistical categories for sorting and filtering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category name | [optional] 
**data_type** | [**DataTypeEnum**](DataTypeEnum.md) |  | [optional] 
**description** | **str** | Category description | [optional] 
**unit** | **str** | Unit of measurement (if applicable) | [optional] 

## Example

```python
from src.griddy.nfl.models.statistical_category import StatisticalCategory

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticalCategory from a JSON string
statistical_category_instance = StatisticalCategory.from_json(json)
# print the JSON string representation of the object
print(StatisticalCategory.to_json())

# convert the object into a dict
statistical_category_dict = statistical_category_instance.to_dict()
# create an instance of StatisticalCategory from a dict
statistical_category_from_dict = StatisticalCategory.from_dict(statistical_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


