---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-deallocate-strategy-status
api_type: REST
updated_at: 2026-05-27 20:02:29.448525
---

# Get Deallocation Status

**POST** `https://api.kraken.com/0/private/Earn/DeallocateStatus`

Get the status of the last deallocation request.

Requires either the `Earn Funds` or `Query Funds` API key permission.

(De)allocation operations are asynchronous and this endpoint allows client to retrieve the status of the last dispatched operation. There can be only one (de)allocation request in progress for given user and strategy.

The `pending` attribute in the response indicates if the previously dispatched operation is still in progress (true) or has successfully completed (false). If the dispatched request failed with an error, then HTTP error is returned to the client as if it belonged to the original request.

Following specific errors within `Earnings` class can be returned by this method:

  * Insufficient funds: `EEarnings:Insufficient funds:Insufficient funds to complete the (de)allocation request`
  * Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**strategy_id** `string` *required*

ID of the earn strategy, call `Earn/Strategies` to list available strategies

## Responses

  * 200

Response

  * application/json
* Schema

**Schema**

**error** `string[]`

**result** `objectnullable`

Status of async earn operation

    ↳ **pending** `boolean`

`true` if an operation is still in progress on the same strategy.
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Earn/DeallocateStatus' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 30295839,  
      "strategy_id": "ESRFUO3-Q62XD-WIOIL7"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 30295839,
      "strategy_id": "ESRFUO3-Q62XD-WIOIL7"
    }