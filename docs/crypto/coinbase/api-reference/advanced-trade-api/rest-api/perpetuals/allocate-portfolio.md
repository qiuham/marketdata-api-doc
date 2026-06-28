---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio
api_type: Account
updated_at: 2026-06-28 19:25:23.783059
---

# Allocate Portfolio

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/intx/allocate`


Allocate portfolio funds to a sub-portfolio on Intx Portfolio
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/intx/allocate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "portfolio_uuid": "<string>",
      "symbol": "<string>",
      "amount": "<string>",
      "currency": "<string>"
    }
    '
    
    
    {}

**Deprecated — retires September 9, 2026.** This INTX perpetuals endpoint is being replaced by the [Deribit-powered derivatives gateway](/coinbase-app/advanced-trade-apis/guides/derivatives/overview). Migrate before the cutover — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

portfolio_uuid

string

The portfolio UUID.

symbol

string

The trading pair (e.g. 'BTC-PERP-INTX').

amount

string

The amount to be allocated for the specified isolated position.

currency

string

The currency to be allocated for the specific isolated position (e.g. USD, BTC, etc).

#### Response

A successful response.

The response is of type `object`.