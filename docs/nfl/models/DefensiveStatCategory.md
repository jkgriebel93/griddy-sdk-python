# DefensiveStatCategory

Definition of defensive statistical categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category name | [optional] 
**data_type** | [**DataTypeEnum**](DataTypeEnum.md) |  | [optional] 
**description** | **str** | Category description | [optional] 
**unit** | **str** | Unit of measurement (if applicable) | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_stat_category import DefensiveStatCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveStatCategory from a JSON string
defensive_stat_category_instance = DefensiveStatCategory.from_json(json)
# print the JSON string representation of the object
print(DefensiveStatCategory.to_json())

# convert the object into a dict
defensive_stat_category_dict = defensive_stat_category_instance.to_dict()
# create an instance of DefensiveStatCategory from a dict
defensive_stat_category_from_dict = DefensiveStatCategory.from_dict(defensive_stat_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


