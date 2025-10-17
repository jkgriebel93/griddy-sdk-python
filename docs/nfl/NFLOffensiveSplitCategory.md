# NFLOffensiveSplitCategory

Definition of offensive situation categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Split category name | [optional] 
**description** | **str** | Category description | [optional] 
**situation_type** | [**NFLNFLOffensiveSituationTypeEnum**](NFLOffensiveSituationTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_offensive_split_category import NFLOffensiveSplitCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NFLOffensiveSplitCategory from a JSON string
nfl_offensive_split_category_instance = NFLOffensiveSplitCategory.from_json(json)
# print the JSON string representation of the object
print(NFLOffensiveSplitCategory.to_json())

# convert the object into a dict
nfl_offensive_split_category_dict = nfl_offensive_split_category_instance.to_dict()
# create an instance of NFLOffensiveSplitCategory from a dict
nfl_offensive_split_category_from_dict = NFLOffensiveSplitCategory.from_dict(nfl_offensive_split_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


