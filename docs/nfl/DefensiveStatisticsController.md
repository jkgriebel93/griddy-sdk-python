# nfl.DefensiveStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_defensive_stats_by_season**](DefensiveStatisticsController.md#get_defensive_stats_by_season) | **GET** /api/secured/stats/defense/nearest/season | Get Defensive Player Statistics by Season


# **get_defensive_stats_by_season**
> NFLNFLDefensiveStatsResponse get_defensive_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_defender=qualified_defender, team_defense=team_defense)

Get Defensive Player Statistics by Season

Retrieves comprehensive defensive statistics for NFL players during a specified season. Returns detailed coverage metrics including targets allowed, completion rates, pass rating allowed, yards after catch prevention, and advanced Next Gen Stats data. Supports filtering by qualified defenders, teams, and various sorting options. Data includes traditional defensive stats and advanced analytics like EPA (Expected Points Added), CROE (Completion Rate Over Expected), receiver separation allowed, and coverage snap counts.

### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_defensive_stats_response import NFLNFLDefensiveStatsResponse
from nfl.models.nfl_season_type_enum import NFLSeasonTypeEnum
from nfl.models.nfl_sort_order_enum import NFLSortOrderEnum
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
    api_instance = nfl.DefensiveStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = cov # str | Field to sort by (optional) (default to cov)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)
    qualified_defender = False # bool | Filter to only qualified defenders (minimum snap threshold) (optional) (default to False)
    team_defense = ['[\"3800\",\"1800\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Defensive Player Statistics by Season
        api_response = api_instance.get_defensive_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_defender=qualified_defender, team_defense=team_defense)
        print("The response of DefensiveStatisticsController->get_defensive_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefensiveStatisticsController->get_defensive_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to cov]
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_defender** | **bool**| Filter to only qualified defenders (minimum snap threshold) | [optional] [default to False]
 **team_defense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**NFLNFLDefensiveStatsResponse**](NFLDefensiveStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved defensive statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

