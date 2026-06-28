---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-deposit-methods
api_type: REST
updated_at: 2026-05-27 20:02:44.020639
---

# Get Deposit Methods

**POST** `https://api.kraken.com/0/private/DepositMethods`

Retrieve methods available for depositing a particular asset.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being deposited

**aclass** `string`

Asset class being deposited (optional)

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**rebase_multiplier** `stringnullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Deposit methods retrieved.

  * application/json
* Schema

**Schema**

**result** `object[]`

  * Array [

**method** `string`

Name of deposit method

**limit**

Maximum net amount that can be deposited right now, or false if no limit

**fee** `string`

Amount of fees that will be paid

**address-setup-fee** string

Whether or not method has an address setup fee

**gen-address** boolean

Whether new addresses can be generated for this method.

**minimum** `string`

Minimum net amount that can be deposited right now

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/DepositMethods' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT"  
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
      "asset": "XBT"
    }