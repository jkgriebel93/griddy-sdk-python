# nfl.TeamsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_teams**](TeamsController.md#get_all_teams) | **GET** /api/teams/all | Get All Teams
[**get_team_roster**](TeamsController.md#get_team_roster) | **GET** /api/teams/roster | Get Team Roster
[**get_team_schedule**](TeamsController.md#get_team_schedule) | **GET** /api/teams/schedule | Get Team Schedule
[**get_weekly_team_roster**](TeamsController.md#get_weekly_team_roster) | **GET** /api/teams/rosterWeek | Get Weekly Team Roster


# **get_all_teams**
> List[NFLNFLProTeam] get_all_teams()

Get All Teams

Retrieves information for all NFL teams including regular teams and Pro Bowl teams.
Returns comprehensive team data including colors, logos, stadiums, and contact information.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_pro_team import NFLNFLProTeam
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
    api_instance = nfl.TeamsController(api_client)

    try:
        # Get All Teams
        api_response = api_instance.get_all_teams()
        print("The response of TeamsController->get_all_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsController->get_all_teams: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NFLNFLProTeam]**](NFLProTeam.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all teams |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_roster**
> NFLNFLTeamRosterResponse get_team_roster(team_id, season)

Get Team Roster

Retrieves the complete roster for a specific team and season.
Returns detailed player information including physical attributes, college info, and experience.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_team_roster_response import NFLNFLTeamRosterResponse
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
    api_instance = nfl.TeamsController(api_client)
    team_id = '3000' # str | Team identifier (4-digit string)
    season = 2025 # int | Season year

    try:
        # Get Team Roster
        api_response = api_instance.get_team_roster(team_id, season)
        print("The response of TeamsController->get_team_roster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsController->get_team_roster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team identifier (4-digit string) | 
 **season** | **int**| Season year | 

### Return type

[**NFLNFLTeamRosterResponse**](NFLTeamRosterResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved team roster |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Team not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_schedule**
> List[NFLNFLScheduledGame] get_team_schedule(team_id, season)

Get Team Schedule

Retrieves the complete schedule for a specific team and season.
Returns all games including preseason, regular season, and postseason with scores for completed games.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_scheduled_game import NFLNFLScheduledGame
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
    api_instance = nfl.TeamsController(api_client)
    team_id = '3000' # str | Team identifier (4-digit string)
    season = 2025 # int | Season year

    try:
        # Get Team Schedule
        api_response = api_instance.get_team_schedule(team_id, season)
        print("The response of TeamsController->get_team_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsController->get_team_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team identifier (4-digit string) | 
 **season** | **int**| Season year | 

### Return type

[**List[NFLNFLScheduledGame]**](NFLScheduledGame.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved team schedule |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Team not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weekly_team_roster**
> NFLNFLWeeklyRosterResponse get_weekly_team_roster(team_id, season, season_type, week)

Get Weekly Team Roster

Retrieves the roster for a specific team, season, season type, and week.
Returns player information with weekly status and availability.


### Example

* Bearer Authentication (NFLAuth):

```python
import nfl
from nfl.models.nflnfl_weekly_roster_response import NFLNFLWeeklyRosterResponse
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
    api_instance = nfl.TeamsController(api_client)
    team_id = '3900' # str | Team identifier (4-digit string)
    season = 2025 # int | Season year
    season_type = nfl.NFLSeasonTypeEnum() # NFLSeasonTypeEnum | Type of season
    week = 3 # int | Week number within the season

    try:
        # Get Weekly Team Roster
        api_response = api_instance.get_weekly_team_roster(team_id, season, season_type, week)
        print("The response of TeamsController->get_weekly_team_roster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsController->get_weekly_team_roster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team identifier (4-digit string) | 
 **season** | **int**| Season year | 
 **season_type** | [**NFLSeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number within the season | 

### Return type

[**NFLNFLWeeklyRosterResponse**](NFLWeeklyRosterResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved weekly roster |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Team or week not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

