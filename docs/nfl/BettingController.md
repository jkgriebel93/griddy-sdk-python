# nfl.BettingController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_weekly_betting_odds**](BettingController.md#get_weekly_betting_odds) | **GET** /api/schedules/week/odds | Get Weekly Betting Odds


# **get_weekly_betting_odds**
> NFLNFLWeeklyOddsResponse get_weekly_betting_odds(season, season_type, week)

Get Weekly Betting Odds

Retrieves comprehensive betting odds for all games in a specified week.
Returns point spreads, money lines, and totals (over/under) for each game
with the latest odds updates from betting markets.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_weekly_odds_response import NFLNFLWeeklyOddsResponse
from nfl.models.nfl_season_type_enum import NFLSeasonTypeEnum
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
    api_instance = nfl.BettingController(api_client)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    week = 4 # int | Week number within the season

    try:
        # Get Weekly Betting Odds
        api_response = api_instance.get_weekly_betting_odds(season, season_type, week)
        print("The response of BettingController->get_weekly_betting_odds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BettingController->get_weekly_betting_odds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number within the season | 

### Return type

[**NFLNFLWeeklyOddsResponse**](NFLWeeklyOddsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved betting odds |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

