---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/schedule-futures-sweep
api_type: REST
updated_at: 2026-07-07 19:30:40.547861
---

# Schedule US Derivatives Sweep

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/cfm/sweeps/schedule`


Schedules a sweep of funds from FCM wallet to USD Spot wallet
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/sweeps/schedule \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "usd_amount": "<string>"
    }
    '
    
    
    {
      "success": true
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

usd_amount

string

The amount of USD to be swept. By default, sweeps all available excess funds.

#### Response

A successful response.

success

boolean