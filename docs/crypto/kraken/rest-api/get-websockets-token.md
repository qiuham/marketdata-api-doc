---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-websockets-token
api_type: WebSocket
updated_at: 2026-05-27 20:06:00.434535
---

# Get Websockets Token

**POST** `https://api.kraken.com/0/private/GetWebSocketsToken`

An authentication token must be requested via this REST API endpoint in order to connect to and authenticate with our [Websockets API](/api/docs/guides/spot-ws-auth). The token should be used within 15 minutes of creation, but it does not expire once a successful Websockets connection and private subscription has been made and is maintained.

**API Key Permissions Required:** `WebSocket interface - On`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

## Responses

  * 200

Websockets token retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **token** `string`

Websockets token

    ↳ **expires** `integer`

Time (in seconds) after which the token expires

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/GetWebSocketsToken' \  
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