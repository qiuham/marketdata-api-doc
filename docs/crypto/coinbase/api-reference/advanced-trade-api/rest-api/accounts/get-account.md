---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/accounts/get-account
api_type: Account
updated_at: 2026-06-30 19:43:26.066195
---

# Get Account

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}`


Get a list of information about an account, given an account UUID.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "account": {
        "uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
        "name": "BTC Wallet",
        "currency": "BTC",
        "available_balance": {
          "value": "1.23",
          "currency": "BTC"
        },
        "default": false,
        "active": true,
        "created_at": "2021-05-31T09:59:59.000Z",
        "updated_at": "2021-05-31T09:59:59.000Z",
        "deleted_at": "2021-05-31T09:59:59.000Z",
        "type": "FIAT",
        "ready": true,
        "hold": {
          "value": "1.23",
          "currency": "BTC"
        },
        "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
        "platform": "ACCOUNT_PLATFORM_CONSUMER"
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

account_uuid

string

required

The account's UUID.

#### Response

A successful response.

account

object