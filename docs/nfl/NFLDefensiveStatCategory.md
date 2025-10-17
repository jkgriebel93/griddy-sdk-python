# NFLDefensiveStatCategory

Definition of defensive statistical categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category name | [optional] 
**data_type** | [**NFLNFLDataTypeEnum**](NFLDataTypeEnum.md) |  | [optional] 
**description** | **str** | Category description | [optional] 
**unit** | **str** | Unit of measurement (if applicable) | [optional] 

## Example

```python
from nfl.models.nfl_defensive_stat_category import NFLDefensiveStatCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveStatCategory from a JSON string
nfl_defensive_stat_category_instance = NFLDefensiveStatCategory.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveStatCategory.to_json())

# convert the object into a dict
nfl_defensive_stat_category_dict = nfl_defensive_stat_category_instance.to_dict()
# create an instance of NFLDefensiveStatCategory from a dict
nfl_defensive_stat_category_from_dict = NFLDefensiveStatCategory.from_dict(nfl_defensive_stat_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


