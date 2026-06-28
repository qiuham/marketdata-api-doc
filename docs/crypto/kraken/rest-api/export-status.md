---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/export-status
api_type: REST
updated_at: 2026-05-27 20:01:38.787240
---

# Get Export Report Status

**POST** `https://api.kraken.com/0/private/ExportStatus`

Get status of requested data exports.

**API Key Permissions Required:** `Data - Export data`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**report** `string` *required*

Type of reports to inquire about

**Possible values:** [`trades`, `ledgers`]

## Responses

  * 200

Export status retrieved

  * application/json
* Schema

**Schema**

**result** `object[]`

  * Array [

    ↳ **id** `string`

Report ID

    ↳ **descr** `string`

    ↳ **format** `string`

    ↳ **report** `string`

    ↳ **subtype** `string`

    ↳ **status** `string`

Status of the report

**Possible values:** [`Queued`, `Processing`, `Processed`]

    ↳ **flags** `stringdeprecated`

    ↳ **fields** `string`

    ↳ **createdtm** `string`

UNIX timestamp of report request

    ↳ **expiretm** `stringdeprecated`

    ↳ **starttm** `string`

UNIX timestamp report processing began

    ↳ **completedtm** `string`

UNIX timestamp report processing finished

    ↳ **datastarttm** `string`

UNIX timestamp of the report data start time

    ↳ **dataendtm** `string`

UNIX timestamp of the report data end time

    ↳ **aclass** `stringdeprecated`

    ↳ **asset** `string`

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/ExportStatus' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "report": "trades"  
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
      "report": "trades"
    }