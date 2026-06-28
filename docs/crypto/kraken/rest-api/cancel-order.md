---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/cancel-order
api_type: REST
updated_at: 2026-05-27 20:00:55.187002
---

# Cancel Order

**POST** `https://api.kraken.com/0/private/CancelOrder`

Cancel a particular open order (or set of open orders) by `txid`, `userref` or `cl_ord_id`

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**txid** `object`

Kraken order identifier (txid) or user reference (userref)

oneOf
* string
* integer

****string

****integer

    ↳ **cl_ord_id** `string`

An alphanumeric client order identifier which uniquely identifies an open order for each client.

## Responses

  * 200

Open order cancelled.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **count** `integer<int32>`

Number of orders cancelled

    ↳ **pending** `boolean`

If true, orders are pending cancellation

**error** `array[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/CancelOrder' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "pair": "XBTUSD",  
      "txid": "OHYO67-6LP66-HMQ437"  
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
      "txid": "OHYO67-6LP66-HMQ437"
    }