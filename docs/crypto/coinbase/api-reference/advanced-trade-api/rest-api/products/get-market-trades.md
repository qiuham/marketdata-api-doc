---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/products/get-market-trades
api_type: Market Data
updated_at: 2026-07-04 19:26:34.630759
---

# Get Market Trades

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/products/{product_id}/ticker`


Get snapshot information by product ID about the last trades (ticks) and best bid/ask.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/products/{product_id}/ticker \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "trades": [
        {
          "trade_id": "34b080bf-fcfd-445a-832b-46b5ddc65601",
          "product_id": "BTC-USD",
          "price": "140.91",
          "size": "4",
          "time": "2021-05-31T09:59:59.000Z",
          "side": "",
          "exchange": "<string>"
        }
      ],
      "best_bid": "291.13",
      "best_ask": "292.40"
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

The trading pair (e.g. 'BTC-USD').

#### Query Parameters

limit

integer<int32>

required

The number of trades to be returned.

start

string

The UNIX timestamp indicating the start of the time interval.

end

string

The UNIX timestamp indicating the end of the time interval.

#### Response

A successful response.

trades

object[]

best_bid

string

The best bid for the `product_id`, in quote currency.

Example:

`"291.13"`

best_ask

string

The best ask for the `product_id`, in quote currency.

Example:

`"292.40"`