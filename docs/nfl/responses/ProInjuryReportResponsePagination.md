# ProInjuryReportResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.pro_injury_report_response_pagination import ProInjuryReportResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of ProInjuryReportResponsePagination from a JSON string
pro_injury_report_response_pagination_instance = ProInjuryReportResponsePagination.from_json(json)
# print the JSON string representation of the object
print(ProInjuryReportResponsePagination.to_json())

# convert the object into a dict
pro_injury_report_response_pagination_dict = pro_injury_report_response_pagination_instance.to_dict()
# create an instance of ProInjuryReportResponsePagination from a dict
pro_injury_report_response_pagination_from_dict = ProInjuryReportResponsePagination.from_dict(pro_injury_report_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


