---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/move-portfolios-funds
api_type: Account
updated_at: 2026-07-07 19:29:55.895510
---

# Move Portfolio Funds

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds`


Move funds between portfolios.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "funds": {
        "value": "<string>",
        "currency": "<string>"
      },
      "source_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
      "target_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe"
    }
    '
    
    
    {
      "source_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
      "target_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

funds

object

The amount to be moved to the specified portfolio.

source_portfolio_uuid

string

The UUID of the portfolio to send funds from.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

target_portfolio_uuid

string

The UUID of the portfolio to send funds to.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

#### Response

A successful response.

source_portfolio_uuid

string

The UUID of the portfolio to send funds from.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

target_portfolio_uuid

string

The UUID of the portfolio to send funds to.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`