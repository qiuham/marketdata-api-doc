---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-account-balance
api_type: REST
updated_at: 2026-05-27 20:01:46.018130
---

# Get Account Balance

**POST** `https://api.kraken.com/0/private/Balance`

Retrieve all cash balances, net of pending withdrawals.

**Note on Staking/Earn assets:** We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our [Support article](https://support.kraken.com/hc/en-us/articles/360039879471-What-is-Asset-S-and-Asset-M-) for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g. `USDT` to transact with your `USDT` and `USDT.F` balances).

**Symbol Extensions** :

  * `.B`: balances in new yield-bearing products, similar to `.S` (staked) and `.M` (opt-in rewards) balances
  * `.F`: balances earning automatically in Kraken Rewards
  * `.T`: tokenized assets.

**API Key Permissions Required:** `Funds permissions - Query`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Account balances retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Account Balance

**property name*** string

balance

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Balance' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "rebase_multiplier": "rebased"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 0,
      "rebase_multiplier": "rebased"
    }