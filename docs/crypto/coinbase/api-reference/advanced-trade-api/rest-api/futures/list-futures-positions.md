---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/list-futures-positions
api_type: REST
updated_at: 2026-07-01 19:42:47.306857
---

# List US Derivatives Positions

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/positions`


Get a list of positions in CFM products
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/positions \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "positions": [
        {
          "product_id": "<string>",
          "expiration_time": "<string>",
          "side": "UNKNOWN",
          "number_of_contracts": "<string>",
          "current_price": "<string>",
          "avg_entry_price": "<string>",
          "unrealized_pnl": "<string>",
          "daily_realized_pnl": "<string>"
        }
      ]
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

positions

object[]