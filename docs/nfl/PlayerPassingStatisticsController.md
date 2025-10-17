# src.griddy.nfl.PlayerPassingStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_passing_stats_by_week**](PlayerPassingStatisticsController.md#get_player_passing_stats_by_week) | **GET** /api/secured/stats/players-offense/passing/week | Get Player Passing Statistics by Week


# **get_player_passing_stats_by_week**
> WeeklyPassingStatsResponse get_player_passing_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_passer=qualified_passer, team_offense=team_offense)

Get Player Passing Statistics by Week

Retrieves comprehensive passing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and game-specific context.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.passing_stats_category_enum import PassingStatsCategoryEnum
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.sort_order_enum import SortOrderEnum
from src.griddy.nfl.models.week_slug_enum import WeekSlugEnum
from src.griddy.nfl.models.weekly_passing_stats_response import WeeklyPassingStatsResponse
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
    api_instance = src.griddy.nfl.PlayerPassingStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = src.griddy.nfl.WeekSlugEnum() # WeekSlugEnum | Week identifier
    limit = 50 # int | Maximum number of players to return (optional) (default to 50)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = src.griddy.nfl.PassingStatsCategoryEnum() # PassingStatsCategoryEnum | Field to sort by (optional)
    sort_value = src.griddy.nfl.SortOrderEnum() # SortOrderEnum | Sort direction (optional)
    qualified_passer = False # bool | Filter to only qualified passers (minimum attempts threshold) (optional) (default to False)
    team_offense = ['[\"3900\",\"3200\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Passing Statistics by Week
        api_response = api_instance.get_player_passing_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_passer=qualified_passer, team_offense=team_offense)
        print("The response of PlayerPassingStatisticsController->get_player_passing_stats_by_week:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerPassingStatisticsController->get_player_passing_stats_by_week: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | [**WeekSlugEnum**](.md)| Week identifier | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 50]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | [**PassingStatsCategoryEnum**](.md)| Field to sort by | [optional] 
 **sort_value** | [**SortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_passer** | **bool**| Filter to only qualified passers (minimum attempts threshold) | [optional] [default to False]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**WeeklyPassingStatsResponse**](WeeklyPassingStatsResponse.md)

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

