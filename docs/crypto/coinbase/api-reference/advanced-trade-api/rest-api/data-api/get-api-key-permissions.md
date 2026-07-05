---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/data-api/get-api-key-permissions
api_type: REST
updated_at: 2026-07-05 19:22:39.504844
---

# Get API Key Permissions

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/key_permissions`


Get information about your CDP API key permissions
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/key_permissions \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "can_view": true,
      "can_trade": true,
      "can_transfer": true,
      "can_receive": true,
      "portfolio_uuid": "<string>",
      "portfolio_type": "UNDEFINED"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

can_view

boolean

Indicates whether the API key has view permissions.

can_trade

boolean

Indicates whether the API key has trade permissions.

can_transfer

boolean

Indicates whether the API key has deposit/withdrawal permissions.

can_receive

boolean

Indicates whether the API key has receive inbound payments permissions.

portfolio_uuid

string

The portfolio ID associated with the API key.

portfolio_type

enum<string>

default:UNDEFINED

The type of portfolio

Available options:

`UNDEFINED`,

`DEFAULT`,

`CONSUMER`,

`INTX`