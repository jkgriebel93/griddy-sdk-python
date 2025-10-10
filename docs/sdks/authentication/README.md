# Authentication
(*authentication*)

## Overview

Token generation and refresh operations for NFL API access

### Available Operations

* [generate_token](#generate_token) - Generate Initial Access Token
* [refresh_token](#refresh_token) - Refresh Access Token

## generate_token

Creates a new access token and refresh token for a client device. This is the initial authentication endpoint that establishes a session for accessing NFL APIs. Requires client credentials and device information.

### Example Usage

<!-- UsageSnippet language="python" operationID="generateToken" method="post" path="/identity/v3/token" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.authentication.generate_token(request={
        "client_key": "4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g",
        "client_secret": "CZuvCL49d9OwfGsR",
        "device_id": "3cfdef35-c7fe-4f2d-8630-1ec72f52b44d",
        "device_info": "eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=",
        "network_type": models.NetworkTypeEnum.OTHER,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TokenRequest](../../models/tokenrequest.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## refresh_token

Refreshes an existing access token using a valid refresh token. This endpoint extends the user's session by generating new access and refresh tokens. Requires the previous refresh token and signature verification.

### Example Usage

<!-- UsageSnippet language="python" operationID="refreshToken" method="post" path="/identity/v3/token/refresh" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.authentication.refresh_token(request={
        "client_key": "4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g",
        "client_secret": "CZuvCL49d9OwfGsR",
        "device_id": "3cfdef35-c7fe-4f2d-8630-1ec72f52b44d",
        "device_info": "eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=",
        "network_type": models.NetworkTypeEnum.OTHER,
        "refresh_token": "640b00c7-33d8-44f2-ab46-e3d1284a4061",
        "signature_timestamp": "1758729181",
        "uid": "df990acd951e4bd6940c3babc4341584",
        "uid_signature": "587bdNt6EKYhhX9ASFOELX+2lqE=",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RefreshTokenRequest](../../models/refreshtokenrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |