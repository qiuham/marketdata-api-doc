---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-server-time
api_type: REST
updated_at: 2026-06-30 19:43:28.934476
---

# Get Server Time

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/time`


Get the current time from the Coinbase Advanced API.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/time \
      --header 'Authorization: Bearer <token>'Public

# Get Server Time

Get the current time from the Coinbase Advanced API.

GET

/

api

/

v3

/

brokerage

/

time

Get Server Time
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/time \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "iso": "<string>",
      "epochSeconds": "<string>",
      "epochMillis": "<string>"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

iso

string

An ISO-8601 representation of the timestamp

epochSeconds

string<int64>

A second-precision representation of the timestamp

epochMillis

string<int64>

A millisecond-precision representation of the timestamp

Public

# Get Public Product Book

Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.

GET

/

api

/

v3

/

brokerage

/

market

/

product_book

Get Public Product Book
    
    
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
    
    
    
    {
      "iso": "<string>",
      "epochSeconds": "<string>",
      "epochMillis": "<string>"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

iso

string

An ISO-8601 representation of the timestamp

epochSeconds

string<int64>

A second-precision representation of the timestamp

epochMillis

string<int64>

A millisecond-precision representation of the timestamp