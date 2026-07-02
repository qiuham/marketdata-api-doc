---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/payment-methods/list-payment-methods
api_type: REST
updated_at: 2026-07-02 19:32:15.460819
---

# List Payment Methods

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/payment_methods`


Get a list of payment methods for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/payment_methods \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "payment_methods": [
        {
          "id": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
          "type": "ACH",
          "name": "ALLY BANK ******1234",
          "currency": "USD",
          "verified": true,
          "allow_buy": true,
          "allow_sell": true,
          "allow_deposit": true,
          "allow_withdraw": true,
          "created_at": "2021-05-31T09:59:59.000Z",
          "updated_at": "2021-05-31T09:59:59.000Z"
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

payment_methods

object[]