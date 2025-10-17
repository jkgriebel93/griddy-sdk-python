# NFLStatisticalCategory

Definition of statistical categories for sorting and filtering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category name | [optional] 
**data_type** | [**NFLNFLDataTypeEnum**](NFLDataTypeEnum.md) |  | [optional] 
**description** | **str** | Category description | [optional] 
**unit** | **str** | Unit of measurement (if applicable) | [optional] 

## Example

```python
from nfl.models.nfl_statistical_category import NFLStatisticalCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStatisticalCategory from a JSON string
nfl_statistical_category_instance = NFLStatisticalCategory.from_json(json)
# print the JSON string representation of the object
print(NFLStatisticalCategory.to_json())

# convert the object into a dict
nfl_statistical_category_dict = nfl_statistical_category_instance.to_dict()
# create an instance of NFLStatisticalCategory from a dict
nfl_statistical_category_from_dict = NFLStatisticalCategory.from_dict(nfl_statistical_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


