# StatisticRankingStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Statistical category name | [optional] 
**value** | **float** | Statistical value | [optional] 

## Example

```python
from src.griddy.nfl.models.statistic_ranking_statistic import StatisticRankingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticRankingStatistic from a JSON string
statistic_ranking_statistic_instance = StatisticRankingStatistic.from_json(json)
# print the JSON string representation of the object
print(StatisticRankingStatistic.to_json())

# convert the object into a dict
statistic_ranking_statistic_dict = statistic_ranking_statistic_instance.to_dict()
# create an instance of StatisticRankingStatistic from a dict
statistic_ranking_statistic_from_dict = StatisticRankingStatistic.from_dict(statistic_ranking_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


