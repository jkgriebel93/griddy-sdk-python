# NFLMultipleRankingsCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLMultipleRankingsCategoryPagination**](NFLMultipleRankingsCategoryPagination.md) |  | [optional] 
**stat_category** | **str** | Category of statistic | [optional] 
**stat_name** | **str** | Name of specific statistic | [optional] 
**teams** | [**List[NFLNFLTeamRankingEntry]**](NFLTeamRankingEntry.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_multiple_rankings_category import NFLMultipleRankingsCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NFLMultipleRankingsCategory from a JSON string
nfl_multiple_rankings_category_instance = NFLMultipleRankingsCategory.from_json(json)
# print the JSON string representation of the object
print(NFLMultipleRankingsCategory.to_json())

# convert the object into a dict
nfl_multiple_rankings_category_dict = nfl_multiple_rankings_category_instance.to_dict()
# create an instance of NFLMultipleRankingsCategory from a dict
nfl_multiple_rankings_category_from_dict = NFLMultipleRankingsCategory.from_dict(nfl_multiple_rankings_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


