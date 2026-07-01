---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/edit-portfolio
api_type: Account
updated_at: 2026-07-01 19:42:48.928798
---

# Edit Portfolio

**Endpoint:** `PUT https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}`


Edit a portfolio.
    
    
    curl --request PUT \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "name": "<string>"
    }
    '
    
    
    {
      "portfolio": {
        "name": "<string>",
        "uuid": "<string>",
        "type": "UNDEFINED",
        "deleted": true
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

portfolio_uuid

string

required

The portfolio UUID.

#### Body

application/json

name

string

The name of the portfolio.

#### Response

A successful response.

portfolio

object

Portfolio is the identifying information for a portfolio.