---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-server-time
api_type: REST
updated_at: 2026-07-07 19:29:58.258028
---

# Get Server Time

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/time`


Get the current time from the Coinbase Advanced API.
    
    
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