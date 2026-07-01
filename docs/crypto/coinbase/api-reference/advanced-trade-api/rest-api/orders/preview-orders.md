---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/preview-orders
api_type: Trading
updated_at: 2026-07-01 19:42:47.817943
---

# Preview Order

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/preview`


Preview an order.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/preview \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "product_id": "<string>",
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
      "prediction_metadata": {
        "prediction_side": "PREDICTION_SIDE_UNKNOWN",
        "preview_order_est_average_filled_price": "<string>",
        "supports_fractional_base_size": true
      },
      "cost_basis_method": "COST_BASIS_METHOD_UNSPECIFIED"
    }
    '
    
    
    {
      "order_total": "<string>",
      "commission_total": "<string>",
      "errs": [
        "UNKNOWN_PREVIEW_FAILURE_REASON"
      ],
      "warning": [
        "UNKNOWN"
      ],
      "quote_size": 10,
      "base_size": 0.001,
      "best_bid": "<string>",
      "best_ask": "<string>",
      "is_max": true,
      "order_margin_total": "<string>",
      "leverage": "2.0",
      "long_leverage": "<string>",
      "short_leverage": "<string>",
      "slippage": "<string>",
      "preview_id": "<string>",
      "current_liquidation_buffer": "<string>",
      "projected_liquidation_buffer": "<string>",
      "max_leverage": "<string>",
      "pnl_configuration": {
        "trigger_bracket_pnl": {
          "take_profit_pnl": "<string>",
          "stop_loss_pnl": "<string>"
        }
      },
      "twap_bucket_metadata": {
        "bucket_duration": "<string>",
        "bucket_size": "<string>",
        "number_buckets": "<string>",
        "start_time": "<string>",
        "end_time": "<string>"
      },
      "position_notional_limit": "<string>",
      "max_notional_at_requested_leverage": "<string>",
      "margin_ratio_data": {
        "current_margin_ratio": "<string>",
        "projected_margin_ratio": "<string>"
      },
      "commission_detail_total": {
        "total_commission": "<string>",
        "gst_commission": "<string>",
        "withholding_commission": "<string>",
        "client_commission": "<string>",
        "venue_commission": "<string>",
        "regulatory_commission": "<string>",
        "clearing_commission": "<string>"
      },
      "scaled_metadata": {
        "scaled_order_distribution": [
          {
            "size": "<string>",
            "price": "<string>",
            "errs": [
              "UNKNOWN_PREVIEW_FAILURE_REASON"
            ],
            "warning": [
              "UNKNOWN"
            ]
          }
        ]
      },
      "compliance_limit_data": {
        "total_limit": {
          "value": "1.23",
          "currency": "BTC"
        },
        "remaining_limits": {
          "value": "1.23",
          "currency": "BTC"
        }
      },
      "est_average_filled_price": "<string>",
      "prediction_order_metadata": {
        "contract_subtotal": "<string>",
        "user_net_total": "<string>",
        "slippage_percentage": "<string>",
        "minimum_contracts": "<string>",
        "minimum_total": {
          "value": "1.23",
          "currency": "BTC"
        },
        "maximum_total": {
          "value": "1.23",
          "currency": "BTC"
        },
        "maximum_contracts": "<string>"
      },
      "predicted_liquidation_price": "<string>"
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

product_id

string

required

The trading pair (e.g. 'BTC-USD').

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

attached_order_configuration

object

The configuration of the attached order. Only TriggerBracketGtc is eligible. Size field must be omitted as the size of the attached order is the same as that of the parent order.

prediction_metadata

object

Request metadata specific to prediction market orders (YES/NO).

cost_basis_method

enum<string>

default:COST_BASIS_METHOD_UNSPECIFIED

The method used to calculate the cost basis for the order.

Available options:

`COST_BASIS_METHOD_UNSPECIFIED`,

`COST_BASIS_METHOD_HIFO`,

`COST_BASIS_METHOD_LIFO`,

`COST_BASIS_METHOD_FIFO`

#### Response

A successful response.

order_total

string

required

commission_total

string

required

Currency amount of the applied commission (so not the rate that was used on input)

errs

enum<string>[]

required

List of potential failure reasons were this order to be submitted

Available options:

`UNKNOWN_PREVIEW_FAILURE_REASON`,

`PREVIEW_MISSING_COMMISSION_RATE`,

`PREVIEW_INVALID_SIDE`,

`PREVIEW_INVALID_ORDER_CONFIG`,

`PREVIEW_INVALID_PRODUCT_ID`,

`PREVIEW_INVALID_SIZE_PRECISION`,

`PREVIEW_INVALID_PRICE_PRECISION`,

`PREVIEW_MISSING_PRODUCT_PRICE_BOOK`,

`PREVIEW_INVALID_LEDGER_BALANCE`,

`PREVIEW_INSUFFICIENT_LEDGER_BALANCE`,

`PREVIEW_INVALID_LIMIT_PRICE_POST_ONLY`,

`PREVIEW_INVALID_LIMIT_PRICE`,

`PREVIEW_INVALID_NO_LIQUIDITY`,

`PREVIEW_INSUFFICIENT_FUND`,

`PREVIEW_INVALID_COMMISSION_CONFIGURATION`,

`PREVIEW_INVALID_STOP_PRICE`,

`PREVIEW_INVALID_BASE_SIZE_TOO_LARGE`,

`PREVIEW_INVALID_BASE_SIZE_TOO_SMALL`,

`PREVIEW_INVALID_QUOTE_SIZE_PRECISION`,

`PREVIEW_INVALID_QUOTE_SIZE_TOO_LARGE`,

`PREVIEW_INVALID_PRICE_TOO_LARGE`,

`PREVIEW_INVALID_QUOTE_SIZE_TOO_SMALL`,

`PREVIEW_INSUFFICIENT_FUNDS_FOR_FUTURES`,

`PREVIEW_BREACHED_PRICE_LIMIT`,

`PREVIEW_BREACHED_ACCOUNT_POSITION_LIMIT`,

`PREVIEW_BREACHED_COMPANY_POSITION_LIMIT`,

`PREVIEW_INVALID_MARGIN_HEALTH`,

`PREVIEW_RISK_PROXY_FAILURE`,

`PREVIEW_UNTRADABLE_FCM_ACCOUNT_STATUS`,

`PREVIEW_IN_LIQUIDATION`,

`PREVIEW_INVALID_MARGIN_TYPE`,

`PREVIEW_INVALID_LEVERAGE`,

`PREVIEW_UNTRADABLE_PRODUCT`,

`PREVIEW_INVALID_FCM_TRADING_SESSION`,

`PREVIEW_NOT_ALLOWED_BY_MARKET_STATE`,

`PREVIEW_BREACHED_OPEN_INTEREST_LIMIT`,

`PREVIEW_GEOFENCING_RESTRICTION`,

`PREVIEW_INVALID_END_TIME`,

`PREVIEW_OPPOSITE_MARGIN_TYPE_EXISTS`,

`PREVIEW_QUOTE_SIZE_NOT_ALLOWED_FOR_BRACKET`,

`PREVIEW_INVALID_BRACKET_PRICES`,

`PREVIEW_MISSING_MARKET_TRADE_DATA`,

`PREVIEW_INVALID_BRACKET_LIMIT_PRICE`,

`PREVIEW_INVALID_BRACKET_STOP_TRIGGER_PRICE`,

`PREVIEW_BRACKET_LIMIT_PRICE_OUT_OF_BOUNDS`,

`PREVIEW_STOP_TRIGGER_PRICE_OUT_OF_BOUNDS`,

`PREVIEW_BRACKET_ORDER_NOT_SUPPORTED`,

`PREVIEW_INVALID_STOP_PRICE_PRECISION`,

`PREVIEW_STOP_PRICE_ABOVE_LIMIT_PRICE`,

`PREVIEW_STOP_PRICE_BELOW_LIMIT_PRICE`,

`PREVIEW_STOP_PRICE_ABOVE_LAST_TRADE_PRICE`,

`PREVIEW_STOP_PRICE_BELOW_LAST_TRADE_PRICE`,

`PREVIEW_FOK_DISABLED`,

`PREVIEW_FOK_ONLY_ALLOWED_ON_LIMIT_ORDERS`,

`PREVIEW_POST_ONLY_NOT_ALLOWED_WITH_FOK`,

`PREVIEW_UBO_HIGH_LEVERAGE_QUANTITY_BREACHED`,

`PREVIEW_ECOSYSTEM_LEVERAGE_UTILIZATION_BREACHED`,

`PREVIEW_CLOSE_ONLY_FAILURE`,

`PREVIEW_UBO_HIGH_LEVERAGE_NOTIONAL_BREACHED`,

`PREVIEW_END_TIME_TOO_FAR_IN_FUTURE`,

`PREVIEW_LIMIT_PRICE_TOO_FAR_FROM_MARKET`,

`PREVIEW_FUTURES_AFTER_HOUR_INVALID_ORDER_TYPE`,

`PREVIEW_FUTURES_AFTER_HOUR_INVALID_TIME_IN_FORCE`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_PRICE`,

`PREVIEW_INVALID_ATTACHED_STOP_LOSS_PRICE`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_PRICE_PRECISION`,

`PREVIEW_INVALID_ATTACHED_STOP_LOSS_PRICE_PRECISION`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_PRICE_OUT_OF_BOUNDS`,

`PREVIEW_INVALID_ATTACHED_STOP_LOSS_PRICE_OUT_OF_BOUNDS`,

`PREVIEW_INVALID_BRACKET_ORDER_SIDE`,

`PREVIEW_BRACKET_ORDER_SIZE_EXCEEDS_POSITION`,

`PREVIEW_ORDER_SIZE_EXCEEDS_BRACKETED_POSITION`,

`PREVIEW_INVALID_LIMIT_PRICE_PRECISION`,

`PREVIEW_INVALID_STOP_TRIGGER_PRICE_PRECISION`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_PRICE_EXCEEDS_MAX_DISTANCE_FROM_ORIGINATING_PRICE`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_SIZE_BELOW_MIN`,

`PREVIEW_ATTACHED_ORDER_SIZE_MUST_BE_NIL`,

`PREVIEW_BELOW_MIN_SIZE_FOR_DURATION`,

`PREVIEW_MAX_DAILY_VOLUME_NOTIONAL_BREACHED`,

`PREVIEW_INVALID_SETTLEMENT_CURRENCY`,

`PREVIEW_DURATION_TOO_SMALL`,

`PREVIEW_INTX_FOK_ONLY_ALLOWED_ON_LIMIT_AND_MARKET_ORDERS`,

`PREVIEW_BUCKET_SIZE_SMALLER_THAN_QUOTE_MIN`,

`PREVIEW_BUCKET_SIZE_SMALLER_THAN_BASE_MIN`,

`PREVIEW_END_TIME_AFTER_CONTRACT_EXPIRATION`,

`PREVIEW_START_TIME_MUST_BE_SPECIFIED`,

`PREVIEW_ICEBERG_ORDERS_NOT_SUPPORTED`,

`PREVIEW_END_TIME_IS_IN_THE_PAST`,

`PREVIEW_GTD_ORDERS_MUST_HAVE_END_TIME`,

`PREVIEW_ATTACHED_ORDER_MUST_HAVE_POSITIVE_PRICES`,

`PREVIEW_INVALID_ORDER_SIDE_FOR_ATTACHED_TPSL`,

`PREVIEW_ATTACHED_ORDERS_ONLY_ALLOWED_ON_MARKET_LIMIT`,

`PREVIEW_INVALID_ORDER_TYPE_FOR_ATTACHED`,

`PREVIEW_PRICE_NOT_ALLOWED_FOR_MARKET_ORDERS`,

`PREVIEW_REDUCE_ONLY_NOT_ALLOWED_ON_VENUE`,

`PREVIEW_NON_NUMERIC_ORDER_SIZE`,

`PREVIEW_INVALID_INTX_CLIENT_ORDER_ID`,

`PREVIEW_DURATION_TOO_LARGE`,

`PREVIEW_REDUCE_ONLY_NOT_ALLOWED_ON_SPOT_PRODUCTS`,

`PREVIEW_LIMIT_ORDER_PRICE_EXCEEDS_PRICE_BAND_ON_BUY`,

`PREVIEW_LIMIT_ORDER_PRICE_EXCEEDS_PRICE_BAND_ON_SELL`,

`PREVIEW_INVALID_ATTACHED_TAKE_PROFIT_PRICE_OUT_OF_BOUNDS_ON_AGGRESSIVE_ORDER`,

`PREVIEW_INVALID_ATTACHED_STOP_LOSS_PRICE_OUT_OF_BOUNDS_ON_AGGRESSIVE_ORDER`,

`PREVIEW_STOP_TRIGGERED`,

`PREVIEW_REPLACE_NOT_SUPPORTED`,

`PREVIEW_ORDER_IS_PENDING_CANCEL`,

`PREVIEW_POSITION_SIZE_INCREASE_REJECT`,

`PREVIEW_ASSET_BALANCE_INCREASE_REJECT`,

`PREVIEW_TOO_MANY_PENDING_REPLACES`,

`PREVIEW_INVALID_RFQ_BASE_SIZE_TOO_SMALL`,

`PREVIEW_INVALID_RFQ_BASE_SIZE_TOO_LARGE`,

`PREVIEW_INVALID_RFQ_QUOTE_SIZE_TOO_SMALL`,

`PREVIEW_INVALID_RFQ_QUOTE_SIZE_TOO_LARGE`,

`PREVIEW_REDUCE_ONLY_INCREASED_POSITION_SIZE`,

`PREVIEW_COMPLIANCE_PURCHASE_LIMIT_EXCEEDED`,

`PREVIEW_SCALED_PARAM_INFEASIBLE`,

`PREVIEW_SCALED_MIN_ORDER_VIOLATION`,

`PREVIEW_SCALED_MAX_ORDER_VIOLATION`,

`PREVIEW_POST_ONLY_NOT_ALLOWED_WITH_PEG`,

`PREVIEW_INVALID_PEG_OFFSET`,

`PREVIEW_INVALID_PEG_WIG_LEVEL`,

`PREVIEW_INVALID_PEG_VENUE_OPTIONS`,

`PREVIEW_PEG_INVALID_ORDER_TYPE`,

`PREVIEW_SINGLE_LEGGED_TPSL_NOT_ALLOWED`,

`PREVIEW_FRACTIONAL_ORDERS_NOT_ALLOWED_FOR_PRODUCT`,

`PREVIEW_QUOTE_ORDERS_NOT_ALLOWED_FOR_PRODUCT`,

`PREVIEW_NBBO_NOT_PROVIDED`,

`PREVIEW_INVALID_NBBO_BID_PRICE`,

`PREVIEW_INVALID_NBBO_ASK_PRICE`,

`PREVIEW_NOTIONAL_SIZE_BREACHES_FRACTIONAL_MINIMUM`,

`PREVIEW_MARKET_ORDERS_PROHIBITED_DURING_NON_CORE_SESSION`,

`PREVIEW_NOTIONAL_ORDERS_PROHIBITED_DURING_NON_CORE_SESSION`,

`PREVIEW_MAX_NOTIONAL_PER_ORDER_BREACHED_15C35_CHECK`,

`PREVIEW_MAX_SHARES_PER_ORDER_BREACHED_15C35_CHECK`,

`PREVIEW_INVALID_EQUITY_TRADING_SESSION`,

`PREVIEW_PRODUCT_TRADING_HALTED`,

`PREVIEW_TRADING_DISABLED`,

`PREVIEW_INVALID_BRACKET_LIMIT_PRICE_PRECISION`,

`PREVIEW_SCALED_PARAM_DISCREPANCY`,

`PREVIEW_STOP_LOSS_PRICE_TOO_LOW`,

`PREVIEW_PREDICTIONS_QUOTE_SIZE_BELOW_MIN_CONTRACT_PRICE`,

`PREVIEW_PREDICTIONS_HIGH_PRICE_CONTRACTS_BLOCKED`,

`PREVIEW_ATTACHED_STOP_LOSS_PRICE_TOO_LOW`,

`PREVIEW_BREACHED_RISK_LIMIT`,

`PREVIEW_STOP_LOSS_PRICE_TOO_HIGH`,

`PREVIEW_ATTACHED_STOP_LOSS_PRICE_TOO_HIGH`,

`PREVIEW_TAKE_PROFIT_PRICE_TOO_HIGH`,

`PREVIEW_ATTACHED_TAKE_PROFIT_PRICE_TOO_HIGH`,

`PREVIEW_TAKE_PROFIT_PRICE_TOO_LOW`,

`PREVIEW_ATTACHED_TAKE_PROFIT_PRICE_TOO_LOW`

warning

enum<string>[]

required

Available options:

`UNKNOWN`,

`BIG_ORDER`,

`SMALL_ORDER`,

`DURATION_EXTENDED_BY_MARKET_CLOSE`,

`OPEN_ORDERS_EXCEED_COMPLIANCE_PURCHASE_LIMIT_MAY_CANCEL`

quote_size

string

required

The amount of the second Asset in the Trading Pair. For example, on the BTC/USD Order Book, USD is the Quote Asset.

Example:

`10`

base_size

string

required

The amount of the first Asset in the Trading Pair. For example, on the BTC-USD Order Book, BTC is the Base Asset.

Example:

`0.001`

best_bid

string

required

best_ask

string

required

is_max

boolean

required

Indicates whether tradable_balance should be set to the maximum amount.

order_margin_total

string

leverage

string

The amount of leverage for the order (default is 1.0).

Example:

`"2.0"`

long_leverage

string

short_leverage

string

slippage

string

preview_id

string

current_liquidation_buffer

string

projected_liquidation_buffer

string

max_leverage

string

pnl_configuration

object

Expected PNL of an order. This value is an estimate and does not take into account fees and slippage.

twap_bucket_metadata

Twap bucket metadata - size/duration of each suborder into which twap is broken into · object

position_notional_limit

string

max_notional_at_requested_leverage

string

margin_ratio_data

New margin ratio fields replacing current_liquidation_buffer and projected_liquidation_buffer · object

commission_detail_total

CommissionDetailTotal contains the breakdown of commission charges for an order · object

Breakdown of commission charges for the order

scaled_metadata

a list of scaled order distributions · object

Metadata for scaled orders containing the order distribution

compliance_limit_data

Compliance Limit service data · object

Optional compliance limit data

est_average_filled_price

string

Estimated fill price for order.

prediction_order_metadata

Prediction market-specific metadata for the order preview response · object

Metadata specific to prediction market orders.

predicted_liquidation_price

string

Predicted liquidation price for FCM orders.