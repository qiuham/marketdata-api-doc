---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-trade-balance
api_type: REST
updated_at: 2026-05-27 20:05:28.829759
---

# Get Trade Balance

**POST** `https://api.kraken.com/0/private/TradeBalance`

Retrieve a summary of collateral balances, margin position valuations, equity and margin level.

**API Key Permissions Required:** `Orders and trades - Query open orders & trades`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string`

Base asset used to determine balance

**Default value:**`ZUSD`

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses

  * 200

Trade balances retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Account Balance

    ↳ **eb** `string`

Equivalent balance (combined balance of all currencies)

**Example:**`3224744.0162`

    ↳ **tb** `string`

Trade balance (combined balance of all equity currencies)

**Example:**`3224744.0162`

    ↳ **m** `string`

Margin amount of open positions

**Example:**`0.0000`

    ↳ **n** `string`

Unrealized net profit/loss of open positions

**Example:**`0.0000`

    ↳ **c** `string`

Cost basis of open positions

**Example:**`0.0000`

    ↳ **v** `string`

Current floating valuation of open positions

**Example:**`0.0000`

    ↳ **e** `string`

Equity: `trade balance + unrealized net profit/loss`

**Example:**`3224744.0162`

    ↳ **mf** `string`

Free margin: `Equity - initial margin (maximum margin available to open new positions)`

**Example:**`3224744.0162`

    ↳ **ml** `string`

Margin level: `(equity / initial margin) * 100`

**Example:**`0.0000`

    ↳ **uv** `string`

Unexecuted value: Value of unfilled and partially filled orders

**Example:**`0.0000`

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/TradeBalance' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828490,  
      "asset": "ZUSD"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828490,
      "asset": "ZUSD"
    }