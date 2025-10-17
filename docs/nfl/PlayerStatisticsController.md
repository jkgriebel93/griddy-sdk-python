# nfl.PlayerStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_passing_stats_by_season**](PlayerStatisticsController.md#get_player_passing_stats_by_season) | **GET** /api/secured/stats/players-offense/passing/season | Get Player Passing Statistics by Season


# **get_player_passing_stats_by_season**
> NFLNFLPassingStatsResponse get_player_passing_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_passer=qualified_passer, team_offense=team_offense)

Get Player Passing Statistics by Season

Retrieves comprehensive passing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers only, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and situational statistics.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_passing_stats_response import NFLNFLPassingStatsResponse
from nfl.models.nfl_passing_stats_category_enum import NFLPassingStatsCategoryEnum
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
    api_instance = nfl.PlayerStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = nfl.NFLPassingStatsCategoryEnum() # NFLPassingStatsCategoryEnum | Field to sort by (optional)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)
    qualified_passer = True # bool | Filter to only qualified passers (minimum attempts threshold) (optional) (default to True)
    team_offense = ['[\"3000\",\"3900\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Passing Statistics by Season
        api_response = api_instance.get_player_passing_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_passer=qualified_passer, team_offense=team_offense)
        print("The response of PlayerStatisticsController->get_player_passing_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerStatisticsController->get_player_passing_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | [**NFLPassingStatsCategoryEnum**](.md)| Field to sort by | [optional] 
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_passer** | **bool**| Filter to only qualified passers (minimum attempts threshold) | [optional] [default to True]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**NFLNFLPassingStatsResponse**](NFLPassingStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved passing statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

