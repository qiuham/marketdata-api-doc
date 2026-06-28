---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/cancel-all-orders-after
api_type: REST
updated_at: 2026-05-27 20:00:47.952540
---

# Cancel All Orders After X

**POST** `https://api.kraken.com/0/private/CancelAllOrdersAfter`

CancelAllOrdersAfter provides a "Dead Man's Switch" mechanism to protect the client from network malfunction, extreme latency or unexpected matching engine downtime. The client can send a request with a timeout (in seconds), that will start a countdown timer which will cancel _all_ client orders when the timer expires. The client has to keep sending new requests to push back the trigger time, or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief disconnection or transient delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime - planned or otherwise).

**API Key Permissions Required:** `Orders and trades - Create & modify orders` or `Orders and trades - Cancel & close orders`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**timeout** `integer` *required*

Duration (in seconds) to set/extend the timer, it should be less than 86400 seconds.

## Responses

  * 200

Dead man's switch timer reset or disabled.

  * application/json
* Schema

**Schema**

**result** `object`

**currentTime** string

Timestamp (RFC3339 format) at which the request was received

**triggerTime** string

Timestamp (RFC3339 format) after which all orders will be cancelled, unless the timer is extended or disabled

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/CancelAllOrdersAfter' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "timeout": 120  
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
      "timeout": 120
    }