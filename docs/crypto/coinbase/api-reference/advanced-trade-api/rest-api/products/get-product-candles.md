---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/products/get-product-candles
api_type: Market Data
updated_at: 2026-07-05 19:22:42.720559
---

# Get Product Candles

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/products/{product_id}/candles`


Get rates for a single product by product ID, grouped in buckets.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/products/{product_id}/candles \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "candles": [
        {
          "start": "1639508050",
          "low": "140.21",
          "high": "140.21",
          "open": "140.21",
          "close": "140.21",
          "volume": "56437345"
        }
      ]
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

start

string

required

The UNIX timestamp indicating the start of the time interval.

end

string

required

The UNIX timestamp indicating the end of the time interval.

granularity

enum<string>

default:UNKNOWN_GRANULARITY

required

The timeframe each candle represents.

Available options:

`UNKNOWN_GRANULARITY`,

`ONE_MINUTE`,

`FIVE_MINUTE`,

`FIFTEEN_MINUTE`,

`THIRTY_MINUTE`,

`ONE_HOUR`,

`TWO_HOUR`,

`FOUR_HOUR`,

`SIX_HOUR`,

`ONE_DAY`

limit

integer<int32>

The number of candle buckets to be returned. By default, returns 350 (max 350).

#### Response

A successful response.

candles

object[]