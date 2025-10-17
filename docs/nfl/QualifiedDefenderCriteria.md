# QualifiedDefenderCriteria

Criteria for qualified defender designation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Explanation of qualification criteria | [optional] 
**minimum_coverage_snaps** | **int** | Minimum coverage snaps required | [optional] 
**minimum_snaps** | **int** | Minimum defensive snaps required | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.qualified_defender_criteria import QualifiedDefenderCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of QualifiedDefenderCriteria from a JSON string
qualified_defender_criteria_instance = QualifiedDefenderCriteria.from_json(json)
# print the JSON string representation of the object
print(QualifiedDefenderCriteria.to_json())

# convert the object into a dict
qualified_defender_criteria_dict = qualified_defender_criteria_instance.to_dict()
# create an instance of QualifiedDefenderCriteria from a dict
qualified_defender_criteria_from_dict = QualifiedDefenderCriteria.from_dict(qualified_defender_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


