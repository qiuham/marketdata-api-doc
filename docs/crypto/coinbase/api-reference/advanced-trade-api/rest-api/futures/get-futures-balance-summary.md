---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-futures-balance-summary
api_type: REST
updated_at: 2026-07-02 19:32:13.665224
---

# Get US Derivatives Balance Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary`


Get a summary of balances for CFM trading
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "balance_summary": {
        "futures_buying_power": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "total_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "cbi_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "cfm_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "total_open_orders_hold_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "unrealized_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "daily_realized_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "initial_margin": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "available_margin": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_threshold": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_buffer_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_buffer_percentage": "<string>",
        "intraday_margin_window_measure": {
          "margin_window_type": "FCM_MARGIN_WINDOW_TYPE_UNSPECIFIED",
          "margin_level": "MARGIN_LEVEL_TYPE_UNSPECIFIED",
          "initial_margin": "<string>",
          "maintenance_margin": "<string>",
          "liquidation_buffer": "<string>",
          "total_hold": "<string>",
          "futures_buying_power": "<string>"
        },
        "overnight_margin_window_measure": {
          "margin_window_type": "FCM_MARGIN_WINDOW_TYPE_UNSPECIFIED",
          "margin_level": "MARGIN_LEVEL_TYPE_UNSPECIFIED",
          "initial_margin": "<string>",
          "maintenance_margin": "<string>",
          "liquidation_buffer": "<string>",
          "total_hold": "<string>",
          "futures_buying_power": "<string>"
        },
        "total_pending_transfers_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "funding_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        }
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Response

A successful response.

balance_summary

object