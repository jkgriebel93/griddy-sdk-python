# NFLStatisticRankingStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Statistical category name | [optional] 
**value** | **float** | Statistical value | [optional] 

## Example

```python
from nfl.models.nfl_statistic_ranking_statistic import NFLStatisticRankingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStatisticRankingStatistic from a JSON string
nfl_statistic_ranking_statistic_instance = NFLStatisticRankingStatistic.from_json(json)
# print the JSON string representation of the object
print(NFLStatisticRankingStatistic.to_json())

# convert the object into a dict
nfl_statistic_ranking_statistic_dict = nfl_statistic_ranking_statistic_instance.to_dict()
# create an instance of NFLStatisticRankingStatistic from a dict
nfl_statistic_ranking_statistic_from_dict = NFLStatisticRankingStatistic.from_dict(nfl_statistic_ranking_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


