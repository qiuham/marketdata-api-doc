---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/list-fills
api_type: Trading
updated_at: 2026-07-01 19:42:47.726021
---

# List Fills

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/orders/historical/fills`


Get a list of fills filtered by optional query parameters (`product_id`, `order_id`, etc).
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/orders/historical/fills \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "fills": [
        {
          "entry_id": "22222-2222222-22222222",
          "trade_id": "1111-11111-111111",
          "order_id": "0000-000000-000000",
          "trade_time": "2021-05-31T09:59:59.000Z",
          "trade_type": "FILL",
          "price": "10000.00",
          "size": "0.001",
          "commission": "1.25",
          "product_id": "BTC-USD",
          "sequence_timestamp": "2021-05-31T09:58:59.000Z",
          "liquidity_indicator": "UNKNOWN_LIQUIDITY_INDICATOR",
          "size_in_quote": false,
          "user_id": "3333-333333-3333333",
          "side": "",
          "retail_portfolio_id": "4444-444444-4444444",
          "fillSource": "FILL_SOURCE_UNKNOWN",
          "commission_detail_total": {
            "total_commission": "<string>",
            "gst_commission": "<string>",
            "withholding_commission": "<string>",
            "client_commission": "<string>",
            "venue_commission": "<string>",
            "regulatory_commission": "<string>",
            "clearing_commission": "<string>"
          }
        }
      ],
      "cursor": "789100",
      "proof_token_required": true
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

order_ids

string[]

The ID(s) of order(s).

trade_ids

string[]

The ID(s) of the trades of fills.

product_ids

string[]

The ID(s) of the product(s) to filter fills by.

start_sequence_timestamp

string<RFC3339 Timestamp>

Only fills with a trade time after the specified start date are returned.

end_sequence_timestamp

string<RFC3339 Timestamp>

Only fills with a trade time before the specified end date are returned.

retail_portfolio_id

string

(Deprecated) Only fills matching this retail portfolio id are returned. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

limit

integer<int64>

The number of fills to be returned (default is 100).

cursor

string

For paginated responses, returns all responses that come after this value.

sort_by

enum<string>

default:UNKNOWN_SORT_BY

Sort results by a field, results use unstable pagination. Default is sort by creation time

Available options:

`UNKNOWN_SORT_BY`,

`PRICE`,

`TRADE_TIME`

asset_filters

string[]

Only returns the fills where the quote, base or underlying asset matches the provided asset filter(s) (e.g. 'BTC').

order_types

enum<string>[]

Only returns fills for orders matching the specified order types (e.g. 'MARKET', 'LIMIT').

  * MARKET: A [market order](https://en.wikipedia.org/wiki/Order_\(exchange\)#Market_order)
  * LIMIT: A [limit order](https://en.wikipedia.org/wiki/Order_\(exchange\)#Limit_order)
  * STOP: A stop order is an order that becomes a market order when triggered
  * STOP_LIMIT: A stop order is a limit order that doesn't go on the book until it hits the stop price
  * BRACKET: A bracket order is a way to mitigate potential losses in volatile markets, consisting of a limit price leg and a stop trigger price.
  * TWAP: TWAP order is a way to split large buy/sell orders to smaller chunks to reduce market impact
  * ROLL_OPEN: ROLL_OPEN order is the open step order of a contract roll
  * ROLL_CLOSE: ROLL_CLOSE is the close step order in a contract roll
  * LIQUIDATION: LIQUIDATION is a special order type that is used to liquidate a position
  * SCALED: SCALED order is an order that is split into multiple child orders at incrementally increasing or decreasing prices

Available options:

`UNKNOWN_ORDER_TYPE`,

`MARKET`,

`LIMIT`,

`STOP`,

`STOP_LIMIT`,

`BRACKET`,

`TWAP`,

`ROLL_OPEN`,

`ROLL_CLOSE`,

`LIQUIDATION`,

`SCALED`

order_side

enum<string>

default:""

Only returns fills for orders matching the specified side ('BUY' or 'SELL'). By default, returns all sides.

Available options:

`BUY`,

`SELL`

product_types

enum<string>[]

Only returns fills for orders matching the specified product types (e.g. 'SPOT', 'FUTURE'). By default, returns all product types.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

proof_token

string

Optional proof token for 2FA validation when accessing transaction history (EU SCA compliance).

#### Response

A successful response.

fills

Represents a fill for an order in the system · object[]

All fills matching the filters.

cursor

string

For paginated responses, returns all responses that come after this value.

Example:

`"789100"`

proof_token_required

boolean

Indicates that a valid proof token is required to access this data (EU SCA compliance).

Example:

`true`