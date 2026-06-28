---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/amend-order
api_type: REST
updated_at: 2026-05-27 20:00:33.385415
---

# Amend Order

**POST** `https://api.kraken.com/0/private/AmendOrder`

The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

  * The order identifiers assigned by Kraken and/or client will stay the same.
  * Queue priority in the order book will be maintained where possible.
  * If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see [amend transaction guide](/api/docs/guides/spot-amends).

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**txid** `string`

The Kraken identifier for the order to be amended. Either `txid` or `cl_ord_id` is required.

**cl_ord_id** `string`

The client identifier for the order to be amended. Either `txid` or `cl_ord_id` is required.

**order_qty** `string`

The new order quantity in terms of the base asset.

**display_qty** `string`

For `iceberg` orders only, it defines the new quantity to show in the book while the rest of order quantity remains hidden. Minimum value is 1 / 15 of remaining order quantity.

**limit_price** `string`

The new limit price restriction on the order (for order types that support limit price only).

The relative pricing can be set by using the `+`, `-` prefixes and/or `%` suffix.
* • `+` adds the amount from the reference price, i.e. market rises 50 USD `"+50"`.
* • `-` subtracts the amount from the reference price, i.e. market drops 100 USD `"-100"`.

**trigger_price** `string`

The new trigger price to activate the order (for triggered order types only).

The relative pricing can be set by using the `+`, `-` prefixes and/or `%` suffix.
* • `+` adds the amount from the reference price, i.e. market rises 50 USD `"+50"`.
* • `-` subtracts the amount from the reference price, i.e. market drops 100 USD `"-100"`.

**pair** `string`

The `pair` is required on amends for non-crypto pairs, i.e. provide the pair symbol for xstocks.

**post_only** `boolean`

An optional flag for `limit_price` amends. If `true`, the limit price change will be rejected if the order cannot be posted passively in the book.

**Default value:**`false`

**deadline** `string`

RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine should reject the new order request, in presence of latency or order queueing. min now() + 2 seconds, max now() + 60 seconds.

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

## Responses

  * 200

A successful amend request will return the unique Kraken amend identifier.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **amend_id** `string`

The unique Kraken identifier generated for this amend transaction.

**error** `array[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/AmendOrder' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",  
      "order_qty": "1.25"  
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
      "cl_ord_id": "6d1b345e-2821-40e2-ad83-4ecb18a06876",
      "order_qty": "1.25"
    }