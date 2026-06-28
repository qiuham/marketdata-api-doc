---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-open-positions
api_type: REST
updated_at: 2026-05-27 20:03:43.314684
---

# Get Open Positions

**POST** `https://api.kraken.com/0/private/OpenPositions`

Get information about open margin positions.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**txid** `string`

Comma delimited list of txids to limit output to

**docalcs** `boolean`

Whether to include P&L calculations

**Default value:**`false`

**consolidation** `string`

Consolidate positions by market/pair

**Possible values:** [`market`]

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Open positions info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

**property name*** txid

    ↳ **ordertxid** `string`

Order ID responsible for the position

    ↳ **posstatus** `string`

Position status

**Possible values:** [`open`]

    ↳ **pair** `string`

Asset pair

    ↳ **time** `number`

Unix timestamp of trade

    ↳ **type** `string`

Direction (buy/sell) of position

    ↳ **ordertype** `string`

Order type used to open position

    ↳ **cost** `string`

Opening cost of position (in quote currency)

    ↳ **fee** `string`

Opening fee of position (in quote currency)

    ↳ **vol** `string`

Position opening size (in base currency)

    ↳ **vol_closed** `string`

Quantity closed (in base currency)

    ↳ **margin** `string`

Initial margin consumed (in quote currency)

    ↳ **value** `string`

Current value of remaining position (if `docalcs` requested)

    ↳ **net** `string`

Unrealised P&L of remaining position (if `docalcs` requested)

    ↳ **terms** `string`

Funding cost and term of position

    ↳ **rollovertm** `string`

Timestamp of next margin rollover fee

    ↳ **misc** `string`

Comma delimited list of add'l info

    ↳ **oflags** `string`

Comma delimited list of opening order flags

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/OpenPositions' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "txid": "string",  
      "docalcs": false,  
      "consolidation": "market",  
      "rebase_multiplier": "rebased"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required

  * Example (from schema)
  * get Open Position

    
    
    {
      "nonce": 0,
      "txid": "string",
      "docalcs": false,
      "consolidation": "market",
      "rebase_multiplier": "rebased"
    }