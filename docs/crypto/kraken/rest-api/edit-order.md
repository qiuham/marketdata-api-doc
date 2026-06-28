---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/edit-order
api_type: REST
updated_at: 2026-05-27 20:01:31.501010
---

# Edit Order

**POST** `https://api.kraken.com/0/private/EditOrder`

Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be created with the adjusted parameters a new `txid` will be returned in the response.

note

The new [AmendOrder](/api/docs/rest-api/amend-order) endpoint resolves the caveats listed below and has additional performance gains.

There are a number of caveats for `EditOrder`:

  * triggered stop loss or profit take profit orders are not supported.
  * orders with conditional close terms attached are not supported.
  * orders where the executed volume is greater than the newly supplied volume will be rejected.
  * `cl_ord_id` is not supported.
  * existing executions will are associated with the original order and not copied to the amended order.
  * queue position will not be maintained.

**API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**userref** `integer<int32>`

User reference id

`userref` is an optional user-specified integer id associated with edit request.

> Note: userref from parent order will not be retained on the new order after edit.

**txid** `object` *required*

Original Order ID or User Reference Id (userref) which is user-specified integer id used with the original order. If userref is not unique and was used with multiple order, edit request is denied with an error.

oneOf
* string
* integer

****string

****integer

    ↳ **volume** `string`

Order quantity in terms of the base asset.

    ↳ **displayvol** `string`

For `iceberg` orders only, it defines the quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of `volume`.

    ↳ **pair** `string` *required*

Asset pair `id` or `altname`

    ↳ **asset_class** `string`

This parameter is required on requests for non-crypto pairs, i.e. use `tokenized_asset` for xstocks.

**Possible values:** [`tokenized_asset`]

    ↳ **price** `string`

Price:
* Limit price for `limit` and `iceberg` orders
* Trigger price for `stop-loss`, `stop-loss-limit`, `take-profit`, `take-profit-limit`, `trailing-stop` and `trailing-stop-limit` orders

Notes:
* Relative Prices: Either `price` or `price2` can be preceded by `+`, `-`, or `#` to specify the order price as an offset relative to the last traded price. `+` adds the amount to, and `-` subtracts the amount from the last traded price. `#` will either add or subtract the amount to the last traded price, depending on the direction and order type used. Prices can also be suffixed with a `%` to signify the relative amount as a percentage, rather than an absolute price difference.
* Trailing Stops: Must use a relative price for this field, namely the `+` prefix, from which the direction will be automatic based on if the original order is a buy or sell (no need to use `-` or `#`). The `%` suffix also works for these order types to use a relative percentage price.

**price2** string

Secondary Price:
* Limit price for `stop-loss-limit`, `take-profit-limit` and `trailing-stop-limit` orders Note:
* Trailing Stops: Must use a relative price for this field, namely one of the `+` or `-` prefixes. This will provide the offset from the trigger price to the limit price, i.e. +0 would set the limit price equal to the trigger price. The `%` suffix also works for this field to use a relative percentage limit price.

**oflags**

Comma delimited list of order flags. Only these flags can be changed: - post post-only order (available when ordertype = limit). All the flags from the parent order are retained except post-only. post-only needs to be explicitly mentioned on edit request.

    ↳ **deadline** `string`

RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine should reject the new order request, in presence of latency or order queueing. min now() + 2 seconds, max now() + 60 seconds.

    ↳ **cancel_response** `boolean`

Used to interpret if client wants to receive pending replace, before the order is completely replaced

    ↳ **validate** `boolean`

Validate inputs only. Do not submit order.

**Default value:**`false`

## Responses

  * 200

Order edited.

  * application/json
* Schema
  * Limit with conditional stop-loss

**Schema**

**result** `object`

    ↳ **descr** `object`

Order description info

        ↳ **order** `string`

Order description

        ↳ **txid** `string`

New Transaction ID   
(if order was added successfully)

        ↳ **newuserref** `string`

Original userref if passed with the request

        ↳ **olduserref** `string`

Original userref if passed with the request

        ↳ **orders_cancelled** `integer`

Number of orders cancelled (either 0 or 1)

        ↳ **originaltxid** `string`

Original transaction ID

        ↳ **status** `string`

Status of the order: Ok or Err

        ↳ **volume** `string`

Updated volume

        ↳ **price** `string`

Updated price

**price2** string

Updated price2

        ↳ **error_message** `string`

Error message if unsuccessful

**error** `array[]`

    
    
    {  
      "error": [],  
      "result": {  
        "status": "ok",  
        "txid": "OFVXHJ-KPQ3B-VS7ELA",  
        "originaltxid": "OHYO67-6LP66-HMQ437",  
        "volume": "0.00030000",  
        "price": "19500.0",  
        "price2": "32500.0",  
        "orders_cancelled": 1,  
        "descr": {  
          "order": "buy 0.00030000 XXBTZGBP @ limit 19500.0"  
        }  
      }  
    }  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/EditOrder' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "pair": "XBTUSD",  
      "txid": "OHYO67-6LP66-HMQ437",  
      "volume": "1.25",  
      "price": "27500",  
      "price2": "26500"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828490,
      "pair": "XBTUSD",
      "txid": "OHYO67-6LP66-HMQ437",
      "volume": "1.25",
      "price": "27500",
      "price2": "26500"
    }