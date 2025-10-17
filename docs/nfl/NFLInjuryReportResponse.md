# NFLInjuryReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[NFLNFLTeamInjuryReport]**](NFLTeamInjuryReport.md) |  | [optional] 
**season** | **int** |  | [optional] 
**week** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_injury_report_response import NFLInjuryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLInjuryReportResponse from a JSON string
nfl_injury_report_response_instance = NFLInjuryReportResponse.from_json(json)
# print the JSON string representation of the object
print(NFLInjuryReportResponse.to_json())

# convert the object into a dict
nfl_injury_report_response_dict = nfl_injury_report_response_instance.to_dict()
# create an instance of NFLInjuryReportResponse from a dict
nfl_injury_report_response_from_dict = NFLInjuryReportResponse.from_dict(nfl_injury_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


