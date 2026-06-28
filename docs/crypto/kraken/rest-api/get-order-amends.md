---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-order-amends
api_type: REST
updated_at: 2026-05-27 20:03:50.618249
---

# Get Order Amends

**POST** `https://api.kraken.com/0/private/OrderAmends`

Retrieves an audit trail of amend transactions on the specified order. The list is ordered by ascending amend timestamp.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and trades - Query closed orders & trades`, depending on status of order.

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**order_id** `string`

The Kraken order identifier for the amended order.

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

The first entry contains the original order parameters and has amend_type of `original`.

  * application/json
* Schema

**Schema**

**result** `object`

The amend transaction history.

    ↳ **count** `integer`

The total count of new and amend transactions (i.e. includes the original order).

    ↳ **amends** `object[]`

  * Array [

        ↳ **amend_id** `string`

Kraken amend identifier

        ↳ **amend_type** `string`

The type of amend transaction:
* • `original`: original order values on order entry.
* • `user`: user requested amendment.
* • `restated`: engine order maintenance amendment.

**Possible values:** [`original`, `user`, `restated`]

        ↳ **order_qty** `string`

Order quantity in terms of the base asset.

        ↳ **display_qty** `string`

The quantity show in the book for iceberg orders.

        ↳ **remaining_qty** `string`

Remaining un-traded quantity on the order.

        ↳ **limit_price** `string`

The limit price restriction on the order.

        ↳ **trigger_price** `string`

The trigger price on trigger order types.

        ↳ **reason** `string`

Description of the reason for this amend.

        ↳ **post_only** `boolean`

Indicates if the transaction was restricted from taking liquidity.

        ↳ **timestamp** `integer`

The UNIX timestamp for the amend transaction.

  * ]
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/OrderAmends' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "order_id": "OVITN3-BFK3H-63K37C"  
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
      "order_id": "OVITN3-BFK3H-63K37C"
    }