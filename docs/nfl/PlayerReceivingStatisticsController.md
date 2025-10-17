# nfl.PlayerReceivingStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_receiving_stats_by_season**](PlayerReceivingStatisticsController.md#get_player_receiving_stats_by_season) | **GET** /api/secured/stats/players-offense/receiving/season | Get Player Receiving Statistics by Season
[**get_player_receiving_stats_by_week**](PlayerReceivingStatisticsController.md#get_player_receiving_stats_by_week) | **GET** /api/secured/stats/players-offense/receiving/week | Get Player Receiving Statistics by Week


# **get_player_receiving_stats_by_season**
> NFLNFLReceivingStatsResponse get_player_receiving_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_receiver=qualified_receiver, team_offense=team_offense)

Get Player Receiving Statistics by Season

Retrieves comprehensive receiving statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified receivers, and various sorting options.
Data includes catch percentage, yards per reception, EPA (Expected Points Added), CROE
(Catch Rate Over Expected), target share, route depth, separation metrics, and YAC analytics.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_receiving_stats_response import NFLNFLReceivingStatsResponse
from nfl.models.nfl_receiving_stats_category_enum import NFLReceivingStatsCategoryEnum
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
    api_instance = nfl.PlayerReceivingStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = nfl.NFLReceivingStatsCategoryEnum() # NFLReceivingStatsCategoryEnum | Field to sort by (optional)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)
    qualified_receiver = False # bool | Filter to only qualified receivers (minimum target threshold) (optional) (default to False)
    team_offense = ['[\"3000\",\"3900\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Receiving Statistics by Season
        api_response = api_instance.get_player_receiving_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_receiver=qualified_receiver, team_offense=team_offense)
        print("The response of PlayerReceivingStatisticsController->get_player_receiving_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerReceivingStatisticsController->get_player_receiving_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | [**NFLReceivingStatsCategoryEnum**](.md)| Field to sort by | [optional] 
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_receiver** | **bool**| Filter to only qualified receivers (minimum target threshold) | [optional] [default to False]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**NFLNFLReceivingStatsResponse**](NFLReceivingStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved receiving statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_receiving_stats_by_week**
> NFLNFLReceivingStatsResponse get_player_receiving_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_receiver=qualified_receiver, team_offense=team_offense)

Get Player Receiving Statistics by Week

Retrieves comprehensive receiving statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified receivers, and various sorting options.
Data includes catch percentage, yards per reception, EPA (Expected Points Added), CROE
(Catch Rate Over Expected), target share, route depth, separation metrics, and YAC analytics.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_receiving_stats_response import NFLNFLReceivingStatsResponse
from nfl.models.nfl_receiving_stats_category_enum import NFLReceivingStatsCategoryEnum
from nfl.models.nfl_season_type_enum import NFLSeasonTypeEnum
from nfl.models.nfl_sort_order_enum import NFLSortOrderEnum
from nfl.models.nfl_week_slug_enum import NFLWeekSlugEnum
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
    api_instance = nfl.PlayerReceivingStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    week = nfl.NFLWeekSlugEnum() # NFLWeekSlugEnum | Week identifier
    limit = 50 # int | Maximum number of players to return (optional) (default to 50)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = nfl.NFLReceivingStatsCategoryEnum() # NFLReceivingStatsCategoryEnum | Field to sort by (optional)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)
    qualified_receiver = False # bool | Filter to only qualified receivers (minimum target threshold) (optional) (default to False)
    team_offense = ['[\"3900\",\"3200\"]'] # List[str] | Filter by specific team IDs (supports multiple teams) (optional)

    try:
        # Get Player Receiving Statistics by Week
        api_response = api_instance.get_player_receiving_stats_by_week(season, season_type, week, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, qualified_receiver=qualified_receiver, team_offense=team_offense)
        print("The response of PlayerReceivingStatisticsController->get_player_receiving_stats_by_week:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerReceivingStatisticsController->get_player_receiving_stats_by_week: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **week** | [**NFLWeekSlugEnum**](.md)| Week identifier | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 50]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | [**NFLReceivingStatsCategoryEnum**](.md)| Field to sort by | [optional] 
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 
 **qualified_receiver** | **bool**| Filter to only qualified receivers (minimum target threshold) | [optional] [default to False]
 **team_offense** | [**List[str]**](str.md)| Filter by specific team IDs (supports multiple teams) | [optional] 

### Return type

[**NFLNFLReceivingStatsResponse**](NFLReceivingStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved receiving statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

