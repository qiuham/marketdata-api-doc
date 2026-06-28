---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-ledgers-info
api_type: REST
updated_at: 2026-05-27 20:03:14.106704
---

# Query Ledgers

**POST** `https://api.kraken.com/0/private/QueryLedgers`

Retrieve information about specific ledger entries.

> **Note on Staking/Earn assets:** We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our [Support article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-) for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g. `USDT` to transact with your `USDT` and `USDT.F` balances).
> 
>   * `.B`, which represents balances in new yield-bearing products, similar to `.S` (staked) and `.M` (opt-in rewards) balances
>   * `.F`, which represents balances earning automatically in Kraken Rewards
> 

**API Key Permissions Required:** `Data - Query ledger entries`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**id** `string` *required*

Comma delimited list of ledger IDs to query info about (20 maximum)

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

Ledgers info retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

**property name*** LedgerEntry

Ledger Entry

    ↳ **refid** `string`

Reference Id of the parent transaction (trade, deposit, withdrawal, etc.) that caused the ledger entry.

    ↳ **time** `number`

Unix timestamp of ledger

    ↳ **type** `string`

Type of ledger entry

**Possible values:** [`none`, `trade`, `deposit`, `withdrawal`, `transfer`, `margin`, `adjustment`, `rollover`, `spend`, `receive`, `settled`, `credit`, `staking`, `reward`, `dividend`, `sale`, `conversion`, `nfttrade`, `nftcreatorfee`, `nftrebate`, `custodytransfer`]

    ↳ **subtype** `string`

Additional info relating to the ledger entry type, where applicable

    ↳ **aclass** `string`

Asset class

    ↳ **asset** `string`

Asset

    ↳ **amount** `string`

Transaction amount

    ↳ **fee** `string`

Transaction fee

    ↳ **balance** `string`

Resulting balance

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/QueryLedgers' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "id": "LUI2RA-CJFLB-EN5I4P, L2QE42-IGSZ3-WEVTLK",  
      "trade": false  
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
      "id": "LUI2RA-CJFLB-EN5I4P, L2QE42-IGSZ3-WEVTLK",
      "trade": false
    }