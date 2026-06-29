---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/products/list-products
api_type: Market Data
updated_at: 2026-06-29 19:44:48.447346
---

# List Products

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/products`


Get a list of the available currency pairs for trading.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/products \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "products": [
        {
          "product_id": "BTC-USD",
          "price": "140.21",
          "price_percentage_change_24h": "9.43%",
          "volume_24h": "1908432",
          "volume_percentage_change_24h": "9.43%",
          "base_increment": "0.00000001",
          "quote_increment": "0.00000001",
          "quote_min_size": "0.00000001",
          "quote_max_size": "1000",
          "base_min_size": "0.00000001",
          "base_max_size": "1000",
          "base_name": "Bitcoin",
          "quote_name": "US Dollar",
          "watched": true,
          "is_disabled": false,
          "new": true,
          "status": "<string>",
          "cancel_only": true,
          "limit_only": true,
          "post_only": true,
          "trading_disabled": false,
          "auction_mode": true,
          "base_display_symbol": "BTC",
          "quote_display_symbol": "USD",
          "product_type": "UNKNOWN_PRODUCT_TYPE",
          "quote_currency_id": "USD",
          "base_currency_id": "BTC",
          "fcm_trading_session_details": {
            "is_session_open": true,
            "open_time": "<string>",
            "close_time": "<string>",
            "session_state": "FCM_TRADING_SESSION_STATE_UNDEFINED",
            "after_hours_order_entry_disabled": true,
            "closed_reason": "FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED",
            "maintenance": {
              "start_time": "<string>",
              "end_time": "<string>"
            }
          },
          "mid_market_price": "140.22",
          "alias": "BTC-USD",
          "alias_to": [
            "BTC-USDC"
          ],
          "view_only": true,
          "price_increment": "0.00000001",
          "display_name": "BTC PERP",
          "product_venue": "neptune",
          "approximate_quote_24h_volume": "1908432",
          "new_at": "2021-07-01T00:00:00.000Z",
          "market_cap": "1500000000000",
          "icon_color": "red",
          "icon_url": "https://metadata.cbhq.net/equity_icons/123456789.png",
          "display_name_overwrite": "Bitcoin Perpetual",
          "is_alpha_testing": false,
          "about_description": "nano Crude Oil Futures is a monthly cash-settled contract that allows participants to manage risk, trade on margin, or speculate on the price of oil.",
          "best_bid_price": "<string>",
          "best_ask_price": "<string>",
          "future_product_details": {
            "venue": "<string>",
            "contract_code": "<string>",
            "contract_expiry": "<string>",
            "contract_size": "<string>",
            "contract_root_unit": "<string>",
            "group_description": "<string>",
            "contract_expiry_timezone": "<string>",
            "group_short_description": "<string>",
            "risk_managed_by": "UNKNOWN_RISK_MANAGEMENT_TYPE",
            "contract_expiry_type": "UNKNOWN_CONTRACT_EXPIRY_TYPE",
            "perpetual_details": {
              "open_interest": "<string>",
              "funding_rate": "<string>",
              "funding_time": "<string>",
              "max_leverage": "<string>",
              "base_asset_uuid": "<string>",
              "underlying_type": "<string>"
            },
            "contract_display_name": "<string>",
            "time_to_expiry_ms": "<string>",
            "non_crypto": true,
            "contract_expiry_name": "<string>",
            "twenty_four_by_seven": true,
            "funding_interval": "<string>",
            "open_interest": "<string>",
            "funding_rate": "<string>",
            "funding_time": "<string>",
            "display_name": "<string>",
            "region_enabled": {},
            "intraday_margin_rate": {
              "long_margin_rate": "0.5",
              "short_margin_rate": "0.5"
            },
            "overnight_margin_rate": {
              "long_margin_rate": "0.5",
              "short_margin_rate": "0.5"
            },
            "settlement_price": "<string>",
            "futures_asset_type": "UNKNOWN_FUTURES_ASSET_TYPE",
            "index_price": "<string>",
            "contract_code_display_name": "<string>",
            "product_group_cbrn": "<string>"
          }
        }
      ],
      "num_products": 100,
      "pagination": {
        "prev_cursor": "<string>",
        "next_cursor": "<string>",
        "has_next": true,
        "has_prev": true
      }
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

limit

integer<int32>

The number of products to be returned.

offset

integer<int32>

The number of products to skip before returning.

product_type

enum<string>

default:UNKNOWN_PRODUCT_TYPE

Only returns the orders matching this product type. By default, returns all product types.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

product_ids

string[]

The list of trading pairs (e.g. 'BTC-USD').

contract_expiry_type

enum<string>

default:UNKNOWN_CONTRACT_EXPIRY_TYPE

Only returns the orders matching the contract expiry type. Only applicable if product_type is set to FUTURE.

Available options:

`UNKNOWN_CONTRACT_EXPIRY_TYPE`,

`EXPIRING`,

`PERPETUAL`

expiring_contract_status

enum<string>

default:UNKNOWN_EXPIRING_CONTRACT_STATUS

Only returns contracts with this status (default is UNEXPIRED).

Available options:

`UNKNOWN_EXPIRING_CONTRACT_STATUS`,

`STATUS_UNEXPIRED`,

`STATUS_EXPIRED`,

`STATUS_ALL`

get_tradability_status

boolean

Whether or not to populate view_only with the tradability status of the product. This is only enabled for SPOT products.

get_all_products

boolean

If true, return all products of all product types (including expired futures contracts).

products_sort_order

enum<string>

default:PRODUCTS_SORT_ORDER_UNDEFINED

The order in which products are returned. By default, products are returned in 24 hour volume descending (in quote).

Available options:

`PRODUCTS_SORT_ORDER_UNDEFINED`,

`PRODUCTS_SORT_ORDER_VOLUME_24H_DESCENDING`,

`PRODUCTS_SORT_ORDER_LIST_TIME_DESCENDING`

cursor

string

The cursor to use for pagination. This will be a base64 encoded string that decodes into the last productId of the previously returned page

futures_underlying_type

enum<string>

default:UNKNOWN_FUTURES_UNDERLYING_TYPE

Only returns the products matching the underlying type. Only applicable if product_type is set to FUTURE.

Available options:

`UNKNOWN_FUTURES_UNDERLYING_TYPE`,

`FUTURES_UNDERLYING_TYPE_SPOT`,

`FUTURES_UNDERLYING_TYPE_INDEX`,

`FUTURES_UNDERLYING_TYPE_EQUITY`,

`FUTURES_UNDERLYING_TYPE_EQUITY_INDEX`,

`FUTURES_UNDERLYING_TYPE_EQUITY_ETF`,

`FUTURES_UNDERLYING_TYPE_PREIPO`,

`FUTURES_UNDERLYING_TYPE_COMMOD`,

`FUTURES_UNDERLYING_TYPE_COMMOD_ETF`,

`FUTURES_UNDERLYING_TYPE_COMMOD_INDEX`,

`FUTURES_UNDERLYING_TYPE_ADR`,

`FUTURES_UNDERLYING_TYPE_FOREIGN_EQUITY`,

`FUTURES_UNDERLYING_TYPE_OTC`

user_country_code

string

The country code of the user. This is used to provide differentiated product display names.

#### Response

A successful response.

products

Get Products · object[]

Array of objects, each representing one product.

num_products

integer<int32>

Number of products that were returned.

Example:

`100`

pagination

object

Pagination metadata for paginated responses.