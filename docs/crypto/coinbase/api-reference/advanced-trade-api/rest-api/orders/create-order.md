---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/create-order
api_type: Trading
updated_at: 2026-07-02 19:32:14.544124
---

# Create Order

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders`


Create an order with a specified `product_id` (asset-pair), `side` (buy/sell), etc.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "client_order_id": "0000-00000-000000",
      "product_id": "BTC-USD",
      "side": "",
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
      },
      "leverage": "2.0",
      "margin_type": "",
      "retail_portfolio_id": "11111111-1111-1111-1111-111111111111",
      "preview_id": "b40bbff9-17ce-4726-8b64-9de7ae57ad26",
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
      "sor_preference": "SOR_ENABLED",
      "prediction_metadata": {
        "prediction_side": "PREDICTION_SIDE_UNKNOWN",
        "preview_order_est_average_filled_price": "<string>",
        "supports_fractional_base_size": true
      },
      "cost_basis_method": "COST_BASIS_METHOD_UNSPECIFIED"
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

A unique ID provided for the order (used for identification purposes). If the ID provided is not unique, the order will not be created and the order corresponding with that ID will be returned instead.

Example:

`"0000-00000-000000"`

product_id

string

required

The trading pair (e.g. 'BTC-USD').

Example:

`"BTC-USD"`

side

enum<string>

default:""

required

The side of the market that the order is on (e.g. 'BUY', 'SELL').

Available options:

`BUY`,

`SELL`

order_configuration

object

required

The configuration of the order (e.g. the order type, size, etc).

leverage

string

The amount of leverage for the order (default is 1.0).

Example:

`"2.0"`

margin_type

enum<string>

default:""

Margin Type for this order (default is CROSS).

Available options:

`CROSS`,

`ISOLATED`

retail_portfolio_id

string

(Deprecated) The ID of the portfolio to associate the order with. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

Example:

`"11111111-1111-1111-1111-111111111111"`

preview_id

string

Preview ID for this order, to associate this order with a preview request

Example:

`"b40bbff9-17ce-4726-8b64-9de7ae57ad26"`

attached_order_configuration

object

The configuration of the attached order. Only TriggerBracketGtc is eligible. Size field must be omitted as the size of the attached order is the same as that of the parent order.

sor_preference

enum<string>

default:SOR_PREFERENCE_UNSPECIFIED

Smart Order Routing preference for this order. UNSPECIFIED uses default behavior based on user settings.

Available options:

`SOR_PREFERENCE_UNSPECIFIED`,

`SOR_ENABLED`,

`SOR_DISABLED`

Example:

`"SOR_ENABLED"`

prediction_metadata

object

Request metadata specific to prediction market orders.

cost_basis_method

enum<string>

default:COST_BASIS_METHOD_UNSPECIFIED

The cost basis method for the order

Available options:

`COST_BASIS_METHOD_UNSPECIFIED`,

`COST_BASIS_METHOD_HIFO`,

`COST_BASIS_METHOD_LIFO`,

`COST_BASIS_METHOD_FIFO`

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