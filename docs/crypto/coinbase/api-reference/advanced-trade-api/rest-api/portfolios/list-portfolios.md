---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios
api_type: Account
updated_at: 2026-06-30 19:43:28.388666
---

# List Portfolios

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/portfolios`


Get all portfolios of a user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "portfolios": [
        {
          "name": "<string>",
          "uuid": "<string>",
          "type": "UNDEFINED",
          "deleted": true
        }
      ]
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

portfolio_type

enum<string>

default:UNDEFINED

Only returns portfolios matching this portfolio type.

Available options:

`UNDEFINED`,

`DEFAULT`,

`CONSUMER`,

`INTX`

#### Response

A successful response.

portfolios

object[]