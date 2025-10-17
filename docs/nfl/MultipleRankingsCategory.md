# MultipleRankingsCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**MultipleRankingsCategoryPagination**](MultipleRankingsCategoryPagination.md) |  | [optional] 
**stat_category** | **str** | Category of statistic | [optional] 
**stat_name** | **str** | Name of specific statistic | [optional] 
**teams** | [**List[TeamRankingEntry]**](TeamRankingEntry.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.multiple_rankings_category import MultipleRankingsCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleRankingsCategory from a JSON string
multiple_rankings_category_instance = MultipleRankingsCategory.from_json(json)
# print the JSON string representation of the object
print(MultipleRankingsCategory.to_json())

# convert the object into a dict
multiple_rankings_category_dict = multiple_rankings_category_instance.to_dict()
# create an instance of MultipleRankingsCategory from a dict
multiple_rankings_category_from_dict = MultipleRankingsCategory.from_dict(multiple_rankings_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


