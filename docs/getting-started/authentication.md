# Authentication

The Griddy SDK requires authentication to access NFL data. This guide covers the available authentication methods.

## Overview

NFL APIs require authentication via access tokens. The SDK supports two methods to obtain these tokens:

1. **Pre-obtained auth token** - Provide an existing access token
2. **Browser authentication** - Automatically log in using Playwright

## Method 1: Pre-obtained Auth Token

If you already have an access token (e.g., from browser developer tools):

```python
from griddy.nfl import GriddyNFL

auth_info = {
    "accessToken": "your_access_token_here"
}

nfl = GriddyNFL(nfl_auth=auth_info)
```

### Obtaining an Access Token Manually

1. Log into [NFL.com](https://www.nfl.com) in your browser
2. Open Developer Tools (F12)
3. Go to the Network tab
4. Make a request on the site
5. Look for requests to `api.nfl.com` or `pro.nfl.com`
6. Find the `Authorization` header - it contains the access token

## Method 2: Browser Authentication

The SDK can automatically log in using Playwright:

```python
from griddy.nfl import GriddyNFL

nfl = GriddyNFL(
    login_email="your_email@example.com",
    login_password="your_password",
    headless_login=True  # Set to False to see the browser
)
```

### Prerequisites for Browser Auth

Install Playwright browsers first:

```bash
playwright install chromium
```

### How Browser Auth Works

1. Playwright opens a Chromium browser
2. Navigates to the NFL login page
3. Enters your credentials
4. Captures the authentication token
5. Saves credentials to `creds.json` for reuse

### Reusing Credentials

After browser authentication, credentials are saved to `creds.json`. You can load and reuse them:

```python
import json
from griddy.nfl import GriddyNFL

# Load saved credentials
with open("creds.json", "r") as f:
    auth_info = json.load(f)

# Use saved credentials
nfl = GriddyNFL(nfl_auth=auth_info)
```

## Token Refresh

Access tokens expire periodically. The SDK provides authentication endpoints to refresh tokens:

```python
# Get a fresh token using the authentication endpoint
new_token = nfl.authentication.generate_access_token()
```

## Security Best Practices

!!! warning "Security Notice"
    Never commit credentials or tokens to version control.

### Environment Variables

Store credentials in environment variables:

```python
import os
from griddy.nfl import GriddyNFL

nfl = GriddyNFL(
    login_email=os.environ.get("NFL_EMAIL"),
    login_password=os.environ.get("NFL_PASSWORD"),
    headless_login=True
)
```

### Credential Files

If using a credentials file:

1. Add `creds.json` to `.gitignore`
2. Set appropriate file permissions: `chmod 600 creds.json`

### Token Storage

For production applications:

- Store tokens in a secure secret manager
- Implement token refresh logic
- Never log or expose tokens

## Troubleshooting

### Browser Authentication Fails

**Symptom**: Browser auth hangs or fails to capture token

**Solutions**:

1. Set `headless_login=False` to see what's happening
2. Ensure Playwright browsers are installed: `playwright install chromium`
3. Check if NFL.com has changed their login flow

### Token Expired

**Symptom**: API calls return 401 Unauthorized

**Solutions**:

1. Re-authenticate to get a fresh token
2. Implement automatic token refresh
3. Check token expiration before making calls

### Invalid Credentials

**Symptom**: Login fails with authentication error

**Solutions**:

1. Verify email and password are correct
2. Check if account has MFA enabled (may require manual login)
3. Ensure account is in good standing

## Authentication Flow Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   User Input    │────▶│  Griddy SDK     │────▶│   NFL API       │
│ (email/pass or  │     │ (Authentication)│     │   (Token)       │
│  auth token)    │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌─────────────────┐
                        │  creds.json     │
                        │ (Saved locally) │
                        └─────────────────┘
```

## Next Steps

- [Quick Start Guide](quickstart.md) - Start using the SDK
- [Configuration](../user-guide/configuration.md) - Configure SDK options
