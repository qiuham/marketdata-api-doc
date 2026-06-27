---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-methods
api_type: REST
updated_at: 2026-05-27 20:07:58.374042
---

# Get Withdrawal Methods

**POST** `https://api.kraken.com/0/private/WithdrawMethods`

Retrieve a list of withdrawal methods available for the user.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string`

Filter methods for specific asset

**aclass** `string`

Filter methods for specific asset class

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**network** `string`

Filter methods for specific network

**rebase_multiplier** `stringnullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Withdrawal methods retrieved.

  * application/json
* Schema

**Schema**

**result** `object[]`

Withdrawal Methods

  * Array [

    ↳ **asset** `string`

Name of asset being withdrawn

**method** `string`

Name of the withdrawal method

**network** `string`

Name of the blockchain or network being withdrawn on

**minimum** `string`

Minimum net amount that can be withdrawn right now

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WithdrawMethods' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "asset": "string",  
      "aclass": "currency",  
      "network": "string",  
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
      "asset": "string",
      "aclass": "currency",
      "network": "string",
      "rebase_multiplier": "rebased"
    }