# src.griddy.nfl.ExperienceController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_experience_games**](ExperienceController.md#get_experience_games) | **GET** /experience/v1/games | Get Games by Season and Week
[**get_experience_teams**](ExperienceController.md#get_experience_teams) | **GET** /experience/v1/teams | Get All Teams


# **get_experience_games**
> ExperienceGamesResponse get_experience_games(season, season_type, week)

Get Games by Season and Week

Retrieves game information for a specific season, season type, and week.
Returns comprehensive game data including teams, venues, broadcast information, and ticket details.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.experience_games_response import ExperienceGamesResponse
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
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
    api_instance = src.griddy.nfl.ExperienceController(api_client)
    season = 2025 # int | Season year (e.g., 2025)
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 4 # int | Week number within the season

    try:
        # Get Games by Season and Week
        api_response = api_instance.get_experience_games(season, season_type, week)
        print("The response of ExperienceController->get_experience_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceController->get_experience_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year (e.g., 2025) | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number within the season | 

### Return type

[**ExperienceGamesResponse**](ExperienceGamesResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved games |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experience_teams**
> ExperienceTeamsResponse get_experience_teams(season, allteams=allteams)

Get All Teams

Retrieves information for all NFL teams including Pro Bowl teams.
Returns comprehensive team data including logos, colors, venues, and social media links.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.experience_teams_response import ExperienceTeamsResponse
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
    api_instance = src.griddy.nfl.ExperienceController(api_client)
    season = 2025 # int | Season year
    allteams = true # bool | Include all teams including special teams (optional)

    try:
        # Get All Teams
        api_response = api_instance.get_experience_teams(season, allteams=allteams)
        print("The response of ExperienceController->get_experience_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperienceController->get_experience_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **allteams** | **bool**| Include all teams including special teams | [optional] 

### Return type

[**ExperienceTeamsResponse**](ExperienceTeamsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved teams |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

