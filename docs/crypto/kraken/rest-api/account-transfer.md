---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/account-transfer
api_type: REST
updated_at: 2026-05-27 19:59:56.099574
---

# Account Transfer

**POST** `https://api.kraken.com/0/private/AccountTransfer`

Transfer funds to and from master and subaccounts. **Note:** `AccountTransfer` must be called using an API key from the master account.

**API Key Permissions Required:** `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being transferred

**asset_class** `string`

Specify the asset class of the asset being transferred

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**amount** `string` *required*

Amount of asset to transfer

**from** `string` *required*

Public account ID of the source account (Example ABCD 1234 EFGH 5678)

**to** `string` *required*

Public account ID of the destination account (Example ABCD 1234 EFGH 5678)

## Responses

  * 200

Funds transferred between accounts.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **transfer_id** `string`

Transfer ID

    ↳ **status** `string`

Transfer status, either `"pending"` or `"complete"`

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/AccountTransfer' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "from": "ABCD 1234 EFGH 5678",  
      "to": "IJKL 0987 MNOP 6543",  
      "amount": "2.54"  
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
      "from": "ABCD 1234 EFGH 5678",
      "to": "IJKL 0987 MNOP 6543",
      "amount": "2.54"
    }