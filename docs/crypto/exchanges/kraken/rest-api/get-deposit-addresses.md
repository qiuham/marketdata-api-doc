---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-deposit-addresses
api_type: REST
updated_at: 2026-05-27 20:02:36.788119
---

# Get Deposit Addresses

**POST** `https://api.kraken.com/0/private/DepositAddresses`

Retrieve (or generate a new) deposit addresses for a particular asset and method.

**API Key Permissions Required:** `Funds permissions - Query`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being deposited

**aclass** `string`

Asset class being deposited

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**method** `string` *required*

Name of the deposit method

**new** `boolean`

Whether or not to generate a new address

**Default value:**`false`

**amount** `object`

Amount you wish to deposit (only required for `method=Bitcoin Lightning`)

oneOf
* string
* integer
* number

****string

****integer

****number

## Responses

  * 200

Deposit addresses retrieved.

  * application/json
* Schema

**Schema**

**result** `object[]`

  * Array [

    ↳ **address** `string`

Deposit Address

    ↳ **expiretm** `string`

Expiration time in unix timestamp, or 0 if not expiring

    ↳ **new** `boolean`

Whether or not address has ever been used

    ↳ **tag** `string`

Contains tags for [XRP](https://support.kraken.com/hc/en-us/articles/360000184443-Destination-Tag-for-Ripple-XRP-deposits) deposit addresses and memos for [STX](https://support.kraken.com/hc/en-us/articles/10902306995860-Memo-for-Stacks-STX-deposits), [XLM](https://support.kraken.com/hc/en-us/articles/360000184543-Memo-for-Stellar-Lumens-XLM-deposits), and [EOS](https://support.kraken.com/hc/en-us/articles/360001099203-Memo-for-EOS-deposits) deposit addresses

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/DepositAddresses' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "method": "Bitcoin",  
      "new": true  
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
      "method": "Bitcoin",
      "new": true
    }