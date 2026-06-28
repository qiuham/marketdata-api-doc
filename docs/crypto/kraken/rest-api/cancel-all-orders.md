---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/cancel-all-orders
api_type: REST
updated_at: 2026-05-27 20:00:40.626904
---

# Cancel All Orders

**POST** `https://api.kraken.com/0/private/CancelAll`

Cancel all open orders

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

## Responses

  * 200

Open orders cancelled.

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

    
    
    curl -L 'https://api.kraken.com/0/private/CancelAll' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828436  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828436
    }