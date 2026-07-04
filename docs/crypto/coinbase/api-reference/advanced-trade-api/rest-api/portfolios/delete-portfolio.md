---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/delete-portfolio
api_type: Account
updated_at: 2026-07-04 19:26:34.389516
---

# Delete Portfolio

**Endpoint:** `DELETE https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}`


Delete portfolio.
    
    
    curl --request DELETE \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    {}

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

#### Response

A successful response.

The response is of type `object`.