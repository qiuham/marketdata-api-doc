---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/add-export
api_type: REST
updated_at: 2026-05-27 20:00:04.620249
---

# Request Export Report

**POST** `https://api.kraken.com/0/private/AddExport`

Request export of trades or ledgers.

**API Key Permissions Required:** `Data - Export data`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**report** `string` *required*

Type of data to export

**Possible values:** [`trades`, `ledgers`]

**format** `string`

File format to export

**Possible values:** [`CSV`, `TSV`]

**Default value:**`CSV`

**description** `string` *required*

Description for the export

**fields** `string`

Comma-delimited list of fields to include
* `trades`: `ordertxid`, `time`, `ordertype`, `price`, `cost`, `fee`, `vol`, `margin`, `misc`, `ledgers`
* `ledgers`: `refid`, `time`, `type`, `subtype`, `aclass`, `asset`, `amount`, `fee`, `balance`, `wallet`

**Default value:**`all`

**starttm** `integer`

UNIX timestamp for report start time (default 1st of the current month)

**endtm** `integer`

UNIX timestamp for report end time (default now)

## Responses

  * 200

Export request made

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **id** `string`

Report ID

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/AddExport' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "report": "trades",  
      "description": "yearly report",  
      "format": "CSV",  
      "starttm": 1695728276,  
      "endtm": 1695828276  
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
      "report": "trades",
      "description": "yearly report",
      "format": "CSV",
      "starttm": 1695728276,
      "endtm": 1695828276
    }