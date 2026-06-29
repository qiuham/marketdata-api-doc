---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out
api_type: REST
updated_at: 2026-06-29 19:44:47.817764
---

# Opt In or Out of Multi Asset Collateral

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral`


Enable or Disable Multi Asset Collateral for a given Portfolio
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "portfolio_uuid": "<string>",
      "multi_asset_collateral_enabled": true
    }
    '
    
    
    {
      "multi_asset_collateral_enabled": true
    }

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

multi_asset_collateral_enabled

boolean

Enable or disable Multi Asset Collateral.

#### Response

A successful response.

multi_asset_collateral_enabled

boolean