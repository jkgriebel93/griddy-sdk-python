# src.griddy.nfl.DefensivePassRushStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_defensive_pass_rush_stats_by_season**](DefensivePassRushStatisticsController.md#get_defensive_pass_rush_stats_by_season) | **GET** /api/secured/stats/defense/passRush/season | Get Defensive Pass Rush Statistics by Season


# **get_defensive_pass_rush_stats_by_season**
> PassRushStatsResponse get_defensive_pass_rush_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_defender=qualified_defender)

Get Defensive Pass Rush Statistics by Season

Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
teams, and various sorting options. Data includes traditional pass rush stats and advanced
analytics like pass rush grade, pressure rate, and time to sack metrics.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.pass_rush_stats_response import PassRushStatsResponse
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.sort_order_enum import SortOrderEnum
from src.griddy.nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = src.griddy.nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = src.griddy.nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with src.griddy.nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = src.griddy.nfl.DefensivePassRushStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = pr # str | Field to sort by (optional) (default to pr)
    sort_value = src.griddy.nfl.SortOrderEnum() # SortOrderEnum | Sort direction (optional)
    qualified_defender = False # bool | Filter to only qualified defenders (minimum snap threshold) (optional) (default to False)

    try:
        # Get Defensive Pass Rush Statistics by Season
        api_response = api_instance.get_defensive_pass_rush_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_defender=qualified_defender)
        print("The response of DefensivePassRushStatisticsController->get_defensive_pass_rush_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefensivePassRushStatisticsController->get_defensive_pass_rush_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to pr]
 **sort_value** | [**SortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_defender** | **bool**| Filter to only qualified defenders (minimum snap threshold) | [optional] [default to False]

### Return type

[**PassRushStatsResponse**](PassRushStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved pass rush statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

