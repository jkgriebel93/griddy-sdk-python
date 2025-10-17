# src.griddy.nfl.SchedulesExtendedController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_week_games**](SchedulesExtendedController.md#get_current_week_games) | **GET** /api/schedules/current | Get Current Week Games
[**get_future_betting_odds**](SchedulesExtendedController.md#get_future_betting_odds) | **GET** /api/schedules/genius/future/odds | Get Future Betting Odds
[**get_team_standings**](SchedulesExtendedController.md#get_team_standings) | **GET** /api/schedules/standings | Get Team Standings


# **get_current_week_games**
> CurrentGamesResponse get_current_week_games()

Get Current Week Games

Retrieves all games for the current week of the NFL season.
Returns comprehensive game data including teams, venues, broadcast information,
scores (for completed games), and ticket details. The endpoint automatically
determines the current week based on the current date.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.current_games_response import CurrentGamesResponse
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
    api_instance = src.griddy.nfl.SchedulesExtendedController(api_client)

    try:
        # Get Current Week Games
        api_response = api_instance.get_current_week_games()
        print("The response of SchedulesExtendedController->get_current_week_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesExtendedController->get_current_week_games: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrentGamesResponse**](CurrentGamesResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved current week games |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_future_betting_odds**
> FuturesOddsResponse get_future_betting_odds()

Get Future Betting Odds

Retrieves comprehensive betting futures data including Super Bowl odds,
conference championship odds, and division winner odds for all teams.
Returns decimal odds for each selection along with availability status.
This endpoint provides futures market data across multiple betting hierarchies.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.futures_odds_response import FuturesOddsResponse
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
    api_instance = src.griddy.nfl.SchedulesExtendedController(api_client)

    try:
        # Get Future Betting Odds
        api_response = api_instance.get_future_betting_odds()
        print("The response of SchedulesExtendedController->get_future_betting_odds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesExtendedController->get_future_betting_odds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FuturesOddsResponse**](FuturesOddsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved betting futures |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_standings**
> StandingsResponse get_team_standings(season, season_type, week)

Get Team Standings

Retrieves comprehensive team standings for a specific season, season type, and week.
Returns detailed standings information including division, conference, home/away records,
win percentages, points for/against, current streaks, and clinching scenarios.
Standings are calculated through the specified week.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.standings_response import StandingsResponse
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
    api_instance = src.griddy.nfl.SchedulesExtendedController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 4 # int | Week number within the season

    try:
        # Get Team Standings
        api_response = api_instance.get_team_standings(season, season_type, week)
        print("The response of SchedulesExtendedController->get_team_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesExtendedController->get_team_standings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number within the season | 

### Return type

[**StandingsResponse**](StandingsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved standings |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

