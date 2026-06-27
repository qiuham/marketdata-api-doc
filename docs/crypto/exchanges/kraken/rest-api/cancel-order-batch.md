---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/cancel-order-batch
api_type: REST
updated_at: 2026-05-27 20:01:02.411248
---

# Cancel Order Batch

**POST** `https://api.kraken.com/0/private/CancelOrderBatch`

Cancel multiple open orders by `txid`, `userref` or `cl_ord_id`(maximum 50 total unique IDs/references)

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**orders** `object[]`

  * Array [

    ↳ **txid** `object`

Open order transaction IDs (txid) or user references (userref), up to a maximum of 50 total unique IDs/references.

oneOf
* string
* integer

****string

****integer

  * ]

        ↳ **cl_ord_ids** `object[]`

  * Array [

            ↳ **cl_ord_id** `string`

An alphanumeric client order identifier which uniquely identifies an open order for each client. Up to a maximum of 50 total unique IDs/references.

  * ]

## Responses

  * 200

Open order cancelled.

  * application/json
* Schema
  * Example

**Schema**

    
    
    {  
      "error": [],  
      "result": {  
        "count": 2  
      }  
    }  
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/CancelOrderBatch' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "orders": [  
        "OP5V2Y-RYKVL-ET3V3B",  
        "OP5V2Y-7YKVL-ET3V3B"  
      ]  
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
      "orders": [
        "OP5V2Y-RYKVL-ET3V3B",
        "OP5V2Y-7YKVL-ET3V3B"
      ]
    }