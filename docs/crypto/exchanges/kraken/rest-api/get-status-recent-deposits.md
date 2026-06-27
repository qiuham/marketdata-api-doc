---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-status-recent-deposits
api_type: REST
updated_at: 2026-05-27 20:04:49.075774
---

# Get Status of Recent Deposits

**POST** `https://api.kraken.com/0/private/DepositStatus`

Retrieve information about recent deposits. Results are sorted by recency, use the `cursor` parameter to iterate through list of deposits (page size equal to value of `limit`) from newest to oldest. **API Key Permissions Required:** `Funds permissions - Query`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string`

Filter for specific asset being deposited

**aclass** `string`

Filter for specific asset class being deposited

**Possible values:** [`currency`, `tokenized_asset`]

**Default value:**`currency`

**method** `string`

Filter for specific name of deposit method

**start** `string`

Start timestamp, deposits created strictly before will not be included in the response

**end** `string`

End timestamp, deposits created strictly after will be not be included in the response

**cursor** `object`

true/false to enable/disable paginated response (boolean) or cursor for next page of results (string)

anyOf
* MOD1
* MOD2

****boolean

Enable/disable paginated response

****string

Cursor for next page of results

    ↳ **limit** `integer`

Number of results to include per page

**Default value:**`25`

    ↳ **rebase_multiplier** `stringnullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Recent deposits retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

anyOf
* deposit
* MOD2

**method** `string`

Name of deposit method

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

Amount deposited

**fee**

Fees paid

**time** `integer<int32>`

Unix timestamp when request was made

**status** `string`

Status of deposit  
For additional information about the status, please refer to the [IFEX financial transaction states](https://github.com/globalcitizen/ifex-protocol/blob/master/draft-ifex-00.txt#L837).

**Possible values:** [`Initial`, `Pending`, `EarlyConfirmed`, `Settled`, `Success`, `Failure`]

**status-prop** string

Addition status properties (if available)  
* `return` A return transaction initiated by Kraken
* `onhold` Deposit is on hold pending review

**Possible values:** [`return`, `onhold`]

**originators** `string[]`

Client sending transaction id(s) for deposits that credit with a sweeping transaction

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/DepositStatus' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "method": "Bitcoin"  
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
      "method": "Bitcoin"
    }