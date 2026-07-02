---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/create-portfolio
api_type: Account
updated_at: 2026-07-02 19:32:15.841386
---

# Create Portfolio

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/portfolios`


Create a portfolio.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios \
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