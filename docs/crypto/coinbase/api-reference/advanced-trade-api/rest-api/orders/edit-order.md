---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/edit-order
api_type: Trading
updated_at: 2026-07-04 19:26:33.585379
---

# Edit Order

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/edit`


Edit an order with a specified new `size`, or new `price`.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/edit \
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
      "success": true,
      "errors": [
        {
          "edit_failure_reason": "UNKNOWN_EDIT_ORDER_FAILURE_REASON",
          "preview_failure_reason": "UNKNOWN_PREVIEW_FAILURE_REASON"
        }
      ]
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

success

boolean

required

Whether the order edit request was placed.

Example:

`true`

errors

object[]