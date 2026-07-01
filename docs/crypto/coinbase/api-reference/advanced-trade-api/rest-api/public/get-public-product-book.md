---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-book
api_type: Market Data
updated_at: 2026-07-01 19:42:49.606626
---

# Get Public Product Book

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/product_book`


Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/product_book \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "pricebook": {
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
      },
      "last": "<string>",
      "mid_market": "<string>",
      "spread_bps": "<string>",
      "spread_absolute": "<string>"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

product_id

string

required

The trading pair (e.g. 'BTC-USD').

limit

integer<int32>

The number of bid/asks to be returned.

aggregation_price_increment

string

The minimum price intervals at which buy and sell orders are grouped or combined in the order book.

#### Response

A successful response.

pricebook

object

required

last

string

mid_market

string

spread_bps

string

spread_absolute

string