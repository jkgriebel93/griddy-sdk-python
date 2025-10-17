# src.griddy.nfl.TeamOffenseOverviewStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_offense_overview_stats_by_season**](TeamOffenseOverviewStatisticsController.md#get_team_offense_overview_stats_by_season) | **GET** /api/secured/stats/team-offense/overview/season | Get Team Offense Overview Statistics by Season


# **get_team_offense_overview_stats_by_season**
> TeamOffenseOverviewStatsResponse get_team_offense_overview_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, team_defense=team_defense, split=split)

Get Team Offense Overview Statistics by Season

Retrieves comprehensive offensive overview statistics for NFL teams during a specified season. Returns detailed metrics including traditional offensive stats, advanced analytics like EPA and efficiency ratings, Next Gen Stats data, and situational performance breakdowns. Supports filtering by various offensive situations including formations (shotgun, under center, pistol), game situations (leading, trailing, tied), and field positions (red zone, goal-to-go). Includes total offense, passing offense, rushing offense, and scoring metrics.

### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.sort_order_enum import SortOrderEnum
from src.griddy.nfl.models.team_offense_overview_stats_response import TeamOffenseOverviewStatsResponse
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
    api_instance = src.griddy.nfl.TeamOffenseOverviewStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of teams to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = ypg # str | Field to sort by (optional) (default to ypg)
    sort_value = src.griddy.nfl.SortOrderEnum() # SortOrderEnum | Sort direction (optional)
    team_defense = '2250' # str | Filter by specific team identifier (optional)
    split = ['[\"TEAM_WHEN_LEADING\"]'] # List[str] | Offensive situation splits to filter by (supports multiple values) (optional)

    try:
        # Get Team Offense Overview Statistics by Season
        api_response = api_instance.get_team_offense_overview_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value, team_defense=team_defense, split=split)
        print("The response of TeamOffenseOverviewStatisticsController->get_team_offense_overview_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamOffenseOverviewStatisticsController->get_team_offense_overview_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of teams to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to ypg]
 **sort_value** | [**SortOrderEnum**](.md)| Sort direction | [optional] 
 **team_defense** | **str**| Filter by specific team identifier | [optional] 
 **split** | [**List[str]**](str.md)| Offensive situation splits to filter by (supports multiple values) | [optional] 

### Return type

[**TeamOffenseOverviewStatsResponse**](TeamOffenseOverviewStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved team offense overview statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

