---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/accounts/list-accounts
api_type: Account
updated_at: 2026-07-02 19:32:13.236795
---

# List Accounts

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/accounts`


Get a list of authenticated accounts for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/accounts \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "has_next": true,
      "accounts": [
        {
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
      ],
      "cursor": "789100",
      "size": 123
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

limit

integer<int32>

The number of accounts to display per page. By default, displays 49 (max 250). If `has_next` is true, additional pages of accounts are available to be fetched. Use the `cursor` parameter to start on a specified page.

cursor

string

For paginated responses, returns all responses that come after this value.

retail_portfolio_id

string

(Deprecated) Only returns the accounts matching the portfolio ID. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

#### Response

A successful response.

has_next

boolean

required

Whether there are additional pages for this query.

Example:

`true`

accounts

object[]

cursor

string

For paginated responses, returns all responses that come after this value.

Example:

`"789100"`

size

integer<int32>

Number of accounts returned