# NFLDefensiveSplitCategory

Definition of defensive situation categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Split category name | [optional] 
**description** | **str** | Category description | [optional] 
**situation_type** | [**NFLNFLDefensiveSituationTypeEnum**](NFLDefensiveSituationTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_defensive_split_category import NFLDefensiveSplitCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDefensiveSplitCategory from a JSON string
nfl_defensive_split_category_instance = NFLDefensiveSplitCategory.from_json(json)
# print the JSON string representation of the object
print(NFLDefensiveSplitCategory.to_json())

# convert the object into a dict
nfl_defensive_split_category_dict = nfl_defensive_split_category_instance.to_dict()
# create an instance of NFLDefensiveSplitCategory from a dict
nfl_defensive_split_category_from_dict = NFLDefensiveSplitCategory.from_dict(nfl_defensive_split_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


