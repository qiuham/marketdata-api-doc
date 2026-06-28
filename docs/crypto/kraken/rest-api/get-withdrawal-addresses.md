---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-addresses
api_type: REST
updated_at: 2026-05-27 20:06:10.975668
---

# Get Withdrawal Addresses

**POST** `https://api.kraken.com/0/private/WithdrawAddresses`

Retrieve a list of withdrawal addresses available for the user.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string`

Filter addresses for specific asset

**aclass** `string`

Filter addresses for specific asset class

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**method** `string`

Filter addresses for specific method

**key** `string`

Find address for by withdrawal key name, as set up on your account

**verified** `boolean`

Filter by verification status of the withdrawal address. Withdrawal addresses successfully completing email confirmation will have a verification status of true.

## Responses

  * 200

Withdrawal addresses retrieved.

  * application/json
* Schema

**Schema**

**result** `object[]`

Withdrawal Addresses

  * Array [

    ↳ **address** `string`

Withdrawal address

    ↳ **asset** `string`

Name of asset being withdrawn

**method** `string`

Name of the withdrawal method

**key** `string`

Withdrawal key name, as set up on your account

**tag** `string`

Contains tags for [XRP](https://support.kraken.com/hc/en-us/articles/360000184443-Destination-Tag-for-Ripple-XRP-deposits) deposit addresses and memos for [STX](https://support.kraken.com/hc/en-us/articles/10902306995860-Memo-for-Stacks-STX-deposits), [XLM](https://support.kraken.com/hc/en-us/articles/360000184543-Memo-for-Stellar-Lumens-XLM-deposits), and [EOS](https://support.kraken.com/hc/en-us/articles/360001099203-Memo-for-EOS-deposits) deposit addresses

**verified** `boolean`

Verification status of withdrawal address

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WithdrawAddresses' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "asset": "string",  
      "aclass": "currency",  
      "method": "string",  
      "key": "string",  
      "verified": true  
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
      "method": "string",
      "key": "string",
      "verified": true
    }