---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-trade-history
api_type: REST
updated_at: 2026-05-27 20:05:35.780483
---

# Get Trades History

**POST** `https://api.kraken.com/0/private/TradesHistory`

Retrieve information about trades/fills. 50 results are returned at a time, the most recent by default.

  * Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

**API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**type** `string`

Type of trade

**Possible values:** [`all`, `any position`, `closed position`, `closing position`, `no position`]

**Default value:**`all`

**trades** `boolean`

Whether or not to include trades related to position in output

**Default value:**`false`

**start** `integer`

Starting unix timestamp or trade tx ID of results (exclusive)

**end** `integer`

Ending unix timestamp or trade tx ID of results (inclusive)

**ofs** `integer`

Result offset for pagination

**without_count** `boolean`

If true, does not retrieve count of ledger entries. Request can be noticeably faster for users with many ledger entries as this avoids an extra database query.

**Default value:**`false`

**consolidate_taker** `boolean`

Whether or not to consolidate trades by individual taker trades

**Default value:**`true`

**ledgers** `boolean`

Whether or not to include related ledger ids for given trade   
Note that setting this to true will slow request performance

**Default value:**`false`

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Trade history retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Trade History

    ↳ **count** `integer`

Amount of available trades matching criteria

    ↳ **trades** `object`

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

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/TradesHistory' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "type": "all",  
      "trades": false,  
      "consolidate_taker": true  
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
      "type": "all",
      "trades": false,
      "consolidate_taker": true
    }