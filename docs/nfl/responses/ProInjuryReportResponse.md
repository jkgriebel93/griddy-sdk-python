# ProInjuryReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**injuries** | **List[Dict[str, object]]** | Array of injured players (empty if no injuries) | [optional] 
**pagination** | [**ProInjuryReportResponsePagination**](ProInjuryReportResponsePagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.pro_injury_report_response import ProInjuryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProInjuryReportResponse from a JSON string
pro_injury_report_response_instance = ProInjuryReportResponse.from_json(json)
# print the JSON string representation of the object
print(ProInjuryReportResponse.to_json())

# convert the object into a dict
pro_injury_report_response_dict = pro_injury_report_response_instance.to_dict()
# create an instance of ProInjuryReportResponse from a dict
pro_injury_report_response_from_dict = ProInjuryReportResponse.from_dict(pro_injury_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


