---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/retrieve-export
api_type: REST
updated_at: 2026-05-27 20:08:27.434097
---

# Retrieve Data Export

**POST** `https://api.kraken.com/0/private/RetrieveExport`

Retrieve a processed data export

**API Key Permissions Required:** `Data - Export data`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**id** `string` *required*

Report ID to retrieve

## Responses

  * 200

Data export report retrieved

  * application/octet-stream
* Schema

**Schema**

**report** `string<binary>`

Binary zip archive containing the report
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/RetrieveExport' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/octet-stream' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "id": "1234556"  
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
      "id": "1234556"
    }