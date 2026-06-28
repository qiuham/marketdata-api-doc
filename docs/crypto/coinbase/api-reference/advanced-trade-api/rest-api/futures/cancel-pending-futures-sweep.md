---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/cancel-pending-futures-sweep
api_type: REST
updated_at: 2026-06-28 19:25:22.076935
---

# Cancel Pending US Derivatives Sweep

**Endpoint:** `DELETE https://api.coinbase.com/api/v3/brokerage/cfm/sweeps`


Cancel the pending sweep of funds from FCM wallet to USD Spot wallet
    
    
    curl --request DELETE \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/sweeps \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "success": true
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

success

boolean