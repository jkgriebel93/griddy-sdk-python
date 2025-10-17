# nfl.TeamDefensePassStatisticsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_defense_pass_stats_by_season**](TeamDefensePassStatisticsController.md#get_team_defense_pass_stats_by_season) | **GET** /api/secured/stats/team-defense/pass/season | Get Team Defense Pass Statistics by Season


# **get_team_defense_pass_stats_by_season**
> NFLNFLTeamDefensePassStatsResponse get_team_defense_pass_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value)

Get Team Defense Pass Statistics by Season

Retrieves comprehensive pass defense statistics for NFL teams during a specified season.
Returns detailed metrics including traditional defensive stats, advanced analytics like EPA
and YACOE (Yards After Catch Over Expected), Next Gen Stats data, and situational performance
breakdowns. Supports various sorting options and includes pressure rates, coverage metrics,
quarterback disruption stats, and receiver separation allowed.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_team_defense_pass_stats_response import NFLNFLTeamDefensePassStatsResponse
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
    api_instance = nfl.TeamDefensePassStatisticsController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    limit = 35 # int | Maximum number of teams to return (optional) (default to 35)
    offset = 0 # int | Number of records to skip for pagination (optional) (default to 0)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    sort_key = passYpg # str | Field to sort by (optional) (default to passYpg)
    sort_value = nfl.NFLSortOrderEnum() # NFLSortOrderEnum | Sort direction (optional)

    try:
        # Get Team Defense Pass Statistics by Season
        api_response = api_instance.get_team_defense_pass_stats_by_season(season, season_type, limit=limit, offset=offset, page=page, sort_key=sort_key, sort_value=sort_value)
        print("The response of TeamDefensePassStatisticsController->get_team_defense_pass_stats_by_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamDefensePassStatisticsController->get_team_defense_pass_stats_by_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **limit** | **int**| Maximum number of teams to return | [optional] [default to 35]
 **offset** | **int**| Number of records to skip for pagination | [optional] [default to 0]
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **sort_key** | **str**| Field to sort by | [optional] [default to passYpg]
 **sort_value** | [**NFLSortOrderEnum**](.md)| Sort direction | [optional] 

### Return type

[**NFLNFLTeamDefensePassStatsResponse**](NFLTeamDefensePassStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved team defense pass statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

