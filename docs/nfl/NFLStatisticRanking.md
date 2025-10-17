# NFLStatisticRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Team&#39;s rank in this category (1-32) | [optional] 
**statistic** | [**NFLNFLStatisticRankingStatistic**](NFLStatisticRankingStatistic.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_statistic_ranking import NFLStatisticRanking

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStatisticRanking from a JSON string
nfl_statistic_ranking_instance = NFLStatisticRanking.from_json(json)
# print the JSON string representation of the object
print(NFLStatisticRanking.to_json())

# convert the object into a dict
nfl_statistic_ranking_dict = nfl_statistic_ranking_instance.to_dict()
# create an instance of NFLStatisticRanking from a dict
nfl_statistic_ranking_from_dict = NFLStatisticRanking.from_dict(nfl_statistic_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


