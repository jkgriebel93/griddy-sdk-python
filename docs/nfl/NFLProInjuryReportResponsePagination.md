# NFLProInjuryReportResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_pro_injury_report_response_pagination import NFLProInjuryReportResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProInjuryReportResponsePagination from a JSON string
nfl_pro_injury_report_response_pagination_instance = NFLProInjuryReportResponsePagination.from_json(json)
# print the JSON string representation of the object
print(NFLProInjuryReportResponsePagination.to_json())

# convert the object into a dict
nfl_pro_injury_report_response_pagination_dict = nfl_pro_injury_report_response_pagination_instance.to_dict()
# create an instance of NFLProInjuryReportResponsePagination from a dict
nfl_pro_injury_report_response_pagination_from_dict = NFLProInjuryReportResponsePagination.from_dict(nfl_pro_injury_report_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


