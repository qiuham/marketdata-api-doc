---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/edit-order-preview
api_type: Trading
updated_at: 2026-07-03 19:28:08.213693
---

# Edit Order Preview

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/edit_preview`


Preview an edit order request with a specified new `size`, or new `price`.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/edit_preview \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "order_id": "<string>",
      "price": "19000.00",
      "size": "0.001",
      "attached_order_configuration": {
        "market_market_ioc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "rfq_disabled": true
        },
        "market_market_fok": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "rfq_disabled": true
        },
        "sor_limit_ioc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "rfq_disabled": true
        },
        "limit_limit_gtc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "post_only": false,
          "rfq_disabled": true
        },
        "limit_limit_gtd": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "end_time": "2021-05-31T09:59:59.000Z",
          "post_only": false
        },
        "limit_limit_fok": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "rfq_disabled": true
        },
        "twap_limit_gtd": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "start_time": "2021-05-31T07:59:59.000Z",
          "end_time": "2021-05-31T09:59:59.000Z",
          "limit_price": "10000.00",
          "number_buckets": "5",
          "bucket_size": "2.00",
          "bucket_duration": "300s"
        },
        "stop_limit_stop_limit_gtc": {
          "base_size": "0.001",
          "limit_price": "10000.00",
          "stop_price": "20000.00",
          "stop_direction": "20000.00"
        },
        "stop_limit_stop_limit_gtd": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_price": "20000.00",
          "end_time": "2021-05-31T09:59:59.000Z",
          "stop_direction": "20000.00"
        },
        "trigger_bracket_gtc": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_trigger_price": "20000.00"
        },
        "trigger_bracket_gtd": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_trigger_price": "20000.00",
          "end_time": "2021-05-31T09:59:59.000Z"
        },
        "scaled_limit_gtc": {
          "orders": [
            {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "post_only": false,
              "rfq_disabled": true
            }
          ],
          "quote_size": "<string>",
          "base_size": "<string>",
          "num_orders": 123,
          "min_price": "<string>",
          "max_price": "<string>",
          "price_distribution": "FLAT",
          "size_distribution": "UNKNOWN_DISTRIBUTION",
          "size_diff": "<string>",
          "size_ratio": "<string>"
        }
      },
      "cancel_attached_order": "true",
      "stop_price": "17000.00",
      "average_entry_price": "18000.00"
    }
    '
    
    
    {
      "errors": [
        {
          "edit_failure_reason": "UNKNOWN_EDIT_ORDER_FAILURE_REASON",
          "preview_failure_reason": "UNKNOWN_PREVIEW_FAILURE_REASON"
        }
      ],
      "slippage": "<string>",
      "order_total": "<string>",
      "commission_total": "<string>",
      "quote_size": 10,
      "base_size": 0.001,
      "best_bid": "<string>",
      "best_ask": "<string>",
      "average_filled_price": "<string>",
      "order_margin_total": "<string>",
      "commission_detail_total": {
        "total_commission": "<string>",
        "gst_commission": "<string>",
        "withholding_commission": "<string>",
        "client_commission": "<string>",
        "venue_commission": "<string>",
        "regulatory_commission": "<string>",
        "clearing_commission": "<string>"
      },
      "pnl_configuration": {
        "trigger_bracket_pnl": {
          "take_profit_pnl": "<string>",
          "stop_loss_pnl": "<string>"
        }
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

order_id

string

required

The ID of the order.

price

string

required

The update price of the order.

Example:

`"19000.00"`

size

string

required

The updated size of the order.

Example:

`"0.001"`

attached_order_configuration

object

The configuration of the attached order. Only TriggerBracketGtc, LimitLimitGtc or StopLimitStopLimitGtc are eligible.

cancel_attached_order

boolean

Drops both the legs of TP/SL, order becomes a simple limit order.

Example:

`"true"`

stop_price

string

The updated stop price of the order. Only applicable for editing TP/SL or SL orders.

Example:

`"17000.00"`

average_entry_price

string

The average entry price of the position. Used for estimated PnL

Example:

`"18000.00"`

#### Response

A successful response.

errors

object[]

required

slippage

string

order_total

string

commission_total

string

quote_size

string

The amount of the second Asset in the Trading Pair. For example, on the BTC/USD Order Book, USD is the Quote Asset.

Example:

`10`

base_size

string

The amount of the first Asset in the Trading Pair. For example, on the BTC-USD Order Book, BTC is the Base Asset.

Example:

`0.001`

best_bid

string

best_ask

string

average_filled_price

string

order_margin_total

string

commission_detail_total

CommissionDetailTotal contains the breakdown of commission charges for an order · object

Breakdown of commission charges for the order

pnl_configuration

object

Expected PNL of an order. This value is an estimate and does not take into account fees and slippage.