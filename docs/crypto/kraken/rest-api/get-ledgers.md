---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-ledgers
api_type: REST
updated_at: 2026-05-27 20:03:06.842186
---

# Get Ledgers Info

**POST** `https://api.kraken.com/0/private/Ledgers`

Retrieve information about ledger entries. 50 results are returned at a time, the most recent by default.

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

**asset** `string`

Filter output by asset or comma delimited list of assets

**Default value:**`all`

**aclass** `string`

Filter output by asset class

**Default value:**`currency`

**type** `string`

Type of ledger to retrieve

**Possible values:** [`all`, `trade`, `deposit`, `withdrawal`, `transfer`, `margin`, `adjustment`, `rollover`, `credit`, `settled`, `staking`, `dividend`, `sale`, `nft_rebate`]

**Default value:**`all`

**start** `integer`

Starting unix timestamp or ledger ID of results (exclusive)

**end** `integer`

Ending unix timestamp or ledger ID of results (inclusive)

**ofs** `integer`

Result offset for pagination

**without_count** `boolean`

If true, does not retrieve count of ledger entries. Request can be noticeably faster for users with many ledger entries as this avoids an extra database query.

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

Ledgers Info

    ↳ **ledger** `object`

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

        ↳ **count** `integer`

Amount of available ledger info matching criteria

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Ledgers' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "type": "trade",  
      "start": 1695728276,  
      "end": 1695828276  
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
      "type": "trade",
      "start": 1695728276,
      "end": 1695828276
    }