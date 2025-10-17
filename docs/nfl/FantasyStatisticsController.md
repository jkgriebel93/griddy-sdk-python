# nfl.FantasyStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fantasy_stats_by_season**](FantasyStatisticsController.md#get_fantasy_stats_by_season) | **GET** /api/secured/stats/fantasy/season | Get Fantasy Football Statistics by Season


# **get_fantasy_stats_by_season**
> NFLNFLFantasyStatsResponse get_fantasy_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, position_group=position_group, team_offense=team_offense, team_defense=team_defense, min_offensive_snaps=min_offensive_snaps, last_n_weeks=last_n_weeks)

Get Fantasy Football Statistics by Season

Retrieves comprehensive fantasy football statistics for NFL players during a specified season.
Returns fantasy-relevant metrics including standard scoring, PPR scoring, snap counts, and
target share data. Supports filtering by position groups (QB, RB, WR, TE, SPEC), teams,
minimum offensive snap thresholds, and rolling N-week windows for recent performance analysis.
Data includes traditional fantasy categories and advanced metrics for lineup optimization.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_fantasy_stats_response import NFLNFLFantasyStatsResponse
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
    api_instance = nfl.FantasyStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of players to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = fpStd # str | Field to sort by (optional) (default to fpStd)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)
    position_group = ['[\"QB\"]'] # List[str] | Filter by position groups (supports multiple positions) (optional)
    team_offense = '3900' # str | Filter by specific offensive team ID (optional)
    team_defense = '4600' # str | Filter by specific defensive team ID (opponent analysis) (optional)
    min_offensive_snaps = 0 # int | Minimum offensive snaps threshold for inclusion (optional) (default to 0)
    last_n_weeks = 3 # int | Number of recent weeks to analyze (rolling window) (optional)

    try:
        # Get Fantasy Football Statistics by Season
        api_response = api_instance.get_fantasy_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, position_group=position_group, team_offense=team_offense, team_defense=team_defense, min_offensive_snaps=min_offensive_snaps, last_n_weeks=last_n_weeks)
        print("The response of FantasyStatisticsController->get_fantasy_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FantasyStatisticsController->get_fantasy_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of players to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to fpStd]
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 
 **position_group** | [**List[str]**](str.md)| Filter by position groups (supports multiple positions) | [optional] 
 **team_offense** | **str**| Filter by specific offensive team ID | [optional] 
 **team_defense** | **str**| Filter by specific defensive team ID (opponent analysis) | [optional] 
 **min_offensive_snaps** | **int**| Minimum offensive snaps threshold for inclusion | [optional] [default to 0]
 **last_n_weeks** | **int**| Number of recent weeks to analyze (rolling window) | [optional] 

### Return type

[**NFLNFLFantasyStatsResponse**](NFLFantasyStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved fantasy statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

