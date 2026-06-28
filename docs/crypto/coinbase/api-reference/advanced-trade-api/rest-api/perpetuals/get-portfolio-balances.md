---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances
api_type: Account
updated_at: 2026-06-28 19:25:24.165217
---

# Get Portfolios Balances

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}`


Get a list of asset balances on Intx for a given Portfolio
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "portfolio_balances": [
        {
          "portfolio_uuid": "<string>",
          "balances": [
            {
              "asset": {
                "asset_id": "<string>",
                "asset_uuid": "<string>",
                "asset_name": "<string>",
                "status": "<string>",
                "collateral_weight": "<string>",
                "account_collateral_limit": "<string>",
                "ecosystem_collateral_limit_breached": true,
                "asset_icon_url": "<string>",
                "supported_networks_enabled": true
              },
              "quantity": "<string>",
              "hold": "<string>",
              "transfer_hold": "<string>",
              "collateral_value": "<string>",
              "collateral_weight": "<string>",
              "max_withdraw_amount": "<string>",
              "loan": "<string>",
              "loan_collateral_requirement_usd": "<string>",
              "pledged_quantity": "<string>",
              "max_portfolio_transfer_amount": "<string>"
            }
          ],
          "is_margin_limit_reached": true
        }
      ]
    }

**Deprecated — retires September 9, 2026.** This INTX perpetuals endpoint is being replaced by the [Deribit-powered derivatives gateway](/coinbase-app/advanced-trade-apis/guides/derivatives/overview). Migrate before the cutover — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

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

#### Response

A successful response.

portfolio_balances

object[]