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
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.authentication.generate_token(client_key="4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g", client_secret="CZuvCL49d9OwfGsR", device_id="3cfdef35-c7fe-4f2d-8630-1ec72f52b44d", device_info="eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=", network_type="other")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `client_key`                                                                                                                           | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Client application identifier key                                                                                                      | 4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g                                                                                                       |
| `client_secret`                                                                                                                        | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Client application secret for authentication                                                                                           | CZuvCL49d9OwfGsR                                                                                                                       |
| `device_id`                                                                                                                            | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Unique device identifier (UUID format)                                                                                                 | 3cfdef35-c7fe-4f2d-8630-1ec72f52b44d                                                                                                   |
| `device_info`                                                                                                                          | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Base64-encoded JSON containing device information such as: {"model":"desktop","version":"Chrome","osName":"Windows","osVersion":"10"}  | eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=                                   |
| `network_type`                                                                                                                         | [Optional[models.NetworkTypeEnum]](../../models/networktypeenum.md)                                                                    | :heavy_minus_sign:                                                                                                                     | Type of network connection                                                                                                             |                                                                                                                                        |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |
| `server_url`                                                                                                                           | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | An optional server URL to use.                                                                                                         | http://localhost:8080                                                                                                                  |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## refresh_token

Refreshes an existing access token using a valid refresh token. This endpoint extends the user's session by generating new access and refresh tokens. Requires the previous refresh token and signature verification.

### Example Usage

<!-- UsageSnippet language="python" operationID="refreshToken" method="post" path="/identity/v3/token/refresh" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.authentication.refresh_token(client_key="4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g", client_secret="CZuvCL49d9OwfGsR", device_id="3cfdef35-c7fe-4f2d-8630-1ec72f52b44d", device_info="eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=", network_type="other", refresh_token="640b00c7-33d8-44f2-ab46-e3d1284a4061", signature_timestamp="1758729181", uid="df990acd951e4bd6940c3babc4341584", uid_signature="587bdNt6EKYhhX9ASFOELX+2lqE=")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `client_key`                                                                                                                           | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Client application identifier key                                                                                                      | 4cFUW6DmwJpzT9L7LrG3qRAcABG5s04g                                                                                                       |
| `client_secret`                                                                                                                        | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Client application secret for authentication                                                                                           | CZuvCL49d9OwfGsR                                                                                                                       |
| `device_id`                                                                                                                            | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Unique device identifier (UUID format)                                                                                                 | 3cfdef35-c7fe-4f2d-8630-1ec72f52b44d                                                                                                   |
| `device_info`                                                                                                                          | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Base64-encoded JSON containing device information such as: {"model":"desktop","version":"Chrome","osName":"Windows","osVersion":"10"}  | eyJtb2RlbCI6ImRlc2t0b3AiLCJ2ZXJzaW9uIjoiQ2hyb21lIiwib3NOYW1lIjoiV2luZG93cyIsIm9zVmVyc2lvbiI6IjEwIn0=                                   |
| `network_type`                                                                                                                         | [Optional[models.NetworkTypeEnum]](../../models/networktypeenum.md)                                                                    | :heavy_minus_sign:                                                                                                                     | Type of network connection                                                                                                             |                                                                                                                                        |
| `refresh_token`                                                                                                                        | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Valid refresh token from previous authentication                                                                                       | 640b00c7-33d8-44f2-ab46-e3d1284a4061                                                                                                   |
| `signature_timestamp`                                                                                                                  | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Unix timestamp for signature verification                                                                                              | 1758729181                                                                                                                             |
| `uid`                                                                                                                                  | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | User identifier hash                                                                                                                   | df990acd951e4bd6940c3babc4341584                                                                                                       |
| `uid_signature`                                                                                                                        | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | HMAC signature for request verification                                                                                                | 587bdNt6EKYhhX9ASFOELX+2lqE=                                                                                                           |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |
| `server_url`                                                                                                                           | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | An optional server URL to use.                                                                                                         | http://localhost:8080                                                                                                                  |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |