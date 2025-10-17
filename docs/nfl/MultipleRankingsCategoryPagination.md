# MultipleRankingsCategoryPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.multiple_rankings_category_pagination import MultipleRankingsCategoryPagination

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleRankingsCategoryPagination from a JSON string
multiple_rankings_category_pagination_instance = MultipleRankingsCategoryPagination.from_json(json)
# print the JSON string representation of the object
print(MultipleRankingsCategoryPagination.to_json())

# convert the object into a dict
multiple_rankings_category_pagination_dict = multiple_rankings_category_pagination_instance.to_dict()
# create an instance of MultipleRankingsCategoryPagination from a dict
multiple_rankings_category_pagination_from_dict = MultipleRankingsCategoryPagination.from_dict(multiple_rankings_category_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


