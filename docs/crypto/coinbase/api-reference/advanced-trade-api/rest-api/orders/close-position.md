---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/close-position
api_type: Trading
updated_at: 2026-07-04 19:26:33.405080
---

# Close Position

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/close_position`


Places an order to close any open positions for a specified `product_id`.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/close_position \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "client_order_id": "0000-00000-000000",
      "product_id": "BIT-28JUL23-CDE",
      "size": 3
    }
    '
    
    
    {
      "success": true,
      "success_response": {
        "order_id": "11111-00000-000000",
        "product_id": "BTC-USD",
        "side": "",
        "client_order_id": "0000-00000-000000"
      },
      "error_response": {
        "error": "UNKNOWN_FAILURE_REASON",
        "message": "The order configuration was invalid",
        "error_details": "Market orders cannot be placed with empty order sizes",
        "preview_failure_reason": "UNKNOWN_PREVIEW_FAILURE_REASON",
        "new_order_failure_reason": "UNKNOWN_FAILURE_REASON"
      },
      "order_configuration": {
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

client_order_id

string

required

The unique ID provided for the order (used for identification purposes).

Example:

`"0000-00000-000000"`

product_id

string

required

The trading pair (e.g. 'BIT-28JUL23-CDE').

Example:

`"BIT-28JUL23-CDE"`

size

string

The amount of contracts that should be closed.

Example:

`3`

#### Response

A successful response.

success

boolean

required

Whether the order was created.

Example:

`true`

success_response

object

error_response

object

order_configuration

object

The configuration of the order (e.g. the order type, size, etc).