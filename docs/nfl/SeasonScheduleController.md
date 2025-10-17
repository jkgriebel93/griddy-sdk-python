# nfl.SeasonScheduleController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule_season_weeks**](SeasonScheduleController.md#get_schedule_season_weeks) | **GET** /api/schedules/weeks | Get Season Weeks


# **get_schedule_season_weeks**
> NFLNFLSeasonWeeksResponse get_schedule_season_weeks(season)

Get Season Weeks

Retrieves all weeks for a specific season including preseason, regular season, and postseason weeks. Returns week dates, types, and teams on bye for each week. This endpoint provides a comprehensive season calendar with all scheduling information.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_season_weeks_response import NFLNFLSeasonWeeksResponse
from nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nfl.SeasonScheduleController(api_client)
    season = 2025 # int | Season year

    try:
        # Get Season Weeks
        api_response = api_instance.get_schedule_season_weeks(season)
        print("The response of SeasonScheduleController->get_schedule_season_weeks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonScheduleController->get_schedule_season_weeks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 

### Return type

[**NFLNFLSeasonWeeksResponse**](NFLSeasonWeeksResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved season weeks |  -  |
**400** | Invalid season parameter |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

