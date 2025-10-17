# InjuryReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[TeamInjuryReport]**](TeamInjuryReport.md) |  | [optional] 
**season** | **int** |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.injury_report_response import InjuryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InjuryReportResponse from a JSON string
injury_report_response_instance = InjuryReportResponse.from_json(json)
# print the JSON string representation of the object
print(InjuryReportResponse.to_json())

# convert the object into a dict
injury_report_response_dict = injury_report_response_instance.to_dict()
# create an instance of InjuryReportResponse from a dict
injury_report_response_from_dict = InjuryReportResponse.from_dict(injury_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


