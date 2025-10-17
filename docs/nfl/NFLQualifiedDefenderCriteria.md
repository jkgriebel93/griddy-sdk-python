# NFLQualifiedDefenderCriteria

Criteria for qualified defender designation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Explanation of qualification criteria | [optional] 
**minimum_coverage_snaps** | **int** | Minimum coverage snaps required | [optional] 
**minimum_snaps** | **int** | Minimum defensive snaps required | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_qualified_defender_criteria import NFLQualifiedDefenderCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of NFLQualifiedDefenderCriteria from a JSON string
nfl_qualified_defender_criteria_instance = NFLQualifiedDefenderCriteria.from_json(json)
# print the JSON string representation of the object
print(NFLQualifiedDefenderCriteria.to_json())

# convert the object into a dict
nfl_qualified_defender_criteria_dict = nfl_qualified_defender_criteria_instance.to_dict()
# create an instance of NFLQualifiedDefenderCriteria from a dict
nfl_qualified_defender_criteria_from_dict = NFLQualifiedDefenderCriteria.from_dict(nfl_qualified_defender_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


