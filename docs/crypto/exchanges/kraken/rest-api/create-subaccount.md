---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/create-subaccount
api_type: REST
updated_at: 2026-05-27 20:01:16.910050
---

# Create Subaccount

**POST** `https://api.kraken.com/0/private/CreateSubaccount`

Create a trading subaccount. **Note:** `CreateSubaccount` must be called using an API key from the master account.

**API Key Permissions Required:** `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**username** `string` *required*

Username for the subaccount

**email** `string` *required*

Email address for the subaccount

## Responses

  * 200

Subaccount created.

  * application/json
* Schema

**Schema**

**result** `boolean`

Whether subaccount creation was successful or not.

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/CreateSubaccount' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    --data-raw '{  
      "nonce": 1695828271,  
      "username": "abc123",  
      "email": "abc123@gmail.com"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828271,
      "username": "abc123",
      "email": "abc123@gmail.com"
    }