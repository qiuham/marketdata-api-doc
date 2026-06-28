---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/remove-export
api_type: REST
updated_at: 2026-05-27 20:08:20.240201
---

# Delete Export Report

**POST** `https://api.kraken.com/0/private/RemoveExport`

Delete exported trades/ledgers report

**API Key Permissions Required:** `Data - Export data`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**id** `string` *required*

ID of report to delete or cancel

**type** `string` *required*

`delete` can only be used for reports that have already been processed. Use `cancel` for queued or processing reports.

**Possible values:** [`cancel`, `delete`]

## Responses

  * 200

Export report deleted or cancelled

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **delete** `boolean`

Whether deletion was successful

    ↳ **cancel** `boolean`

Whether cancellation was successful

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/RemoveExport' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "id": "1234556",  
      "type": "cancel"  
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
      "id": "1234556",
      "type": "cancel"
    }