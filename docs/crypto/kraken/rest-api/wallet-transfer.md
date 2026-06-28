---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/wallet-transfer
api_type: REST
updated_at: 2026-05-27 20:08:34.590377
---

# Request Wallet Transfer

**POST** `https://api.kraken.com/0/private/WalletTransfer`

Transfer from a Kraken spot wallet to a Kraken Futures wallet. Note that a transfer in the other direction must be requested via the Kraken Futures API endpoint for [withdrawals to Spot wallets](/api/docs/futures-api/trading/withdrawal).

**API Key Permissions Required:** `Funds permissions - Query`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset to transfer (asset ID or `altname`)

**Example:**`XBT`

**from** `string` *required*

Source wallet

**Possible values:** [`Spot Wallet`]

**to** `string` *required*

Destination wallet

**Possible values:** [`Futures Wallet`]

**amount** `string` *required*

Amount to transfer

## Responses

  * 200

Transfer created.

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **refid** `string`

Reference ID

**Example:**`FTQcuak-V6Za8qrWnhzTx67yYHz8Tg`

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WalletTransfer' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "from": "Spot Wallet",  
      "to": "Futures Wallet",  
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
      "from": "Spot Wallet",
      "to": "Futures Wallet",
      "amount": "2.54"
    }