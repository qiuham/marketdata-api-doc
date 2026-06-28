---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/cancel-order
api_type: Trading
updated_at: 2026-05-27 18:47:37.569256
---

# Cancel Orders

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel`


Initiate cancel requests for one or more orders.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "order_ids": [
        "0000-00000",
        "1111-11111"
      ]
    }
    '
    
    
    {
      "results": [
        {
          "success": true,
          "failure_reason": "UNKNOWN_CANCEL_FAILURE_REASON",
          "order_id": "0000-00000"
        }
      ]
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

order_ids

string[]

required

The order IDs that cancel requests should be initiated for.

Example:
    
    
    ["0000-00000", "1111-11111"]

#### Response

A successful response.

results

object[]

The result of initiated cancel requests