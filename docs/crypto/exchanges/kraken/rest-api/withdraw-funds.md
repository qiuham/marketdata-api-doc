---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/withdraw-funds
api_type: REST
updated_at: 2026-05-27 20:08:41.796357
---

# Withdraw Funds

**POST** `https://api.kraken.com/0/private/Withdraw`

Make a withdrawal request.

**API Key Permissions Required:** `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being withdrawn

**aclass** `string`

Specify the asset class of the asset being withdrawn

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**key** `string` *required*

Withdrawal key name, as set up on your account

**address** `string`

Optional, crypto address that can be used to confirm address matches key (will return `Invalid withdrawal address` error if different)

**amount** `string` *required*

Amount to be withdrawn

**max_fee** `string`

Optional, if the processed withdrawal fee is higher than `max_fee`, withdrawal will fail with `EFunding:Max fee exceeded`

**rebase_multiplier** `stringnullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Withdrawal created.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **refid** `string`

Reference ID

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/Withdraw' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "key": "btc_2709",  
      "amount": "0.725",  
      "address": "bc1kar0ssrr7xf3vy5l6d3lydnwkre5og2zz3f5ldq"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828271,
      "asset": "XBT",
      "key": "btc_2709",
      "amount": "0.725",
      "address": "bc1kar0ssrr7xf3vy5l6d3lydnwkre5og2zz3f5ldq"
    }