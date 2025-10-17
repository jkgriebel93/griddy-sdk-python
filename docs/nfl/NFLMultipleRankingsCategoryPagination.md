# NFLMultipleRankingsCategoryPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_multiple_rankings_category_pagination import NFLMultipleRankingsCategoryPagination

# TODO update the JSON string below
json = "{}"
# create an instance of NFLMultipleRankingsCategoryPagination from a JSON string
nfl_multiple_rankings_category_pagination_instance = NFLMultipleRankingsCategoryPagination.from_json(json)
# print the JSON string representation of the object
print(NFLMultipleRankingsCategoryPagination.to_json())

# convert the object into a dict
nfl_multiple_rankings_category_pagination_dict = nfl_multiple_rankings_category_pagination_instance.to_dict()
# create an instance of NFLMultipleRankingsCategoryPagination from a dict
nfl_multiple_rankings_category_pagination_from_dict = NFLMultipleRankingsCategoryPagination.from_dict(nfl_multiple_rankings_category_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


