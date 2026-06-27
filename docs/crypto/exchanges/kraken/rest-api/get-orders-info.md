---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-orders-info
api_type: REST
updated_at: 2026-05-27 20:04:05.150117
---

# Query Orders Info

**POST** `https://api.kraken.com/0/private/QueryOrders`

Retrieve information about specific orders.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and trades - Query closed orders & trades`, depending on status of order

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**trades** `boolean`

Whether or not to include trades related to position in output

**Default value:**`false`

**userref** `integer<int32>`

Restrict results to given user reference id

**txid** `string` *required*

The Kraken order identifier. To query multiple orders, use comma delimited list of up to 50 ids.

**consolidate_taker** `boolean`

Whether or not to consolidate trades by individual taker trades

**Default value:**`true`

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Orders info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

txid of the order.

oneOf
* OpenOrder
* txid

    ↳ **refid** `stringnullable`

Referral order transaction ID that created this order

    ↳ **userref** `integernullable`

Optional numeric, client identifier associated with one or more orders.

    ↳ **cl_ord_id** `stringnullable`

Optional alphanumeric, client identifier associated with the order.

    ↳ **status** `string`

Status of order
* pending = order pending book entry
* open = open order
* closed = closed order
* canceled = order canceled
* expired = order expired

**Possible values:** [`pending`, `open`, `closed`, `canceled`, `expired`]

    ↳ **opentm** `number`

Unix timestamp of when order was placed

    ↳ **starttm** `number`

Unix timestamp of order start time (or 0 if not set)

    ↳ **expiretm** `number`

Unix timestamp of order end time (or 0 if not set)

    ↳ **descr** `object`

Order description info

        ↳ **pair** `string`

Asset pair

        ↳ **type** `string`

Type of order (buy/sell)

**Possible values:** [`buy`, `sell`]

        ↳ **ordertype** `ordertype (string)`

The execution model of the order.

**Possible values:** [`market`, `limit`, `iceberg`, `stop-loss`, `take-profit`, `stop-loss-limit`, `take-profit-limit`, `trailing-stop`, `trailing-stop-limit`, `settle-position`]

**Example:**`limit`

        ↳ **price** `string`

primary price

**price2** string

Secondary price

        ↳ **leverage** `string`

Amount of leverage

        ↳ **order** `string`

Order description

        ↳ **close** `string`

Conditional close order description (if conditional close set)

        ↳ **vol** `string`

Volume of order (base currency)

        ↳ **vol_exec** `string`

Volume executed (base currency)

        ↳ **cost** `string`

Total cost (quote currency unless)

        ↳ **fee** `string`

Total fee (quote currency)

        ↳ **price** `string`

Average price (quote currency)

        ↳ **stopprice** `string`

Stop price (quote currency)

        ↳ **limitprice** `string`

Triggered limit price (quote currency, when limit based order type triggered)

        ↳ **trigger** `string`

Price signal used to trigger "stop-loss" "take-profit" "stop-loss-limit" "take-profit-limit" orders.
* `last` is the implied trigger if this field is not set.

**Possible values:** [`last`, `index`]

**Default value:**`last`

        ↳ **margin** `boolean`

Indicates if the order is funded on margin.

        ↳ **misc** `string`

Comma delimited list of miscellaneous info
* `stopped` triggered by stop price
* `touched` triggered by touch price
* `liquidated` liquidation
* `partial` partial fill
* `amended` order parameters modified

        ↳ **sender_sub_id** `stringnullable`

For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).

        ↳ **oflags** `oflags (string)`

Comma delimited list of order flags
* • `post` post-only order (available when ordertype = limit)
* • `fcib` prefer fee in base currency (default if selling)
* • `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
* • `nompp` (DEPRECATED) — disabling Market Price Protection for market orders is no longer supported. If supplied, the flag is accepted but ignored.
* • `viqc` order volume expressed in quote currency. This option is supported only for buy market orders. Also not available on margin orders.

**Example:**`post`

        ↳ **trades** `string[]`

List of trade IDs related to order (if trades info requested and data available)

        ↳ **refid** `stringnullable`

Referral order transaction ID that created this order

        ↳ **userref** `integernullable`

Optional numeric, client identifier associated with one or more orders.

        ↳ **cl_ord_id** `stringnullable`

Optional alphanumeric, client identifier associated with the order.

        ↳ **status** `string`

Status of order
* pending = order pending book entry
* open = open order
* closed = closed order
* canceled = order canceled
* expired = order expired

**Possible values:** [`pending`, `open`, `closed`, `canceled`, `expired`]

        ↳ **opentm** `number`

Unix timestamp of when order was placed

        ↳ **starttm** `number`

Unix timestamp of order start time (or 0 if not set)

        ↳ **expiretm** `number`

Unix timestamp of order end time (or 0 if not set)

        ↳ **descr** `object`

Order description info

            ↳ **pair** `string`

Asset pair

            ↳ **type** `string`

Type of order (buy/sell)

**Possible values:** [`buy`, `sell`]

            ↳ **ordertype** `string`

Order type

**Possible values:** [`market`, `limit`, `iceberg`, `stop-loss`, `take-profit`, `trailing-stop`, `stop-loss-limit`, `take-profit-limit`, `trailing-stop-limit`, `settle-position`]

            ↳ **price** `string`

primary price

**price2** string

Secondary price

            ↳ **leverage** `string`

Amount of leverage

            ↳ **order** `string`

Order description

            ↳ **close** `string`

Conditional close order description (if conditional close set)

            ↳ **vol** `string`

Volume of order (base currency)

            ↳ **vol_exec** `string`

Volume executed (base currency)

            ↳ **cost** `string`

Total cost (quote currency unless)

            ↳ **fee** `string`

Total fee (quote currency)

            ↳ **price** `string`

Average price (quote currency)

            ↳ **stopprice** `string`

Stop price (quote currency)

            ↳ **limitprice** `string`

Triggered limit price (quote currency, when limit based order type triggered)

            ↳ **trigger** `string`

Price signal used to trigger "stop-loss" "take-profit" "stop-loss-limit" "take-profit-limit" orders.
* `last` is the implied trigger if this field is not set.

**Possible values:** [`last`, `index`]

**Default value:**`last`

            ↳ **margin** `boolean`

Indicates if the order is funded on margin.

            ↳ **misc** `string`

Comma delimited list of miscellaneous info:
* `stopped` triggered by stop price
* `touched` triggered by touch price
* `liquidated` liquidation
* `partial` partial fill
* `amended` order parameters modified

            ↳ **oflags** `string`

Comma delimited list of order flags:
* `post` post-only order (available when ordertype = limit)
* `fcib` prefer fee in base currency (default if selling)
* `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
* `nompp` disable [market price protection](https://support.kraken.com/hc/en-us/articles/201648183-Market-Price-Protection) for market orders
* `viqc` order volumes expressed in quote currency.

            ↳ **trades** `string[]`

List of trade IDs related to order (if trades info requested and data available)

            ↳ **sender_sub_id** `stringnullable`

For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).

            ↳ **closetm** `number`

Unix timestamp of when order was closed

            ↳ **reason** `string`

Additional info on status (if any)

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/QueryOrders' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "trades": false,  
      "userref": 0,  
      "txid": "string",  
      "consolidate_taker": true,  
      "rebase_multiplier": "rebased"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required

  * Example (from schema)
  * Example Query 2 orders

    
    
    {
      "nonce": 0,
      "trades": false,
      "userref": 0,
      "txid": "string",
      "consolidate_taker": true,
      "rebase_multiplier": "rebased"
    }