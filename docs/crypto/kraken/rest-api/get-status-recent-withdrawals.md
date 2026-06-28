---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-status-recent-withdrawals
api_type: REST
updated_at: 2026-05-27 20:04:56.966676
---

# Get Status of Recent Withdrawals

**POST** `https://api.kraken.com/0/private/WithdrawStatus`

Retrieve information about recent withdrawals. Results are sorted by recency, use the `cursor` parameter to iterate through list of withdrawals (page size equal to value of `limit`) from newest to oldest.

**API Key Permissions Required:** `Funds permissions - Withdraw` or `Data - Query ledger entries`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string`

Filter for specific asset being withdrawn

**aclass** `string`

Filter for specific asset class being withdrawn

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**method** `string`

Filter for specific name of withdrawal method

**start** `string`

Start timestamp, withdrawals created strictly before will not be included in the response

**end** `string`

End timestamp, withdrawals created strictly after will be not be included in the response

**cursor** `object`

true/false to enable/disable paginated response (boolean) or cursor for next page of results (string), default false

anyOf
* MOD1
* MOD2

****boolean

Enable/disable paginated response

****string

Cursor for next page of results

    ↳ **limit** `integer`

Number of results to include per page

**Default value:**`500`

    ↳ **rebase_multiplier** `stringnullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Recent withdrawals retrieved.

  * application/json
* Schema

**Schema**

**result** `object[]`

  * Array [

**method** `string`

Name of withdrawal method

**network** `string`

Network name based on the funding method used

**aclass** `string`

Asset class

**asset** `string`

Asset

**refid** `string`

Reference ID

**txid** `string`

Method transaction ID

**info** `string`

Method transaction information

**amount** `string`

Amount withdrawn

**fee**

Fees paid

**time** `integer<int32>`

Unix timestamp when request was made

**status** `string`

Status of withdraw  
For information about the status, please refer to the [IFEX financial transaction states](https://github.com/globalcitizen/ifex-protocol/blob/master/draft-ifex-00.txt#L837).

**Possible values:** [`Initial`, `Pending`, `Settled`, `Success`, `Failure`]

**status-prop** string

Addition status properties (if available)  
* `cancel-pending` cancelation requested
* `canceled` canceled
* `cancel-denied` cancelation requested but was denied
* `return` a return transaction initiated by Kraken; it cannot be canceled
* `onhold` withdrawal is on hold pending review

**Possible values:** [`cancel-pending`, `canceled`, `cancel-denied`, `return`, `onhold`]

**key** `string`

Withdrawal key name, as set up on your account

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WithdrawStatus' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "method": "bitcoin"  
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
      "method": "bitcoin"
    }