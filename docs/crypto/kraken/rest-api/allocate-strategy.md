---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/allocate-strategy
api_type: REST
updated_at: 2026-05-27 20:00:26.141350
---

# Allocate Earn Funds

**POST** `https://api.kraken.com/0/private/Earn/Allocate`

Allocate funds to the Strategy.

Requires the `Earn Funds` API key permission. The amount must always be defined.

This method is asynchronous. A couple of preflight checks are performed synchronously on behalf of the method before it is dispatched further. The client is required to poll the result using the `/0/private/Earn/AllocateStatus` endpoint.

There can be only one (de)allocation request in progress for given user and strategy at any time. While the operation is in progress:

  1. `pending` attribute in `/Earn/Allocations` response for the strategy indicates that funds are being allocated,
  2. `pending` attribute in `/Earn/AllocateStatus` response will be true.

Following specific errors within `Earnings` class can be returned by this method:

  * Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
  * Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in progress`
  * Service temporarily unavailable: `EEarnings:Busy`. Try again in a few minutes.
  * User tier verification: `EEarnings:Permission denied:The user's tier is not high enough`
  * Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**amount** `string` *required*

The amount to allocate.

**strategy_id** `string` *required*

A unique identifier of the chosen earn strategy, as returned from `/0/private/Earn/Strategies`.

## Responses

  * 200

Response

  * application/json
* Schema

**Schema**

**error** `string[]`

**result** `booleannullable`

Will return `true` when the operation is successful, null when an error occurred.
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Earn/Allocate' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "amount": "4.3",  
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
      "amount": "4.3",
      "nonce": 30295839,
      "strategy_id": "ESRFUO3-Q62XD-WIOIL7"
    }