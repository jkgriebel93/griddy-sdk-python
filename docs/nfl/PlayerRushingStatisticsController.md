# src.griddy.nfl.PlayerRushingStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_rushing_stats_by_season**](PlayerRushingStatisticsController.md#get_player_rushing_stats_by_season) | **GET** /api/secured/stats/players-offense/rushing/season | Get Player Rushing Statistics by Season
[**get_player_rushing_stats_by_week**](PlayerRushingStatisticsController.md#get_player_rushing_stats_by_week) | **GET** /api/secured/stats/players-offense/rushing/week | Get Player Rushing Statistics by Week


# **get_player_rushing_stats_by_season**
> RushingStatsResponse get_player_rushing_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_rusher=qualified_rusher, team_offense=team_offense)

Get Player Rushing Statistics by Season

Retrieves comprehensive rushing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and situational breakdowns.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.rushing_stats_response import RushingStatsResponse
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
    api_instance = src.griddy.nfl.PlayerRushingStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = yds # str | Field to sort by (optional) (default to yds)
    sort_value = src.griddy.nfl.SortOrderEnum() # SortOrderEnum | Sort direction (optional)
    qualified_rusher = False # bool | Filter to only qualified rushers (minimum attempts threshold) (optional) (default to False)
    team_offense = ['[\"3000\",\"3900\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Rushing Statistics by Season
        api_response = api_instance.get_player_rushing_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_rusher=qualified_rusher, team_offense=team_offense)
        print("The response of PlayerRushingStatisticsController->get_player_rushing_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRushingStatisticsController->get_player_rushing_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to yds]
 **sort_value** | [**SortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_rusher** | **bool**| Filter to only qualified rushers (minimum attempts threshold) | [optional] [default to False]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**RushingStatsResponse**](RushingStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved rushing statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rushing_stats_by_week**
> WeeklyRushingStatsResponse get_player_rushing_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_rusher=qualified_rusher, team_offense=team_offense)

Get Player Rushing Statistics by Week

Retrieves comprehensive rushing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and game-specific context.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.sort_order_enum import SortOrderEnum
from src.griddy.nfl.models.week_slug_enum import WeekSlugEnum
from src.griddy.nfl.models.weekly_rushing_stats_response import WeeklyRushingStatsResponse
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
    api_instance = src.griddy.nfl.PlayerRushingStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = src.griddy.nfl.WeekSlugEnum() # WeekSlugEnum | Week identifier
    limit = 50 # int | Maximum number of players to return (optional) (default to 50)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = yds # str | Field to sort by (optional) (default to yds)
    sort_value = src.griddy.nfl.SortOrderEnum() # SortOrderEnum | Sort direction (optional)
    qualified_rusher = False # bool | Filter to only qualified rushers (minimum attempts threshold) (optional) (default to False)
    team_offense = ['[\"3900\",\"3200\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Rushing Statistics by Week
        api_response = api_instance.get_player_rushing_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_rusher=qualified_rusher, team_offense=team_offense)
        print("The response of PlayerRushingStatisticsController->get_player_rushing_stats_by_week:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRushingStatisticsController->get_player_rushing_stats_by_week: %s\n" % e)
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
 **sort_key** | **str**| Field to sort by | [optional] [default to yds]
 **sort_value** | [**SortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_rusher** | **bool**| Filter to only qualified rushers (minimum attempts threshold) | [optional] [default to False]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**WeeklyRushingStatsResponse**](WeeklyRushingStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved rushing statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

