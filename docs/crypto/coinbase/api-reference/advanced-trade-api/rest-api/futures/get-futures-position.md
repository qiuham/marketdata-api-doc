---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-futures-position
api_type: REST
updated_at: 2026-06-29 19:44:46.569970
---

# Get US Derivatives Position

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/positions/{product_id}`


Get positions for a specific CFM product
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/positions/{product_id} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "position": {
        "product_id": "<string>",
        "expiration_time": "<string>",
        "side": "UNKNOWN",
        "number_of_contracts": "<string>",
        "current_price": "<string>",
        "avg_entry_price": "<string>",
        "unrealized_pnl": "<string>",
        "daily_realized_pnl": "<string>"
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

product_id

string

required

The ticker symbol (e.g. 'BIT-28JUL23-CDE').

#### Response

A successful response.

position

object