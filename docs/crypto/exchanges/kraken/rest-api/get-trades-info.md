---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-trades-info
api_type: REST
updated_at: 2026-05-27 20:05:52.506169
---

# Query Trades Info

**POST** `https://api.kraken.com/0/private/QueryTrades`

Retrieve information about specific trades/fills.

**API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**txid** `string` *required*

Comma delimited list of transaction IDs to query info about (20 maximum)

**trades** `boolean`

Whether or not to include trades related to position in output

**Default value:**`false`

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Trades info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Trade info

**property name*** Trade

Trade Info

    ↳ **ordertxid** `string`

Order responsible for execution of trade

    ↳ **postxid** `string`

Position responsible for execution of trade

    ↳ **pair** `string`

Asset pair

    ↳ **time** `number`

Unix timestamp of trade

    ↳ **type** `string`

Type of order (buy/sell)

    ↳ **ordertype** `string`

Order type

    ↳ **price** `string`

Average price order was executed at (quote currency)

    ↳ **cost** `string`

Total cost of order (quote currency)

    ↳ **fee** `string`

Total fee (quote currency)

    ↳ **vol** `string`

Volume (base currency)

    ↳ **margin** `string`

Initial margin (quote currency)

    ↳ **leverage** `string`

Amount of leverage used in trade

    ↳ **misc** `string`

Comma delimited list of miscellaneous info:
* `closing` — Trade closes all or part of a position

    ↳ **ledgers** `string[]`

List of ledger ids for entries associated with trade

    ↳ **trade_id** `integer`

Unique identifier of trade executed

    ↳ **maker** `boolean`

`true` if trade was executed with user as the maker, `false` if taker

    ↳ **posstatus** `string`

Position status (open/closed)   
Only present if trade opened a position

    ↳ **cprice** `number`

Average price of closed portion of position (quote currency)   
Only present if trade opened a position

    ↳ **ccost** `number`

Total cost of closed portion of position (quote currency)   
Only present if trade opened a position

    ↳ **cfee** `number`

Total fee of closed portion of position (quote currency)   
Only present if trade opened a position

    ↳ **cvol** `number`

Total fee of closed portion of position (quote currency)   
Only present if trade opened a position

    ↳ **cmargin** `number`

Total margin freed in closed portion of position (quote currency)   
Only present if trade opened a position

    ↳ **net** `number`

Net profit/loss of closed portion of position (quote currency, quote currency scale)   
Only present if trade opened a position

    ↳ **trades** `string[]`

List of closing trades for position (if available)   
Only present if trade opened a position

**error** `array[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/QueryTrades' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "txid": "L2QE42-IGSZ3-WEVTLK, STMH53C-C54CG-4SO42I",  
      "trades": false  
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
      "txid": "L2QE42-IGSZ3-WEVTLK, STMH53C-C54CG-4SO42I",
      "trades": false
    }