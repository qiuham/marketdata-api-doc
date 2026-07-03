---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary
api_type: Account
updated_at: 2026-07-03 19:28:09.140278
---

# Get Perpetuals Portfolio Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}`


Get a summary of your Perpetuals portfolio
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "portfolios": [
        {
          "portfolio_uuid": "<string>",
          "collateral": "<string>",
          "position_notional": "<string>",
          "open_position_notional": "<string>",
          "pending_fees": "<string>",
          "borrow": "<string>",
          "accrued_interest": "<string>",
          "rolling_debt": "<string>",
          "portfolio_initial_margin": "<string>",
          "portfolio_im_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "portfolio_maintenance_margin": "<string>",
          "portfolio_mm_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "liquidation_percentage": "<string>",
          "liquidation_buffer": "<string>",
          "margin_type": "MARGIN_TYPE_UNSPECIFIED",
          "margin_flags": "PORTFOLIO_MARGIN_FLAGS_UNSPECIFIED",
          "liquidation_status": "PORTFOLIO_LIQUIDATION_STATUS_UNSPECIFIED",
          "unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_balance": {
            "value": "<string>",
            "currency": "<string>"
          }
        }
      ],
      "summary": {
        "unrealized_pnl": {
          "value": "<string>",
          "currency": "<string>"
        },
        "buying_power": {
          "value": "<string>",
          "currency": "<string>"
        },
        "total_balance": {
          "value": "<string>",
          "currency": "<string>"
        },
        "max_withdrawal_amount": {
          "value": "<string>",
          "currency": "<string>"
        }
      }
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

The portfolio UUID.

#### Response

A successful response.

portfolios

object[]

summary

object