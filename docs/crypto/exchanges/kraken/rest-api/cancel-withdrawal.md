---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/cancel-withdrawal
api_type: REST
updated_at: 2026-05-27 20:01:09.676748
---

# Request Withdrawal Cancellation

**POST** `https://api.kraken.com/0/private/WithdrawCancel`

Cancel a recently requested withdrawal, if it has not already been successfully processed.

**API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a `WalletTransfer`, then no permissions are required.

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being withdrawn

**refid** `string` *required*

Withdrawal reference ID

## Responses

  * 200

Withdrawal cancellation requested.

  * application/json
* Schema

**Schema**

**result** `boolean`

Whether cancellation was successful or not.

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WithdrawCancel' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "refid": "FTQcuak-V6Za8qrWnhzTx67yYHz8Tg"  
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
      "refid": "FTQcuak-V6Za8qrWnhzTx67yYHz8Tg"
    }