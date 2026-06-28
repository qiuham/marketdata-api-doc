---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/set-intraday-margin-settings
api_type: REST
updated_at: 2026-05-27 18:47:37.499732
---

# Set Intraday Margin Setting

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting`


Set the futures intraday margin setting
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "setting": "INTRADAY_MARGIN_SETTING_UNSPECIFIED"
    }
    '
    
    
    {}

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

setting

enum<string>

default:INTRADAY_MARGIN_SETTING_UNSPECIFIED

The margin setting for the account. Describes whether the account is opted in to receive increased leverage during weekdays (8am-4pm ET), excluding [market holidays](https://www.coinbase.com/derivatives/market-notices).

Available options:

`INTRADAY_MARGIN_SETTING_UNSPECIFIED`,

`INTRADAY_MARGIN_SETTING_STANDARD`,

`INTRADAY_MARGIN_SETTING_INTRADAY`

#### Response

A successful response.

The response is of type `SetIntradayMarginSettingResponse · object`.