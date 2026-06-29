---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/products/get-best-bid-ask
api_type: Market Data
updated_at: 2026-06-29 19:44:48.198965
---

# Get Best Bid/Ask

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/best_bid_ask`


Get the best bid/ask for all products. A subset of all products can be returned instead by using the product_ids input.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/best_bid_ask \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "pricebooks": [
        {
          "product_id": "BTC-USD",
          "bids": [
            {
              "price": "<string>",
              "size": "<string>"
            }
          ],
          "asks": [
            {
              "price": "<string>",
              "size": "<string>"
            }
          ],
          "time": "<string>"
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

product_ids

string[]

The list of trading pairs (e.g. 'BTC-USD').

#### Response

A successful response.

pricebooks

object[]

required