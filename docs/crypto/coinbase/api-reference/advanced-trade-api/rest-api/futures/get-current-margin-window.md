---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-current-margin-window
api_type: REST
updated_at: 2026-07-05 19:22:39.594007
---

# Get Current Margin Window

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window`


Get the futures current margin window
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "margin_window": {
        "margin_window_type": "MARGIN_WINDOW_TYPE_UNSPECIFIED",
        "end_time": "<string>"
      },
      "is_intraday_margin_killswitch_enabled": true,
      "is_intraday_margin_enrollment_killswitch_enabled": true
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

margin_profile_type

enum<string>

default:MARGIN_PROFILE_TYPE_UNSPECIFIED

The margin profile type for your account.

Available options:

`MARGIN_PROFILE_TYPE_UNSPECIFIED`,

`MARGIN_PROFILE_TYPE_RETAIL_REGULAR`,

`MARGIN_PROFILE_TYPE_RETAIL_INTRADAY_MARGIN_1`

#### Response

A successful response.

margin_window

object

is_intraday_margin_killswitch_enabled

boolean

True if intraday margin killswitch is enabled

is_intraday_margin_enrollment_killswitch_enabled

boolean

True if intraday margin enrollment killswitch is enabled