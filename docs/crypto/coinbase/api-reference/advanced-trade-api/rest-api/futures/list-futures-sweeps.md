---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/list-futures-sweeps
api_type: REST
updated_at: 2026-07-04 19:26:33.352109
---

# List US Derivatives Sweeps

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/sweeps`


Get pending and processing sweeps of funds from FCM wallet to USD Spot wallet
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/sweeps \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "sweeps": [
        {
          "id": "<string>",
          "requested_amount": {
            "value": "<string>",
            "currency": "<string>",
            "cbrn": "<string>"
          },
          "should_sweep_all": true,
          "status": "UNKNOWN_FCM_SWEEP_STATUS",
          "scheduled_time": "<string>"
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

sweeps

object[]