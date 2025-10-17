# NFLProInjuryReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**injuries** | **List[Dict[str, object]]** | Array of injured players (empty if no injuries) | [optional] 
**pagination** | [**NFLNFLProInjuryReportResponsePagination**](NFLProInjuryReportResponsePagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_pro_injury_report_response import NFLProInjuryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProInjuryReportResponse from a JSON string
nfl_pro_injury_report_response_instance = NFLProInjuryReportResponse.from_json(json)
# print the JSON string representation of the object
print(NFLProInjuryReportResponse.to_json())

# convert the object into a dict
nfl_pro_injury_report_response_dict = nfl_pro_injury_report_response_instance.to_dict()
# create an instance of NFLProInjuryReportResponse from a dict
nfl_pro_injury_report_response_from_dict = NFLProInjuryReportResponse.from_dict(nfl_pro_injury_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


