---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-position
api_type: REST
updated_at: 2026-06-30 19:43:27.962512
---

# Get Perpetuals Position

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}/{symbol}`


Get a specific open position on Intx
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}/{symbol} \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "position": {
        "product_id": "<string>",
        "product_uuid": "<string>",
        "portfolio_uuid": "<string>",
        "symbol": "<string>",
        "vwap": {
          "value": "<string>",
          "currency": "<string>"
        },
        "entry_vwap": {
          "value": "<string>",
          "currency": "<string>"
        },
        "position_side": "POSITION_SIDE_UNKNOWN",
        "margin_type": "MARGIN_TYPE_UNSPECIFIED",
        "net_size": "<string>",
        "buy_order_size": "<string>",
        "sell_order_size": "<string>",
        "im_contribution": "<string>",
        "unrealized_pnl": {
          "value": "<string>",
          "currency": "<string>"
        },
        "mark_price": {
          "value": "<string>",
          "currency": "<string>"
        },
        "liquidation_price": {
          "value": "<string>",
          "currency": "<string>"
        },
        "leverage": "<string>",
        "im_notional": {
          "value": "<string>",
          "currency": "<string>"
        },
        "mm_notional": {
          "value": "<string>",
          "currency": "<string>"
        },
        "position_notional": {
          "value": "<string>",
          "currency": "<string>"
        },
        "aggregated_pnl": {
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

symbol

string

required

The trading pair (e.g. 'BTC-PERP-INTX').

#### Response

A successful response.

position

object