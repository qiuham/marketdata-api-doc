---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-intraday-margin-setting
api_type: REST
updated_at: 2026-07-07 19:29:32.612322
---

# Get Intraday Margin Setting

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting`


Get the futures intraday margin setting
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "setting": "INTRADAY_MARGIN_SETTING_UNSPECIFIED"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

setting

enum<string>

default:INTRADAY_MARGIN_SETTING_UNSPECIFIED

Available options:

`INTRADAY_MARGIN_SETTING_UNSPECIFIED`,

`INTRADAY_MARGIN_SETTING_STANDARD`,

`INTRADAY_MARGIN_SETTING_INTRADAY`