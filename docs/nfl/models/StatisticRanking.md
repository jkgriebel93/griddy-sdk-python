# StatisticRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Team&#39;s rank in this category (1-32) | [optional] 
**statistic** | [**StatisticRankingStatistic**](StatisticRankingStatistic.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.statistic_ranking import StatisticRanking

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticRanking from a JSON string
statistic_ranking_instance = StatisticRanking.from_json(json)
# print the JSON string representation of the object
print(StatisticRanking.to_json())

# convert the object into a dict
statistic_ranking_dict = statistic_ranking_instance.to_dict()
# create an instance of StatisticRanking from a dict
statistic_ranking_from_dict = StatisticRanking.from_dict(statistic_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


